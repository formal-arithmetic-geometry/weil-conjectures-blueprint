+++
id = "prose-18-01"
kind = "hidden"
title = "The Deligne–Laumon theorem in general"
order = 1321
+++
At this point we know the Deligne–Laumon theorem on curves: a pure lisse sheaf of
weight $w$ on a curve has $H^r_c$ of weights at most $w+r$. For the Weil
conjectures we need the same bound for the cohomology of a variety of
any dimension. In this section we prove
Theorem [theorem-weights-rf-shriek], which says that for a separated
morphism of finite type $f:X_0\to Y_0$, the functor $Rf_!$ maps
$D_{\leq w}(X_0)$ into $D_{\leq w}(Y_0)$.

Take a surface fibred in curves over a curve, $f:X_0\to Y_0$. Here the Leray
spectral sequence $H^a_c(Y,R^bf_!\overline{\mathbf Q}_\ell)\Rightarrow H^{a+b}_c(X,\overline{\mathbf Q}_\ell)$
suggests applying the curve case twice, once on the fibres and once on
the base. On the fibres there is no difficulty: at a closed point $y$
the stalk of $R^bf_!\overline{\mathbf Q}_\ell$ is $H^b_c(X_{\bar y},\overline{\mathbf Q}_\ell)$, and the curve
case says that it has weights at most $b$. On the base, however, the
curve case applies only to pure sheaves. So we need a finite filtration
of $R^bf_!\overline{\mathbf Q}_\ell$ with pure quotients, that is, we need $R^bf_!\overline{\mathbf Q}_\ell$ to
be mixed in the sense of Definition [definition-weights], and bounds at
each point separately do not produce such a filtration. In his first
proof [deligne74] Deligne avoided the problem with a Lefschetz
pencil, where the Picard–Lefschetz formula describes the direct image in
the middle degree, but for an arbitrary fibration the sheaves on the base
are not explicit. Once a mixed filtration exists, on the other hand, the pointwise
bound also bounds the weights of its quotients
(Lemma [lemma-bounding-weights-mixed-sheaf]). The question is
therefore whether the direct images are mixed.

The answer comes once more from positivity
(Theorem [theorem-real-constructible-sheaves-are-mixed]):

> every constructible real Weil sheaf on a separated scheme of finite
> type over $k_0$ is mixed.

To see why, let $S$ be an irreducible constituent of a real lisse sheaf on a smooth
affine $X_0$. In order to compare the eigenvalues of $S$ at a fixed point $x_*$
with those at an arbitrary point $x$, we restrict to a curve through
both. On the curve each irreducible constituent is pure by
Theorem [theorem-purity-real-sheaves-curves], so if the restriction of
$S$ stays irreducible, its eigenvalues at $x$ have the weight
read off at $x_*$. In order to find curves on which $S$ stays irreducible, we
first show that irreducibility can be detected in one finite quotient of
the fundamental group
(Lemma [lemma-detecting-irreducibility-finite-quotient]), and then Bertini's
theorem gives a curve through the given points that stays connected
in the corresponding finite étale cover
(Lemma [lemma-curve-preserving-finite-cover] and
Corollary [corollary-curve-preserving-geometric-irreducibility]). For
constructible sheaves, finally, we stratify.

By Noether normalization over strata
(Lemma [lemma-relative-noether-normalization-over-stratification]),
an arbitrary $f$ is built from quasi-finite maps and projections of
relative affine lines. The essential case is a smooth family of affine
curves $h:U_0\to Y_0$ with a pure lisse sheaf $F$ on $U_0$. To apply the
theorem on real sheaves we need direct images that are real, and here
the curve case helps a second time. After a twist to weight zero and the
addition of the dual, $F$ becomes a real sheaf $G$, and the curve case on the
fibres makes the direct images of $G$ real, hence mixed. A twist of $F$ is a
direct summand of $G$, so the direct images of $F$ are mixed as well
(Theorem [theorem-pure-lisse-sheaves-over-relative]).
