+++
id = "prose-14-06"
kind = "hidden"
title = "Why the weight bound holds"
order = 4326
+++
For example, if $X_0$ is a smooth projective curve, the theorem applied
to the constant sheaf, which is pure of weight $0$, says that the
eigenvalues of Frobenius on $H^1(X,\overline{\mathbf Q}_\ell)$ have absolute value at most
$q^{1/2}$. Poincaré duality pairs an eigenvalue $\alpha$ with
$q/\alpha$, and hence gives equality.

Why should such a bound hold, and why is it easier to prove for all
sheaves than for the constant sheaf? The answer is that the statement
for sheaves can be proved one dimension at a time. If $X_0$ is fibred
over a base with curves as fibres, the compactly supported cohomology
of $X$ is computed in two steps, first along the fibres and then on the
base, so it suffices to prove the theorem for families of curves and
for sheaves on the base. The heart of the matter is therefore a single
curve: for a lisse sheaf $F$ on a smooth curve, pure of weight $w$, we
must show that $H^1_c$ has weights at most $w+1$
(Theorem [sk-cor-wft-curve-upper]). The cases $H^0_c$ and $H^2_c$ are
easy, so the whole difficulty lies in $H^1_c$.

To bound $H^1_c$ we use an idea of Rankin. Suppose first that the
local characteristic polynomials of a lisse sheaf $F$ have real
coefficients. Then the logarithm of the $L$-function of an even tensor
power $F^{\otimes2m}$ has nonnegative coefficients, and a power series
with nonnegative coefficients converges up to its first singularity on
the positive real axis. By the trace formula the only possible poles
of this $L$-function come from $H^2_c$, which is easy to control. This
bounds the local eigenvalues of $F^{\otimes2m}$, and letting
$m\to\infty$ we find that every irreducible constituent of $F$ is pure
(Theorem [sk-p-real-purity]). This
argument needs to know the weights of the simple constituents of
tensor powers, which is where the monodromy group of $F$ enters
(Sections “Rank-one sheaves on curves” and “Monodromy and determinant weights”). To pass from real
sheaves to the bound on $H^1_c$, we realize $H^1_c$ as a stalk of the
Fourier transform of $F$, a sheaf on the dual line whose weight can be
computed by comparing sums of squares of traces (the Plancherel
formula). This is done in Sections “The Fourier transform on the affine line”
and “Weights of the cohomology of curves”.

In Section “Weights under direct image with proper support” we pass from curves to arbitrary
morphisms. We show that direct images of real sheaves along families of curves are mixed,
bound their weights fibre by fibre by the case of a curve, and reduce
an arbitrary morphism to families of curves by Noether normalization.
Section “Cohomology of smooth proper schemes and the Weil conjectures” deduces the Weil conjectures.
