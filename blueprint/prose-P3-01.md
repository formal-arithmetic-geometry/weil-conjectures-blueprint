+++
id = "prose-P3-01"
kind = "hidden"
title = "Weights and the Riemann hypothesis"
order = 624
+++
Parts “The six operations” and “Duality and the trace formula” prove rationality and the
functional equation. What remains is Weil's axiom (d): for smooth proper
$X_0$ of pure dimension $d$, every eigenvalue $\alpha$ of Frobenius on
$H^i(X,\Ql)$ is an algebraic integer with $|\iota(\alpha)|=q^{i/2}$ for every
complex embedding $\iota$ (Corollary [sk-input-weights]). With it
come the Riemann hypothesis, integrality of the factors $P_i$ and their
independence of $\ell$ (Theorem [sk-thm-weil-final]).

For curves this goes back to Weil, who used the Jacobian and the
positivity of the Rosati involution. In higher dimension no such
structure is available, and Deligne found two different arguments. In
his first proof [deligne74] he fibred $X_0$ by a Lefschetz pencil
and bounded the eigenvalues on the cohomology of the fibres, using the
monodromy of the pencil and an argument of Rankin's from the theory of
modular forms. In his second paper [deligne80] he proved much
more, a theorem about all sheaves:

> if $K$ has weights at most $w$, then so does $Rf_!K$

(Theorem [sk-cor-dl-general-complex]). Here an eigenvalue $\alpha$ of
Frobenius at a closed point of degree $n$ has weight $w$ if
$|\iota(\alpha)|=q^{nw/2}$, and a complex has weights at most $w$ if each
$\mathcal H^i$ is mixed with weights at most $w+i$. Applied to the constant sheaf
on a smooth proper $X_0$, the theorem gives the upper bound
$|\iota(\alpha)|\le q^{i/2}$ on $H^i$, and Poincaré duality, which pairs
$\alpha$ with $q^d/\alpha$ on $H^{2d-i}$, gives the lower bound. We follow
Laumon's proof of Deligne's theorem [laumon87], which replaces the
Lefschetz pencil by the $\ell$-adic Fourier transform.

The theorem is stated for sheaves because the proof needs sheaves.
Locally, a variety is fibred in curves over a variety of smaller dimension, and the
direct image of the constant sheaf along such a fibration is not
constant. So the whole argument rests on the case of a curve, and it
proceeds in three steps.

1. On a curve, the pointwise eigenvalues of a sheaf are controlled by
   its determinants. A lisse sheaf of rank one has finite geometric
   monodromy, so after a twist it has finite order and is pure; this
   applies to the determinant of every lisse sheaf
   (Section [sec-rank-one-curves]).
   Sections [sec-determinant-weights] and [sec-purity-real-sheaves] then show, by
   Rankin's positivity argument applied to tensor powers, that every
   irreducible constituent of a real sheaf is pure of weight equal to its
   determinant weight (Theorem [sk-p-real-purity]).
2. The cohomology group $H^1_c(\mathbf A^1,j_*M)$ that we have to bound
   is the stalk of a sheaf on the dual line, the Fourier transform of $M$
   (Section [sec-fourier-transform]). Showing that a twist of this sheaf
   is a quotient of a real sheaf makes step 1 apply to it, and the
   Plancherel formula identifies its weight. Hence, for a pure lisse sheaf
   $F$ of weight $w$ on a curve, $H^r_c(C,F)$ has weights at most $w+r$
   (Theorem [sk-thm-wft-curve-middle-upper]).
3. The general case follows by fibring in curves
   (Section [sec-deligne-laumon-general]), after one proves that real sheaves on any
   base are mixed (Theorem [sk-i-dl-general-real]).

The Weil conjectures are then a short deduction (Section [sec-zeta-weil]).
What makes step 1 work is positivity. A real sheaf has real trace
functions, so the local Euler factors of its even tensor powers
$\mathcal G^{\otimes2m}$ are power series with nonnegative coefficients.
For such a product, no factor can have a pole closer to the origin than
the product itself (Lemma [sk-lem-wrp-positive-euler]). The trace formula
writes the $L$-function of $\mathcal G^{\otimes2m}$ as a ratio of
characteristic polynomials on $H^1_c$ and $H^2_c$, and on an affine
curve only $H^2_c$ contributes poles, at places controlled by the
determinant weights. An eigenvalue $\alpha$ of $\mathcal G$ at a closed
point $x$ thus satisfies $|\iota(\alpha)|^{2m}\le q_x^{m\beta+1}$ for all
$m$, where $\beta$ is the largest determinant weight and
$q_x=\#\kappa(x)$, and letting $m\to\infty$ gives
$|\iota(\alpha)|^2\le q_x^\beta$
(Proposition [sk-p-real-rankin]). This is Rankin's trick.
