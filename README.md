# The Weil conjectures: blueprint

The informal blueprint of
[formal-arithmetic-geometry/weil-conjectures](https://github.com/formal-arithmetic-geometry/weil-conjectures),
kept with the [blueprint](https://github.com/chrisflav/blueprint) tool. Each
object is one Markdown file with TOML front matter under `blueprint/`; the
Lean declarations it refers to live in the project, and their status is
derived from the project's oleans rather than written here.

The content was imported from the project's leanblueprint LaTeX sources
(`blueprint/src/version/` in the project) and is edited here from now on.

## Working locally

```
lake exe cache get              # Mathlib oleans for the project dependency
lake build WeilConjectures      # the project itself
lake exe blueprint extract      # lean-facts.json from the built modules
lake exe blueprint check --lean # every check, including Lean facts
lake exe blueprint serve        # the site on localhost
```

The site at https://blueprint.fuxi.merten.dev is rebuilt by CI on every push.

### The blueprint tool

The tool is vendored in `blueprint-tool/`, a copy of
[chrisflav/blueprint](https://github.com/chrisflav/blueprint) at `12dff24`
with local fixes, and Lake builds it from there (`path` in `lakefile.toml`),
locally and in CI. Edit it in place; `lake exe blueprint` rebuilds it. Its
own tests are `blueprint-tool/test.sh`.

Local changes so far:

* `extract`: the dependency walk stays inside the project, so a blueprint
  object mapped to a Mathlib declaration no longer produces false
  `actual-not-declared` warnings (chrisflav/blueprint#1). The project is the
  roots of `[lean] modules`, extendable with `[lean] descend`.
