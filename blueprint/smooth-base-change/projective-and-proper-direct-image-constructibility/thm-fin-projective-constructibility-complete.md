+++
id = "thm-fin-projective-constructibility-complete"
kind = "theorem"
title = "Projective direct-image constructibility"
order = 5206
lean = ["AlgebraicGeometry.Etale.hasConstructibleDirectImage_of_projective"]
uses = ["def-finrepair-property-c", "thm-fin-projective-line-constructible", "lem-finrepair-projective-from-line"]
+++
Every projective morphism between schemes of finite type over $k$ satisfies
$\mathcal C(f)$ of [def-finrepair-property-c].

## Proof

[thm-fin-projective-line-constructible] proves projective-line
constructibility over every finite-type base. Apply
[lem-finrepair-projective-from-line].

Unresolved dependencies: def:pc-projective-morphism
