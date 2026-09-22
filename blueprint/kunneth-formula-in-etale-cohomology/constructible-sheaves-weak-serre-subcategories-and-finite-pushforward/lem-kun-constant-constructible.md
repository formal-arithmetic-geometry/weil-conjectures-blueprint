+++
id = "lem-kun-constant-constructible"
kind = "lemma"
title = "Constant sheaves are constructible"
order = 6118
lean = ["AlgebraicGeometry.Etale.isConstructible_constantSheaf"]
uses = ["def-kun-constant-sheaf"]
+++
Let $X$ be a quasi-compact and quasi-separated scheme. For every finite
abelian group (respectively finite $\Lambda$-module, $\Lambda$ Noetherian)
$M$, the constant sheaf $\underline{M}$ of [def-kun-constant-sheaf] on
$X_{\Et}$ is constructible.

## Proof

The single-piece partition $X$ makes $\underline{M}$ locally constant
with finite stalks (the stalk at every geometric point is $M$), which is
constructibility.

Unresolved dependencies: def:weil-pbc-constructible-complexes, def:weil-pbc-scheme-conventions
