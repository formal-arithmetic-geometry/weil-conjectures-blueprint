+++
id = "prose-15-01"
kind = "hidden"
title = "Pure sheaves on curves"
order = 1172
+++
How much does the [trace function](@definition-trace-function) of a sheaf know about its Frobenius
eigenvalues? For a sheaf of rank one, [pure](@definition-weights) of weight $w$, on a dense open
$U_0$ of the line, it knows the weight. Indeed, every trace over $\mathbf F_{q^n}$
has absolute value $q^{nw/2}$, so the sum $S_n$ of the $|\href{@definition-trace-function}{t(x)}|^2$ over
$U_0(\mathbf F_{q^n})$ is $q^{nw}\#U_0(\mathbf F_{q^n})$, about
$q^{n(w+1)}$, and the growth rate $q^{w+1}$ of these sums therefore determines $w$. In higher rank, however, a
trace is a sum of eigenvalues, and the eigenvalues can cancel. For example, on
$\href{@proposition-weights-under-usual-operations}{\mathcal B_b}\oplus\href{@proposition-weights-under-usual-operations}{\mathcal B_{-b}}$ the trace at a point of degree $n$ is
$b^n+(-b)^n$, which is zero for every odd $n$. We show that the
cancellation cannot persist: for a nonzero [pure](@definition-weights) [lisse](@definition-lisse-sheaves) sheaf of weight $w$
on an affine curve, $\limsup_n\frac1n\log_qS_n=w+1$
(Theorem [theorem-weights-sums-squared-traces]).

The reason is positivity once more. Recall that a sheaf $\mathcal G$ is real
if the characteristic polynomials of Frobenius on its stalks have real
coefficients under $\iota$ (Definition [definition-real-sheaves]). For
such $\mathcal G$, [pure](@definition-weights) of weight $w$, $|\href{@definition-trace-function}{t_{\mathcal G}}|^2$ is the [trace function](@definition-trace-function) of
$\mathcal G\otimes\mathcal G$, and hence the generating series of the $S_n$ is the
logarithmic derivative of [$L(\mathcal G\otimes\mathcal G,t)$](@theorem-trace-formula-euler-product). Positivity of
the Euler factors (Lemma [lemma-positivity-euler-factors]) shows that [$L(\mathcal G\otimes\mathcal G,t)$](@theorem-trace-formula-euler-product) is not a
polynomial, and Lemma [lemma-degree-zero-top-cohomology] puts its poles
on $|t|=q^{-w-1}$. Together these force the sums $S_n$ to reach the size $q^{n(w+1)}$
infinitely often. The restriction to [real](@definition-real-sheaves) sheaves costs nothing, since an arbitrary [pure](@definition-weights) sheaf becomes [real](@definition-real-sheaves)
after a twist to weight zero and the addition of its dual
(Proposition [proposition-twisting-weight-zero-adding-dual]).

This is what the Fourier argument of Chapter [chap-The-Deligne-Laumon-theorem-for-curves]
needs. That argument starts from a [pure](@definition-weights) [lisse](@definition-lisse-sheaves) sheaf $M$ of weight $w$ on a dense open
$j:U_0\hookrightarrow\mathbf A^1$ and produces a [pure](@definition-weights) [lisse](@definition-lisse-sheaves) sheaf $M'$ on a
dense open $j'$ of the dual line. It knows the [trace function](@definition-trace-function) of
$M'$ exactly, as the discrete Fourier transform of that of $M$, but it
cannot see the weight of $M'$ directly. Since [Plancherel's formula](@corollary-plancherel) multiplies the
sums $S_n$ by $q^n$, the theorem shows that $M'$ has weight $w+1$.

The group we finally want to bound, $H^1_c(\mathbf A^1,j_*M)$, is the stalk of
$j'_*M'$ at the origin. But the origin may be one of the points where $M'$ is
not [lisse](@definition-lisse-sheaves), and there we need to know that $j'_*$ does not create larger weights
(Proposition [proposition-weights-j-boundary-points]).
