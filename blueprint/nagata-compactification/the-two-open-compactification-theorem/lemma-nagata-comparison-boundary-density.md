+++
id = "lemma-nagata-comparison-boundary-density"
kind = "lemma"
title = "Density over the prepared boundary"
order = 544
lean = ["AlgebraicGeometry.exists_prepared_keyDisjoint_twoOpenSide"]
uses = ["def-nagata-admissible-blowup", "def-nagata-compactifiable", "def-nagata-compactification", "def-nagata-global-blowup", "def-nagata-global-blowup-cover-comparison", "def-nagata-global-blowup-map", "def-nagata-isomorphism-near-closure", "def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-closure", "def-nagata-scheme-theoretic-image", "def-nagata-strict-transform", "def-nagata-two-open-boundary-loci", "def-nagata-two-open-comparison-space", "def-nagata-two-open-graph-extensions", "def-nagata-two-open-improved-comparison", "def-nagata-two-open-prepared-boundaries", "lemma-nagata-admissible-blowup-over-open", "lemma-nagata-comparison-isiso-near-boundary", "lemma-nagata-comparison-projections-proper", "lemma-nagata-diagonal-base-change", "lemma-nagata-immersion-open-in-scheme-image", "lemma-nagata-isomorphism-near-closure", "lemma-nagata-open-immersion-qc-over-separated-target", "lemma-nagata-prepared-boundaries", "lemma-nagata-proper-to-separated-target", "lemma-nagata-scheme-image-ideal-qc", "lemma-nagata-scheme-image-of-closed-immersion", "lemma-nagata-strict-transform-closure-characterization", "lemma-nagata-two-open-graph-extensions", "prop-nagata-global-blowup-cover-independent"]
+++
The subset $Z_{12,2}$ is dense in
$p_1^{-1}(\overline Z_{1,2})$.

## Proof

Choose an open neighbourhood $N\subseteq X_1$ of
$\overline Z_{1,2}$ over which $p_1$ is an isomorphism, as supplied by
[lemma-nagata-comparison-isiso-near-boundary]. Then
$p_1^{-1}(\overline Z_{1,2})$ lies in $p_1^{-1}(N)$, and the restriction

$$
p_1^{-1}(\overline Z_{1,2})\longrightarrow\overline Z_{1,2}
$$

is an isomorphism. By the definition of $Z_{12,2}$, its inverse image under
this isomorphism is $Z_{1,2}$. Since $Z_{1,2}$ is dense in its closure
$\overline Z_{1,2}$, the inverse image $Z_{12,2}$ is dense in
$p_1^{-1}(\overline Z_{1,2})$.
