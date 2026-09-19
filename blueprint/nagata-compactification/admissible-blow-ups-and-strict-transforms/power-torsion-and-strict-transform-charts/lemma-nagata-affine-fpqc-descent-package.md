+++
id = "lemma-nagata-affine-fpqc-descent-package"
kind = "lemma"
title = "Affine morphisms descend fpqc-locally"
order = 370
+++
**Status.** Bypassed by the formalized route: the Raynaud–Gruson flattening
chain is not formalized. Elimination of indeterminacy is obtained instead
by the route of the chapter *Elimination of indeterminacy after Deligne
and Conrad*, whose output is
`AlgebraicGeometry.exists_admissibleBlowup_isOpenImmersion_strictTransformMap`.

Let $p\colon X'\to X$ be faithfully flat and quasi-compact. If
$f\colon Y\to X$ is quasi-compact and $Y\times_XX'\to X'$ is affine, then
$f$ is affine.

## Proof

Work over an affine $X_0=\operatorname{Spec}(A)$ and choose a finite affine
cover $X'_0=\bigcup_i\operatorname{Spec}(A_i)$. Write the affine pullbacks
as $\operatorname{Spec}(B_i)$. On overlaps the $B_i$ carry the canonical
descent identifications. Set
$B=\ker(\prod_iB_i\rightrightarrows\prod_{i,j}B_i\otimes_AA_{ij})$.
Faithful flatness makes tensoring this equalizer with each $A_i$ exact and
identifies $B\otimes_AA_i$ with $B_i$. Hence $\operatorname{Spec}(B)$
pulls back to the given affine cover and glues to $Y\times_XX'_0$; the
comparison with $Y$ is an isomorphism after the faithfully flat cover and
therefore an isomorphism. Thus $Y$ is affine over $X_0$.
