+++
id = "lemma-nagata-comparison-isiso-near-boundary"
kind = "lemma"
title = "Properties of the improved first comparison projection"
order = 543
lean = ["AlgebraicGeometry.exists_prepared_keyDisjoint_twoOpenSide"]
uses = ["def-nagata-admissible-blowup", "def-nagata-compactifiable", "def-nagata-compactification", "def-nagata-global-blowup", "def-nagata-global-blowup-cover-comparison", "def-nagata-global-blowup-map", "def-nagata-isomorphism-near-closure", "def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-closure", "def-nagata-scheme-theoretic-image", "def-nagata-strict-transform", "def-nagata-two-open-boundary-loci", "def-nagata-two-open-comparison-space", "def-nagata-two-open-graph-extensions", "def-nagata-two-open-improved-comparison", "def-nagata-two-open-prepared-boundaries", "lemma-nagata-admissible-blowup-over-open", "lemma-nagata-boundary-disjoint-persists", "lemma-nagata-boundary-loci", "lemma-nagata-comparison-projections-proper", "lemma-nagata-comparison-restrict-proper-open", "lemma-nagata-diagonal-base-change", "lemma-nagata-immersion-open-in-scheme-image", "lemma-nagata-isomorphism-near-closure", "lemma-nagata-maximal-isomorphism-open", "lemma-nagata-open-immersion-qc-over-separated-target", "lemma-nagata-prepared-boundaries", "lemma-nagata-proper-to-separated-target", "lemma-nagata-scheme-image-ideal-qc", "lemma-nagata-scheme-image-of-closed-immersion", "lemma-nagata-scheme-image-strict-transform", "lemma-nagata-strict-transform-closure-characterization", "lemma-nagata-two-open-graph-extensions", "prop-nagata-global-blowup-cover-independent"]
+++
The constructed map $X_1^{\mathrm{cmp}}\to X_1^{\mathrm{old}}$ is
$V_1$-admissible, the transported $p_1$ is an isomorphism over an open
neighbourhood of $\overline Z_{1,2}$, and all previously established
boundary-disjointness relations still hold.

## Proof

By [lemma-nagata-comparison-restrict-proper-open], the restriction of
$p_1$ over $V_1$ is the base change
$V_1\times_UV_2\to V_1$ of $\psi_2$. The maximal isomorphism open $N_2$
contains $Z_2$ by [lemma-nagata-boundary-loci] and
[lemma-nagata-maximal-isomorphism-open]; hence $p_1$ is an
isomorphism over $\psi_1^{-1}(N_2)$, an open containing $Z_{1,2}$.

The subset $Z_{1,2}$ is closed in $V_1$, and $p_1$ is proper by
[lemma-nagata-comparison-projections-proper]. Therefore the property
of $\mathsf{IsoBl}_{V_1,Z_{1,2}}(p_1)$ gives the asserted isomorphism near
the closure. The new comparison scheme is the strict transform by
[lemma-nagata-scheme-image-strict-transform]. Finally
[lemma-nagata-boundary-disjoint-persists] preserves every earlier
disjointness relation under this further $V_1$-admissible blow-up.
