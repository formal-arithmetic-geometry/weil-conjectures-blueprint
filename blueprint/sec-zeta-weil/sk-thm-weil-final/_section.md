+++
id = "sk-thm-weil-final"
kind = "theorem"
title = "The Weil conjectures for smooth proper schemes"
order = 4364
uses = ["sk-cor-tf-point-counting", "sk-input-weights", "sk-lem-wweil-integer-rationality", "sk-cor-tf-functional-equation", "sk-cor-trace"]
lean = ["AlgebraicGeometry.Scheme.weil_conjectures", "AlgebraicGeometry.Scheme.exists_isWeilFactorization_of_smoothProper", "AlgebraicGeometry.Scheme.weil_integral_factors", "AlgebraicGeometry.Scheme.riemann_hypothesis", "AlgebraicGeometry.Scheme.weil_betti", "AlgebraicGeometry.Scheme.weil_functional_equation"]
tags = ["sketch"]
+++
For smooth, proper and geometrically connected $X_0$ of pure dimension $d$, put

$$
 H^i_\ell=H^i(X_{\mathrm{pro\acute et}},\Ql),\qquad
 P_{i,\ell}(T)=\det(1-T\operatorname{Frob}_{X,\Lambda_X}\mid H^i_\ell),\qquad
 b_{i,\ell}=\dim_{\Ql}H^i_\ell.
$$

Since $X_0$ is proper, $H^i_c=H^i$, and the determinant identity of
[sk-cor-tf-point-counting] for $\Lambda=\Ql$ reads

$$
 Z(X_0,T)=\prod_{i=0}^{2d}P_{i,\ell}(T)^{(-1)^{i+1}}.
$$

Since Frobenius is invertible, $\deg P_{i,\ell}=b_{i,\ell}$.
A *reciprocal root* of a polynomial $P$ is a scalar $\alpha$ such
that $1-\alpha T$ divides $P$. Thus the reciprocal roots of
$P_{i,\ell}$ are the Frobenius eigenvalues on $H^i_\ell$.

Let $X_0/\mathbf F_q$ be smooth, proper and geometrically connected of pure
dimension $d$, and let $P_{i,\ell}$ be as above.

1. There are unique polynomials $P_i(T)\in\mathbf Z[T]$ with $P_i(0)=1$
   whose images in $\mathbf Q_\ell[T]$ are $P_{i,\ell}(T)$ for every prime
   $\ell\nmid q$, and
   $Z(X_0,T)=\prod_{i=0}^{2d}P_i(T)^{(-1)^{i+1}}$.
1. The reciprocal roots of $P_i$ are algebraic integers, and each of them
   has absolute value $q^{i/2}$ under every complex embedding.
1. The degrees $b_i=\deg P_i=\dim_{\Ql}H^i_\ell$ do not depend on $\ell$,
   and $b_i=b_{2d-i}$. Moreover,
   $P_0=1-T$, $P_{2d}=1-q^dT$, and $b_0=b_{2d}=1$.
1. Put $\chi=\sum_i(-1)^ib_i$. Then $d\chi$ is even and there
   is $\varepsilon\in\{1,-1\}$ such that

$$
 Z\!\left(X_0,\frac1{q^dT}\right)
  =\varepsilon q^{d\chi/2}T^\chi Z(X_0,T)
  \quad\hbox{in }\mathbf Q(T).
$$
