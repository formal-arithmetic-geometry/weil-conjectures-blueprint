+++
kind = "proof"
of = "lemma-mixedness-open-closed--1"
order = 1339002
uses = ["proposition-extension-zero-restriction-closed-subscheme", "lemma-finite-quasi-finite-direct-images", "lemma-weights-exact-sequence"]
+++
Place $G$ in degree zero and write $K=G[0]$. By the definition of
weights for complexes, $K$ has weights at most $w$ if and only if
$G$ does. Pullback commutes with placing a sheaf in degree zero, so
$j^*K$ and $i^*K$ have weights at most $w$.

Extension by zero along $j$ preserves this bound, as does direct image
along the closed immersion $i$, the latter being a finite morphism
(Lemma [lemma-finite-quasi-finite-direct-images]). In Lean these steps are
`AlgebraicGeometry.WeilComplex.IsMixedOfWeightsAtMost.derivedLowerShriek_of_isOpenImmersion`
and
`AlgebraicGeometry.WeilComplex.IsMixedOfWeightsAtMost.derivedLowerStar_of_isClosedImmersion`.

The localization sequence of
[proposition-extension-zero-restriction-closed-subscheme] gives a
distinguished triangle with terms isomorphic to

$$
j_!j^*K\longrightarrow K\longrightarrow Ri_*i^*K
\longrightarrow (j_!j^*K)[1].
$$

This is the form supplied by
`AlgebraicGeometry.WeilComplex.exists_distTriang_openClosed`.
For each $b$, its cohomology sequence is exact at $\mathcal H^b(K)$.
The two outer cohomology sheaves have weights at most $w+b$, so
[lemma-weights-exact-sequence] gives the same bound for
$\mathcal H^b(K)$. Thus $K$ has weights at most $w$, and hence so does
$G$. These are the steps of
`AlgebraicGeometry.WeilComplex.IsMixedOfWeightsAtMost.of_distTriang`
and `AlgebraicGeometry.WeilComplex.IsMixedOfWeightsAtMost.of_openClosed`.

For mixedness without a specified bound, choose bounds $w_U$ and $w_Z$
for the two restrictions and apply the result with
$w=\max(w_U,w_Z)$. This is how the lemma is used in the Noetherian
induction proving that real constructible Weil sheaves are mixed.
