+++
id = "prose-P3-01"
kind = "hidden"
title = "Weights and the Riemann hypothesis"
order = 1050
+++
After Parts I and II we can write
the number of points of a smooth proper variety as an alternating sum of
powers of Frobenius eigenvalues. But we know nothing about the size of these
eigenvalues, so the formula alone estimates nothing. For a curve of genus $g$
the formula reads $N_m=1+q^m-\sum_j\alpha_j^m$. It gives Weil's bound
$|N_m-1-q^m|\le2gq^{m/2}$ only once we know that $|\alpha_j|=q^{1/2}$. This Part
proves the analogous statement in every dimension, Weil's axiom (d)
(Corollary [corollary-purity-cohomology-smooth-proper-variety]): for smooth
proper $X_0$ of pure dimension $d$, every eigenvalue $\alpha$ of Frobenius on
$H^i(X,\mathbf Q_\ell)$ satisfies $|\iota(\alpha)|=q^{i/2}$ for every
complex embedding $\iota$.
Theorem [theorem-weil-conjectures-smooth-proper-schemes] deduces from it
the Riemann hypothesis, the integrality of the factors $P_i$ and their
independence of $\ell$.

For curves Weil proved this with the Jacobian. There the eigenvalues on $H^1$ are those of Frobenius on a Tate module, and the positivity of the Rosati
involution forces $|\alpha|=q^{1/2}$. In higher dimension, however, no such structure is available. Instead, Deligne's first proof [deligne74] fibred $X_0$ by a
Lefschetz pencil and used the monodromy of the pencil. In his second paper [deligne80], by contrast, he proved a theorem about all sheaves:

> if $K$ has weights at most $w$, then so does $Rf_!K$

(Theorem [theorem-weights-rf-shriek]; weights are defined in
Definition [definition-weights]). In particular, for the constant sheaf on a smooth proper $X_0$, the theorem gives the upper bound
$|\iota(\alpha)|\le q^{i/2}$ on $H^i$. Since Poincaré duality pairs $\alpha$ with $q^d/\alpha$ on $H^{2d-i}$, the upper bound on $H^{2d-i}$ gives the lower bound on $H^i$. Here we follow Laumon's proof [laumon87] of the Deligne–Laumon theorem, which replaces the Lefschetz pencil
by the $\ell$-adic Fourier transform.

The theorem has to be about sheaves because the proof fibres the variety,
locally, in curves over a variety of smaller dimension, and along such a fibration the direct image of the constant sheaf is no longer constant.
Everything therefore comes down to a pure lisse sheaf $F$ of weight $w$ on a
curve $C$. There we must show that $H^r_c(C,F)$ has weights at most $w+r$
(Theorem [theorem-weight-bound-curve]), and only $H^1_c$ is hard.

On a curve the one tool is the trace formula. It writes the $L$-function, a
product of local factors over the closed points, as the ratio of the
characteristic polynomials on $H^1_c$ and $H^2_c$. The difficulty is cancellation: a large local eigenvalue gives a local factor with a pole near the origin, but the other factors might cancel it. Rankin's trick from the theory of modular forms rules this out when the traces are real, because then
the even tensor powers have Euler factors with nonnegative coefficients. By
Lemma [lemma-positivity-convergence], no factor of such a product can have a
pole closer to the origin than the product itself. On an affine curve, moreover, only $H^2_c$ contributes poles, and their position is controlled by the
determinants. These determinants are pure because a lisse sheaf of rank one has
finite geometric monodromy (Section [sec-Sheaves-of-rank-one]). The outcome is the bound $|\iota(\alpha)|^2\le q_x^\beta$, where $\beta$ is the largest determinant weight
(Proposition [proposition-bound-largest-determinant-weight]). Applied to exterior powers, this bound shows that every irreducible constituent of a real sheaf is
pure (Theorem [theorem-purity-real-sheaves-curves],
Section [chap-Purity-of-real-sheaves]).

This bounds eigenvalues at points of a curve. What we must bound, however, is
a cohomology group $H^1_c(\mathbf A^1,j_*M)$, for a pure lisse sheaf $M$ on a
dense open $j:U_0\hookrightarrow\mathbf A^1$. The Fourier transform (Section [chap-The-Fourier-transform]) turns this group into the stalk of a sheaf on
the dual line, and a twist of that sheaf is a quotient of a real sheaf. The
Plancherel formula, together with two facts about pure sheaves on curves
(Section [chap-Pure-sheaves-on-curves]), shows that the sheaf has weight $w+1$.

In higher dimension the same positivity shows that real sheaves on any
base are mixed (Theorem [theorem-real-constructible-sheaves-are-mixed]).
This lets us apply the curve case along a fibration
(Section [chap-The-Deligne-Laumon-theorem-in-general]). The Weil conjectures are then a
short deduction (Section [chap-Proof-of-the-Weil-conjectures]).
