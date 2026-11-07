#!/usr/bin/env bash
# The key `lean-facts.json` is stored under by the Site workflow. The facts depend on exactly:
#
#   * the weil-conjectures revision pinned in lake-manifest.json (the oleans read);
#   * the extractor: lean-toolchain and the pinned tool's Blueprint/Extract.lean;
#   * the Lean names the blueprint asks for: every `lean` attribute of its objects
#     (the `@[blueprint]` tags come from the oleans, so the revision covers them).
#
# Two runs with the same key extract the same facts, so the second can reuse the first's.
# Prints `key=…` and the parts it was made of. Needs the tool built and no lean-facts.json in
# the root (`blueprint build` would read it, and the names must come from the sources alone).
set -euo pipefail
root=${1:-.}
cd "$root"
test ! -e lean-facts.json || { echo "facts-key: remove lean-facts.json first" >&2; exit 2; }

proj=$(jq -r '.packages[] | select(.url | test("formal-arithmetic-geometry/weil-conjectures(\\.git)?$")) | .rev' lake-manifest.json)
test -n "$proj"
extractor=$(cat lean-toolchain .lake/packages/blueprint/Blueprint/Extract.lean | sha256sum | cut -c1-16)

tmp=$(mktemp)
trap 'rm -f "$tmp"' EXIT
# `build` exits 1 when error-level checks fire but still writes the snapshot.
lake exe blueprint build --root . -o "$tmp" > /dev/null 2>&1 || true
test -s "$tmp"
count=$(jq -r '[.objects[] | .attrs.lean // empty | if type == "array" then .[] else . end] | unique | length' "$tmp")
names=$(jq -r '[.objects[] | .attrs.lean // empty | if type == "array" then .[] else . end] | unique | .[]' "$tmp" \
  | sha256sum | cut -c1-16)

key=$(printf 'proj=%s extractor=%s names=%s' "$proj" "$extractor" "$names" | sha256sum | cut -c1-24)
echo "project=$proj"
echo "extractor=$extractor"
echo "names=$names ($count)"
echo "key=$key"
