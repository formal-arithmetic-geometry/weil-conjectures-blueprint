+++
id = "thm-weil-final-rationality"
kind = "theorem"
title = "Weil conjectures I: rationality and Euler product"
order = 3266
lean = ["AlgebraicGeometry.Scheme.zetaSeries_rational"]
uses = ["def-weil-finite-field-fiber", "def-weil-geometric-hypotheses", "def-weil-point-counts-zeta", "prop-euler-product", "prop-every-iterate-trace", "prop-rational-descent", "prop-trace-determinant", "prop-weil-rationality-criterion"]
+++
Fix a finite field
$k_0=\mathbf F_q$ of characteristic $p$, with algebraic closure
$k=\overline{\mathbf F}_q$.
Let $X_0$ be a $k_0$-scheme of finite type (quasi-compact and locally of
finite type over $k_0$).
For an indeterminate $T$, use the
point-count zeta series

$$
Z(X_0,T)=\exp\left(\sum_{n\geq1}
\#X_0(\mathbf F_{q^n})\frac{T^n}{n}\right).
$$

Here $|X_0|$ is the set of closed points and
$\deg(x)=[\kappa(x):k_0]$. Then there are polynomials
$A,B\in\mathbf Z[T]$ with $B(0)=1$ and

$$
B(T)\,Z(X_0,T)=A(T)\quad\text{in }\mathbf Q[[T]],
$$

so that in particular $Z(X_0,T)\in1+T\mathbf Z[[T]]\cap\mathbf Q(T)$; and

$$
Z(X_0,T)=\prod_{x\in|X_0|}(1-T^{\deg(x)})^{-1}.
$$
