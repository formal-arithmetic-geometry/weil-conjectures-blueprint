# The Weil conjectures: blueprint

The informal blueprint of
[formal-arithmetic-geometry/weil-conjectures](https://github.com/formal-arithmetic-geometry/weil-conjectures),
kept with the [blueprint](https://github.com/chrisflav/blueprint) tool. Each
object is one Markdown file with TOML front matter under `blueprint/`; the
Lean declarations it refers to live in the project, and their status is
derived from the project's oleans rather than written here.

The content was imported from the project's leanblueprint LaTeX sources
(`blueprint/src/version/` in the project) and is edited here from now on.

## Updated source notes

[Condensed Coefficients, Proper Base Change and Six Functors in Ordinary Derived Categories](DerivedCategoryAndSixFunctorsChoice_readable.tex)
(14 October 2026) is a newer standalone account of the coefficient and
derived-category foundations, proper base change, the construction of the
exceptional inverse image, and smooth purity with its trace and Frobenius
compatibility. Its proper base change chapter follows the blueprint's
injective acyclicity criterion, projective-line argument, and reduction
through finite morphisms, symmetric powers, and Chow's lemma, then connects
the torsion theorem to pro-étale and completed integral coefficients. It
uses condensed rings to define coefficients uniformly. The supplied LaTeX
source is kept alongside the node-based blueprint as a reference for this
part of the project.

## Working locally

```
lake exe cache get              # Mathlib oleans for the project dependency
lake build WeilConjectures      # the project itself
lake exe blueprint extract      # lean-facts.json from the built modules
lake exe blueprint check --lean # every check, including Lean facts
lake exe blueprint serve        # the site on localhost
```

The site at https://blueprint.fuxi.merten.dev is rebuilt by CI on every push.
