+++
id = "lem-pc-closed-immersion-coherent-cohomology"
kind = "lemma"
title = "Coherent modules under a closed immersion"
order = 4327
lean = ["AlgebraicGeometry.cohomology_pushforward_closedImmersion"]
uses = ["def-pc-morphism-conventions", "lem-pc-affine-morphism-hi"]
+++
Let $i:X\hookrightarrow Y$ be a closed immersion
[def-pc-morphism-conventions] of locally Noetherian schemes, and let
$\mathcal F$ be a coherent module on $X$. Then $i_*\mathcal F$ is coherent,
and $H^q(Y,i_*\mathcal F)\cong H^q(X,\mathcal F)$ for every $q$. For an
invertible module $\mathcal L$ on $Y$, the natural map
$i_*\mathcal F\otimes\mathcal L\to i_*(\mathcal F\otimes i^*\mathcal L)$ is
an isomorphism.

## Proof

Over $V=\operatorname{Spec}(R)\subset Y$, write
$i^{-1}(V)=\operatorname{Spec}(R/I)$. The module of sections of
$\mathcal F$ there is finite over $R/I$, hence finite over $R$. It computes
$i_*\mathcal F|_V$ with the usual localization maps, so the coherence
criterion on a locally Noetherian scheme proves coherence. Closed
immersions are affine by this same description, and
[lem-pc-affine-morphism-hi] gives $R^qi_*\mathcal F=0$ for $q>0$. The
Leray spectral sequence therefore gives the asserted cohomology
identifications. Finally trivialize $\mathcal L$ on an open cover. On each
member the tensor map is the identity on $i_*\mathcal F$; these are the
restrictions of the natural map, and hence prove its isomorphism globally.

Unresolved dependencies: pqf-def-coherent, pqf-def-cohomology, def:sc-invertible-module, pqf-lem-coherent-ft-locnoeth, pqf-lem-leray
