+++
id = "theorem-trace-formula-euler-product--5"
kind = "theorem"
title = "The trace formula as an Euler product (5)"
name_showing = false
order = 1036005
aliases = ["bp-r317-5"]
lean = ["AlgebraicGeometry.WeilSheaf.lSeries_mul_localPolynomial_compactlySupportedCohomology_two"]
uses = ["theorem-trace-formula-euler-product--3", "definition-frobenius-operator"]
+++
Lean uses the following curve case of the rationality assertion.
Let $U_0$ be a smooth geometrically connected affine curve over
$\mathbf F_q$, let $\ell\nmid q$, let $\mathcal F$ be a lisse Weil
sheaf with $\overline{\mathbf Q}_\ell$-coefficients, and fix an embedding
$\iota:\overline{\mathbf Q}_\ell\hookrightarrow\mathbf C$.
Put $U=U_0\times_{\mathbf F_q}\overline{\mathbf F}_q$ and

$$
P_i(T)=\iota\!\left(\det(1-T\operatorname{Frob}_{U,\mathcal F}
\mid H_c^i(U_{\mathrm{pro}\acute{e}t},\mathcal F))\right).
$$

For the product of [theorem-trace-formula-euler-product--3],

$$
L_\iota(U_0,\mathcal F,T)P_2(T)=P_1(T).
$$

Since $P_1(0)=P_2(0)=1$, this expresses the series as the expansion at
zero of $P_1(T)/P_2(T)\in\mathbf C(T)$, with value $1$ at zero.
The general complex identity in
[theorem-trace-formula-euler-product--4] likewise has a finite product
of polynomials and their inverses on its right; Lean does not package
that general rationality consequence as a separate assertion here.
