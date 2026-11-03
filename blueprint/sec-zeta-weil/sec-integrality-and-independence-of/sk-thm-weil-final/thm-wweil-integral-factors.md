+++
id = "thm-wweil-integral-factors"
kind = "theorem"
title = "Integral factors and independence of the prime"
order = 4365
lean = ["AlgebraicGeometry.Scheme.integral_frobenius_factors", "AlgebraicGeometry.Scheme.integral_recovery", "AlgebraicGeometry.Scheme.realization_independence", "AlgebraicGeometry.Scheme.weil_integral_factors"]
uses = ["sk-cor-tf-point-counting", "sk-input-weights", "sk-lem-wweil-integer-rationality"]
+++
For smooth, proper and geometrically connected $X_0$ of pure dimension $d$, put

$$
 H^i_\ell=H^i(X_{\mathrm{pro\acute et}},\Ql),\qquad
 P_{i,\ell}(T)=\det(1-TF_i\mid H^i_\ell),\qquad
 b_{i,\ell}=\dim_{\Ql}H^i_\ell.
$$

These are the operators and factors of [sk-cor-tf-point-counting], whose
determinant identity reads

$$
 Z(X_0,T)=\prod_{i=0}^{2d}P_{i,\ell}(T)^{(-1)^{i+1}}.
$$

Since Frobenius is invertible, $\deg P_{i,\ell}=b_{i,\ell}$.
A *reciprocal root* of a polynomial $P$ is a scalar $\alpha$ such
that $1-\alpha T$ divides $P$; thus the reciprocal roots of
$P_{i,\ell}$ are the Frobenius eigenvalues on $H^i_\ell$.

There are unique polynomials $P_i(T)\in\mathbf Z[T]$, $P_i(0)=1$,
whose images in $\mathbf Q_\ell[T]$ are $P_{i,\ell}(T)$ for every
$\ell\nmid q$. Their reciprocal roots are algebraic integers, and
every complex embedding of each reciprocal root has absolute value
$q^{i/2}$. In particular the degrees $b_i=\deg P_i$ are independent
of $\ell$.

*Complement.* Consequently
$Z(X_0,T)=\prod_{i=0}^{2d}P_i(T)^{(-1)^{i+1}}$ in $\mathbf Q(T)$, a
factorization that does not depend on $\ell$; and, with $A/B$ the
normalized integral reduced fraction of the zeta function,
$A=\prod_{i\ \mathrm{odd}}P_i$ and $B=\prod_{i\ \mathrm{even}}P_i$.
