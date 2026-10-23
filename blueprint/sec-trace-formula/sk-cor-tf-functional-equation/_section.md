+++
id = "sk-cor-tf-functional-equation"
kind = "corollary"
title = "Functional equation"
order = 3558
uses = ["sk-cor-tf-point-counting", "sk-thm-derived-duality", "sk-thm-frobenius", "sk-thm-poincare-duality"]
tags = ["sketch"]
+++
Let $X_0/\mathbf F_q$ be smooth and proper of pure dimension $d$, and let
$\ell\nmid q$. Put $H^i=H^i(X_{\mathrm{pro\acute et}},\Ql)$, let $F_i$ be the
endomorphism of $H^i$ induced by the geometric Frobenius
$\operatorname{Frob}_{X,\Lambda_X}$ of [sk-cor-tf-point-counting] for
$\Lambda=\Ql$, and put

$$
 b_i=\dim_{\Ql}H^i,\qquad \chi=\sum_i(-1)^ib_i,\qquad
 D=\prod_i\det(F_i)^{(-1)^i}.
$$

Then $D^2=q^{d\chi}$, and in $\Ql(T)$ we have

$$
 Z\!\left(X_0,\frac1{q^dT}\right)=(-1)^{\chi}D\,T^{\chi}\,Z(X_0,T).
$$

*Complement.* The proof gives $b_{2d-i}=b_i$, the eigenvalues of $F_{2d-i}$
are the $q^d/\alpha$ for the eigenvalues $\alpha$ of $F_i$, with
multiplicities, and $\det F_i\cdot\det F_{2d-i}=q^{db_i}$. Moreover $d\chi$
is even, so that $D=\varepsilon q^{d\chi/2}$ with $\varepsilon=\pm1$: for odd
$d$ the middle pairing on $H^d$ is perfect and alternating, so $b_d$ is
even, and $\chi\equiv b_d\pmod 2$ because $b_{2d-i}=b_i$.
