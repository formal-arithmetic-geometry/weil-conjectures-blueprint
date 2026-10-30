+++
id = "prose-20-06"
kind = "hidden"
title = "Reduction to the relative affine line"
order = 779
+++
It remains to reduce an arbitrary separated morphism of finite type to
relative affine curves. We do this by Noether normalization over
strata, and the strata are put back together by the following lemma.

This is the analogue of computing the cohomology of a variety by
fibring it. Over a field, Noether normalization makes an affine
variety of dimension $d$ finite over $\mathbf A^d$, and
$\mathbf A^d\to\operatorname{Spec}k$ is a composite of $d$ projections
of affine lines. For a morphism $f$ the same works over a dense open of
the target, and the complement is handled by induction on its
dimension (Lemma [sk-l-dl-general-normalization]). The weight bound
then has to be checked for two kinds of maps and shown to be stable
under the gluing operations. Quasi-finite maps were treated in
Lemma [sk-l-dl-general-quasifinite]. For the projection $\mathbf A^1_Y\to Y$
(Proposition [sk-prop-wgen-relative-line]), a sheaf on the relative line is,
over a dense open of the base, lisse off a closed subscheme finite over
the base, so it is glued from a relative affine curve and a
quasi-finite piece. The Leray spectral sequence gives stability under
composition (Theorem [sk-thm-dl-general-sheaf]), and the localization
sequences below give stability under partitions of the source and
of the target. These gluing steps only use that mixed sheaves of
weights at most $u$ are closed under subquotients and extensions.
