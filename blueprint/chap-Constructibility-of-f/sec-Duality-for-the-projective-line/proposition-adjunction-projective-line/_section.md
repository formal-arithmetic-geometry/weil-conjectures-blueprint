+++
id = "proposition-adjunction-projective-line"
kind = "proposition"
title = "The adjunction for the projective line"
order = 553
lean = ["AlgebraicGeometry.Etale.exists_projectiveLineAdjunction", "AlgebraicGeometry.Etale.projectiveLineAdjunctionBaseChange_of_isNormalized"]
uses = ["definition-tate-twists", "lemma-cohomology-projective-line-trace", "lemma-cycle-class-cartier-divisor"]
+++
Let $S$ be of finite type over $k$, and let $p:\mathbf P^1_S\to S$ be the
projection. The functors
$Rp_*:D((\mathbf P^1_S)_{\acute{e}t},A)\to
D(S_{\acute{e}t},A)$ and
$p^*(1)[2]:D(S_{\acute{e}t},A)\to
D((\mathbf P^1_S)_{\acute{e}t},A)$ form
an adjunction

$$
Rp_* \ \dashv\ p^*(1)[2],
\tag{6.7}
$$

with unit (6.5) and counit (6.6). For every morphism
$g:S'\to S$ with $S'$ of finite type over $k$, the unit and counit
are compatible with base change along $g$. They are
also compatible with change of finite coefficients.
