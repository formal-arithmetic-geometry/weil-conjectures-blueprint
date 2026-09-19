+++
id = "lemma-nagata-dense-affine-cover-exists"
kind = "lemma"
title = "Existence of a finite affine cover with dense total intersection"
order = 478
lean = ["AlgebraicGeometry.exists_isAffineOpen_iSup_eq_top_and_genericPoints_subset_iInter"]
uses = ["lemma-nagata-affine-neighbourhood-generic-points"]
+++
Let $X$ be quasi-compact and quasi-separated and assume that it has finitely
many irreducible components, with generic points
$\eta_1,\ldots,\eta_r$. There is a finite affine open cover
$(U_1,\ldots,U_n)$ whose total intersection is dense in $X$.

## Proof

For every $x\in X$, apply
[lemma-nagata-affine-neighbourhood-generic-points] to obtain an affine
open containing $x$ and every $\eta_i$. Quasi-compactness gives a finite
subcover. Its total intersection contains the generic point of every
irreducible component, and is therefore dense.
