# The Weil conjectures: blueprint

The informal blueprint of
[formal-arithmetic-geometry/weil-conjectures](https://github.com/formal-arithmetic-geometry/weil-conjectures),
kept with the [blueprint](https://github.com/chrisflav/blueprint) tool. Each
object is one Markdown file with TOML front matter under `blueprint/`; the
Lean declarations it refers to live in the project, and their status is
derived from the project's oleans rather than written here.

The content was imported from the project's leanblueprint LaTeX sources
(`blueprint/src/version/` in the project) and is edited here from now on.

## Lecture notes

The blueprint follows the lecture notes *The Weil Conjectures: Six
operations, the trace formula and Deligne's theorem on weights*
(`Readable Lecture Notes.tex`). Its sections are the sections and
subsections of the notes, with the notes' sections at the top level; its sketch layer is the notes' theorems, lemmas,
propositions, corollaries, definitions, remarks and examples, one node each;
and the text between them is kept as nodes of kind `hidden`, which the
document shows in place and the graph leaves out. The Lean-backed detail
nodes sit below the sketch nodes. `TEX-ALIGNMENT.md` records how each
declaration of the notes was matched, and where the nodes the notes do not
state went.

## Working locally

```
lake exe cache get              # Mathlib oleans for the project dependency
lake build WeilConjectures      # the project itself
lake exe blueprint extract      # lean-facts.json from the built modules
lake exe blueprint check --lean # every check, including Lean facts
lake exe blueprint serve        # the site on localhost
```

The site at https://blueprint.fuxi.merten.dev is rebuilt by CI on every push.

Comments on the site go to the Zulip channel #Blueprint Comments
(`[site.comments]` in `blueprint.toml`). A comment is public, listed below
its page, or private, for the blueprint's authors alone. The page never talks
to Zulip: it posts to the comment server, which relays to Zulip as a bot whose
email and key only the server holds. On the website that is the relay on
fuxi (`deploy/comments-relay.sh`); locally it is the one `serve` starts. Give
it the bot in its environment; without it, `serve` keeps the comments locally
in `comments/`:

```
scripts/serve.sh --port 8001        # serve with the bot of ~/.config/blueprint-comments/zulip.env
```

`scripts/serve.sh` reads the bot from the file the relay on fuxi reads
(`BLUEPRINT_ZULIP_EMAIL=…` and `BLUEPRINT_ZULIP_KEY=…`, one per line); by hand,
export the two variables and run `lake exe blueprint serve`. A comment posted
locally goes to the same channel as the website's.
