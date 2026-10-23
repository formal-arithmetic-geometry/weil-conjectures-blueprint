+++
id = "lem-a1-subquotient-pure"
kind = "lemma"
title = "Irreducible lisse subquotients of a pure lisse sheaf are pure of the same weight"
lean = ["AlgebraicGeometry.WeilSheaf.IsPunctuallyPureOfWeight.of_subquotient"]
order = 4020
uses = ["sk-lem-coefficient-heart", "def-weil-pbc-scheme-conventions", "def-weil-punctual-weights", "def-weil-weil-sheaf-complex", "sk-def-sf-weil-complexes", "lem-a1-spectrum-exact-sequence"]
+++
Let $X_0$ be a separated
finite-type $k_0$-scheme and let $\mathcal G$ be a lisse
$\Qlb$-Weil sheaf on $X_0$ (a lisse $\overline{\mathbf Q}_{\ell,X}$-module on $X_{\mathrm{proét}}$,
[sk-lem-coefficient-heart], with a Weil structure, [sk-def-sf-weil-complexes]) which is punctually
$\iota$-pure of weight $w\in\mathbf R$ in the sense of
[def-weil-punctual-weights]. Then every irreducible lisse subquotient
$\mathcal S$ of $\mathcal G$ is punctually $\iota$-pure of weight
$w$.
