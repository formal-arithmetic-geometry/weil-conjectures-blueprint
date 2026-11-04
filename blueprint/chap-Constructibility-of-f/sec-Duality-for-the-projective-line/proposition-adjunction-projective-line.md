+++
id = "proposition-adjunction-projective-line"
kind = "proposition"
title = "The adjunction for the projective line"
order = 547
lean = ["AlgebraicGeometry.Etale.exists_projectiveLineAdjunction", "AlgebraicGeometry.Etale.projectiveLineAdjunctionBaseChange_of_isNormalized"]
+++
Let $S$ be of finite type over $k$, and let $p:\mathbf P^1_S\to S$ be the
projection. The functors
$Rp_*:D_{\mathrm{class}}((\mathbf P^1_S)_{\mathrm{pro}\acute{e}t},\Lambda)\to
D_{\mathrm{class}}(S_{\mathrm{pro}\acute{e}t},\Lambda)$ and
$p^*(1)[2]:D_{\mathrm{class}}(S_{\mathrm{pro}\acute{e}t},\Lambda)\to
D_{\mathrm{class}}((\mathbf P^1_S)_{\mathrm{pro}\acute{e}t},\Lambda)$ form
an adjunction

$$
Rp_* \ \dashv\ p^*(1)[2],
\tag{6.7}
$$

with unit (6.5) and counit (6.6). For every morphism
$g:S'\to S$ with $S'$ of finite type over $k$, the unit and counit
are compatible with base change along $g$. They are
also compatible with change of finite coefficients.
