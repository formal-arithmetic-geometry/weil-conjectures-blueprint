+++
id = "lemma-nagata-comparison-boundary-density"
kind = "lemma"
title = "Density over the prepared boundary"
order = 478
lean = ["AlgebraicGeometry.exists_prepared_keyDisjoint_twoOpenSide"]
uses = ["def-nagata-global-blowup-cover-comparison", "lemma-nagata-comparison-isiso-near-boundary", "prop-nagata-global-blowup-cover-independent"]
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
