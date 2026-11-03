+++
id = "sk-cor-tf-functional-equation"
kind = "corollary"
title = "Functional equation"
order = 621
lean = ["AlgebraicGeometry.Scheme.duality_reciprocity", "AlgebraicGeometry.Scheme.reciprocity", "AlgebraicGeometry.Scheme.even_finrank_cohomology_middle"]
uses = ["sk-cor-tf-point-counting", "sk-thm-derived-duality", "sk-thm-frobenius", "sk-thm-poincare-duality"]
tags = ["sketch"]
+++
Let $X_0/\mathbf F_q$ be smooth and proper of pure dimension $d$, and let
$\ell\nmid q$. Put $H^i=H^i(X_{\mathrm{pro}\acute{e}t},\Ql)$, let $F_i$ be the Frobenius operator $F$ on $H^i$
(Section [sec-frobenius]), and put

$$
b_i=\dim_{\Ql}H^i,\qquad \chi=\sum_i(-1)^ib_i,\qquad
D=\prod_i\det(F_i)^{(-1)^i}.
$$

Then $b_{2d-i}=b_i$, $d\chi$ is even, $D^2=q^{d\chi}$, and in $\Ql(T)$

$$
Z\!\left(X_0,\frac1{q^dT}\right)=(-1)^{\chi}D\,T^{\chi}\,Z(X_0,T)
=\varepsilon q^{d\chi/2}T^{\chi}Z(X_0,T),
\qquad \varepsilon=(-1)^\chi Dq^{-d\chi/2}\in\{1,-1\}.
$$
