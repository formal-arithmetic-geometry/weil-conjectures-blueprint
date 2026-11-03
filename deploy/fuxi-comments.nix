# The comment server of https://blueprint.fuxi.merten.dev, for fuxi's NixOS
# configuration (beside fuxi/blueprint.nix in chrisflav/nixos-config).
#
# The website posts and reads its comments at api/comments/<id> on its own
# address. nginx forwards those requests to the blueprint tool's comment
# server (web/comments-server.py), which the site build ships as
# comments-server.py at the root of the `site` branch. The server relays to
# the Zulip of comments-config.json (#Blueprint Comments) as the bot of its
# environment; the bot's email and key stay on fuxi and never reach a page.
#
# To adapt: `site` is the checkout of the `site` branch that nginx serves,
# and the secret file holds the two lines
#   BLUEPRINT_ZULIP_EMAIL=<the bot's email>
#   BLUEPRINT_ZULIP_KEY=<the bot's API key>
# (the repository secrets ZULIP_BOT_EMAIL / ZULIP_BOT_API_KEY).
{ pkgs, ... }:
let
  site = "/var/lib/blueprint/site"; # the checkout of the `site` branch nginx serves
  port = 8701;
in
{
  systemd.services.blueprint-comments = {
    description = "Comment server of blueprint.fuxi.merten.dev (relays to Zulip)";
    wantedBy = [ "multi-user.target" ];
    wants = [ "network-online.target" ];
    after = [ "network-online.target" ];
    serviceConfig = {
      ExecStart = "${pkgs.python3}/bin/python3 ${site}/comments-server.py"
        + " --directory ${site} --comments /var/lib/blueprint-comments"
        + " --bind 127.0.0.1 --port ${toString port}";
      EnvironmentFile = "/run/secrets/blueprint-zulip-bot";
      StateDirectory = "blueprint-comments"; # its files, unused while on Zulip
      DynamicUser = true;
      Restart = "on-failure";
    };
  };

  # A new site may bring a new comment server: restart it with the site.
  systemd.paths.blueprint-comments-update = {
    wantedBy = [ "multi-user.target" ];
    pathConfig.PathChanged = "${site}/comments-server.py";
  };
  systemd.services.blueprint-comments-update = {
    serviceConfig.Type = "oneshot";
    script = "systemctl try-restart blueprint-comments.service";
  };

  # Under the site's own password: if the password (auth_basic) is set on
  # location "/" rather than on the server, set it on this location too.
  services.nginx.virtualHosts."blueprint.fuxi.merten.dev".locations."/api/comments/" = {
    proxyPass = "http://127.0.0.1:${toString port}";
  };
}
