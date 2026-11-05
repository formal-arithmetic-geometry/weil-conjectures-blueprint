#!/usr/bin/env bash
# `blueprint serve` with the website's comments.  When the Zulip bot is at
# hand (~/.config/blueprint-comments/zulip.env, the file of
# deploy/comments-relay.sh), the local comment server relays to Zulip as the
# website's does, to the same channel; without it the comments stay in
# comments/.  Arguments go to `serve`:
#
#   scripts/serve.sh --port 8001 --facts lean-facts.json
#
# BLUEPRINT names another blueprint than `lake exe blueprint`, such as a
# binary built from chrisflav/blueprint at the pinned version.
set -euo pipefail
cd "$(dirname "$0")/.."
envfile=${BLUEPRINT_COMMENTS_ENV:-$HOME/.config/blueprint-comments/zulip.env}
if [ -r "$envfile" ]; then
  set -a; . "$envfile"; set +a
  echo "comments: on Zulip, as the bot of $envfile"
else
  echo "comments: kept in comments/ (no $envfile)"
fi
exec ${BLUEPRINT:-lake exe blueprint} serve "$@"
