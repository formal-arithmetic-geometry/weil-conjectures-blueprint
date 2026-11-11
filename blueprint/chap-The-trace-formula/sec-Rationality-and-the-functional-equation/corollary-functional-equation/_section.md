+++
id = "corollary-functional-equation"
kind = "corollary"
title = "Functional equation"
order = 1045
lean = ["AlgebraicGeometry.Scheme.functional_equation_frobeniusCharpolyRev"]
uses = ["lemma-stability"]
+++
Let $X_0/\mathbf F_q$ be smooth and proper of pure dimension $d$, and let
$\ell\nmid q$. Put $H^i=H^i(X_{\mathrm{pro}\acute{e}t},\mathbf Q_\ell)$, let $F_i$ be the Frobenius operator $F$ on $H^i$
(Section [sec-Weil-complexes]), and put

$$
b_i=\dim_{\mathbf Q_\ell}H^i,\qquad \chi=\sum_i(-1)^ib_i,\qquad
D=\prod_i\det(F_i)^{(-1)^i}.
$$

Then $b_{2d-i}=b_i$, $d\chi$ is even, $D^2=q^{d\chi}$, and in $\mathbf Q_\ell(T)$

$$
Z\!\left(X_0,\frac1{q^dT}\right)=(-1)^{\chi}D\,T^{\chi}\,Z(X_0,T)
=\varepsilon q^{d\chi/2}T^{\chi}Z(X_0,T),
\qquad \varepsilon=(-1)^\chi Dq^{-d\chi/2}\in\{1,-1\}.
$$
