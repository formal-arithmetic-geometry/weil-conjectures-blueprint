+++
id = "prose-18-09"
kind = "hidden"
title = "Proof of the Deligne–Laumon theorem (1)"
order = 1348
+++
An arbitrary $f$ reduces to relative affine curves and quasi-finite
maps. Over a field, Noether normalization makes an affine
variety of dimension $d$ finite over $\mathbf A^d$, and
$\mathbf A^d\to\operatorname{Spec}k$ is a composite of $d$ projections
of affine lines. For a separated morphism $f$ of finite type the same
works over a dense open of the target, and we treat the complement by
induction on its dimension
(Lemma [lemma-relative-noether-normalization-over-stratification]).
So we must check the weight bound for two kinds of maps and show
that it survives the gluing.

Quasi-finite maps were treated in
Lemma [lemma-finite-quasi-finite-direct-images]. For the
projection $\mathbf A^1_Y\to Y$
(Proposition [proposition-relative-affine-line]), consider a sheaf
on the relative line. Over a dense open of the base it is lisse off a
closed subscheme finite over the base. It is therefore glued from a
relative affine curve and a quasi-finite piece. The bound is stable
under composition by the Leray spectral sequence
(Theorem [theorem-direct-image-mixed-sheaf]). It is stable under
partitions of the source and of the target by the localization
sequences below. These gluing steps use only that mixed sheaves of
weights at most $u$ are closed under subquotients and extensions.
