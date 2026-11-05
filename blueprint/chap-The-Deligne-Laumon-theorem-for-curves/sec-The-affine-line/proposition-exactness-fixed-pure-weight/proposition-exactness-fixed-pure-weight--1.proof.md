+++
kind = "proof"
of = "proposition-exactness-fixed-pure-weight--1"
order = 1295002
uses = ["corollary-open-direct-image-over-field", "proposition-weights-j-boundary-points", "lemma-local-duality-point-c-u", "proposition-weights-under-usual-operations", "lemma-filtrations-spectra"]
+++
The short exact sequence gives a distinguished triangle of Weil
complexes. Apply $Rj_*$, using
[corollary-open-direct-image-over-field], and take cohomology sheaves.
The natural identifications $\mathcal H^0(Rj_*F_i)\simeq j_*F_i$ and
the vanishing of negative cohomology give an exact sequence

$$
0\longrightarrow j_*F_1\longrightarrow j_*F
\longrightarrow j_*F_2\xrightarrow{\ \delta\ }R^1j_*F_1.
$$

On $U$, the map $j_*F\to j_*F_2$ restricts to the epimorphism
$F\to F_2$. Its composite with $\delta$ is zero, so $\delta$ vanishes
on the geometric stalks over closed points of $U_0$.

Let $s$ be a closed point of $C_0\setminus U_0$, with residue
cardinality $q_s>1$. By [proposition-weights-j-boundary-points], the
stalk $(j_*F_2)_{\bar s}$ has weights at most $w$.
The lisse dual $F_1^\vee$ is pure of weight $-w$, by
[proposition-weights-under-usual-operations], so the same boundary
estimate gives weights at most $-w$ on $(j_*F_1^\vee)_{\bar s}$.
The perfect pairing of [lemma-local-duality-point-c-u] identifies
$(R^1j_*F_1)_{\bar s}$ with the dual of this last stalk twisted by
$(-1)$; its weights are therefore at least $w+2$.

The map $\delta_{\bar s}$ commutes with Frobenius. If it were nonzero,
the spectra of its image as a quotient of the source and as a subspace
of the target would give an eigenvalue of weights both at most $w$
and at least $w+2$, contrary to $q_s>1$; see
[lemma-filtrations-spectra]. This is the weight-gap argument in
`FrobeniusModule.eq_zero_of_hasWeightsAtMost_of_dual`, applied to
stalks by `AlgebraicGeometry.WeilSheaf.stalkAtMap_eq_zero_of_dual`.

Thus $\delta$ vanishes on all geometric stalks over closed points.
`AlgebraicGeometry.WeilSheaf.eq_zero_of_forall_stalkAtMap` gives
$\delta=0$. Exactness of the cohomology sequence now gives the desired
short exact sequence, transported along the natural identifications
with ordinary direct images.
