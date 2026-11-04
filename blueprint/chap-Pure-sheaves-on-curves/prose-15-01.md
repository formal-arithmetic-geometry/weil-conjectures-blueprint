+++
id = "prose-15-01"
kind = "hidden"
title = "Pure sheaves on curves"
order = 1163
+++
How much does the trace function of a sheaf know about its Frobenius
eigenvalues? For a sheaf of rank one, pure of weight $w$, on a dense open
$U_0$ of the line, it knows the weight. Every trace over $\mathbf F_{q^n}$
has absolute value $q^{nw/2}$, so the sum $S_n$ of the $|t(x)|^2$ over
$U_0(\mathbf F_{q^n})$ is $q^{nw}\#U_0(\mathbf F_{q^n})$, about
$q^{n(w+1)}$. The growth rate $q^{w+1}$ of these sums therefore determines $w$. In higher rank a
trace is a sum of eigenvalues, and the eigenvalues can cancel. On
$\mathcal B_b\oplus\mathcal B_{-b}$ the trace at a point of degree $n$ is
$b^n+(-b)^n$, which is zero for every odd $n$. We show that the
cancellation cannot persist. For a nonzero pure lisse sheaf of weight $w$
on an affine curve, $\limsup_n\frac1n\log_qS_n=w+1$
(Theorem [theorem-weights-sums-squared-traces]).

The reason is positivity once more. Recall that a sheaf $\mathcal G$ is real
if the characteristic polynomials of Frobenius on its stalks have real
coefficients under $\iota$ (Definition [definition-real-sheaves]). For
such $\mathcal G$, pure of weight $w$, $|t_{\mathcal G}|^2$ is the trace function of
$\mathcal G\otimes\mathcal G$. Hence the generating series of the $S_n$ is the
logarithmic derivative of $L(\mathcal G\otimes\mathcal G,t)$. Positivity of
the Euler factors (Lemma [lemma-positivity-euler-factors]) shows that $L(\mathcal G\otimes\mathcal G,t)$ is not a
polynomial, and Lemma [lemma-degree-zero-top-cohomology] puts its poles
on $|t|=q^{-w-1}$. This forces the sums $S_n$ to reach the size $q^{n(w+1)}$
infinitely often. An arbitrary pure sheaf becomes real
after a twist to weight zero and the addition of its dual
(Proposition [proposition-twisting-weight-zero-adding-dual]).

This is what the Fourier argument of Section [chap-Delignes-theorem-for-curves]
needs. It starts from a pure lisse sheaf $M$ of weight $w$ on a dense open
$j:U_0\hookrightarrow\mathbf A^1$. It produces a pure lisse sheaf $M'$ on a
dense open $j'$ of the dual line. The argument knows the trace function of
$M'$ exactly, as the discrete Fourier transform of that of $M$, but it
cannot see the weight of $M'$ directly. Plancherel's formula multiplies the
sums $S_n$ by $q^n$, so the theorem shows that $M'$ has weight $w+1$.

The group we finally want to bound, $H^1_c(\mathbf A^1,j_*M)$, is the stalk of
$j'_*M'$ at the origin. The origin may be one of the points where $M'$ is
not lisse. There we need to know that $j'_*$ does not create larger weights
(Proposition [proposition-weights-j-boundary-points]).
