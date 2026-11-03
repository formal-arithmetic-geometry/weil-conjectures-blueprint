#!/usr/bin/env bash
# The website's comment server on fuxi: the relay that posts the comments of
# https://blueprint.fuxi.merten.dev to Zulip and reads them back, as the bot
# whose email and key only it holds (comments-server.py of the blueprint
# tool, chrisflav/blueprint#78).  It runs as a Docker container of an
# ordinary user, listening on 127.0.0.1 only; fuxi's nginx forwards the
# site's /api/comments/ to it.
#
# Run it from a checkout of this repository whose blueprint tool is fetched
# (`lake exe blueprint check` once), and again after the tool's pin moves:
#
#   deploy/comments-relay.sh
#
# It reads the bot from ~/.config/blueprint-comments/zulip.env, two lines
#   BLUEPRINT_ZULIP_EMAIL=<the bot's email>
#   BLUEPRINT_ZULIP_KEY=<the bot's API key>
# and keeps its files in ~/blueprint-comments.
set -euo pipefail
root=$(cd "$(dirname "$0")/.." && pwd)
home=${BLUEPRINT_COMMENTS_HOME:-$HOME/blueprint-comments}
envfile=${BLUEPRINT_COMMENTS_ENV:-$HOME/.config/blueprint-comments/zulip.env}
port=${BLUEPRINT_COMMENTS_PORT:-8701}
name=${BLUEPRINT_COMMENTS_NAME:-blueprint-comments}
server="$root/.lake/packages/blueprint/web/comments-server.py"

[ -r "$envfile" ] || { echo "no $envfile: put the bot's BLUEPRINT_ZULIP_EMAIL and BLUEPRINT_ZULIP_KEY there" >&2; exit 1; }
[ -r "$server" ] || { echo "no $server: fetch the blueprint tool first (lake exe blueprint check)" >&2; exit 1; }
mkdir -p "$home/site" "$home/comments"
cp "$server" "$home/comments-server.py"
# The Zulip and the channel, from [site.comments] of blueprint.toml, where
# the comment server looks for them (its --directory); nothing else of the
# site is needed, nginx sends it /api/comments/ alone.
python3 - "$root/blueprint.toml" "$home/site/comments-config.json" <<'PY'
import json, sys, tomllib
c = tomllib.load(open(sys.argv[1], "rb"))["site"]["comments"]
json.dump({"zulip": {"site": c["zulip"], "channel": c["channel"]}}, open(sys.argv[2], "w"))
PY
docker rm -f "$name" >/dev/null 2>&1 || true
docker run -d --name "$name" --restart unless-stopped \
  --user "$(id -u):$(id -g)" \
  --env-file "$envfile" \
  -p "127.0.0.1:$port:8701" \
  -v "$home:/relay" \
  python:3.13-slim \
  python3 /relay/comments-server.py --directory /relay/site --comments /relay/comments \
    --bind 0.0.0.0 --port 8701 >/dev/null
echo "$name: on 127.0.0.1:$port, $(docker inspect -f '{{.State.Status}}' "$name")"
