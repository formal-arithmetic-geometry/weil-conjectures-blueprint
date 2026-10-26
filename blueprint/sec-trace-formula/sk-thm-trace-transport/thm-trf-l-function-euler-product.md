+++
id = "thm-trf-l-function-euler-product"
kind = "theorem"
title = "Euler-product form of the trace formula"
lean = ["AlgebraicGeometry.WeilComplex.coeff_prod_inv_alternatingCharpolyRevProd_stalk"]
order = 3535
uses = ["def-weil-finite-field-fiber", "def-weil-scheme-morphism-properties", "def-weil-weil-sheaf-complex", "det-thm-tf-uniform-formula-weil", "sk-thm-tf-uniform-formula", "sk-prop-logdet", "sk-lem-finite", "lem-trf-frobenius-degree-formula", "lem-trf-iterated-weil-cocycle", "lem-trf-local-frobenius-conjugacy", "lem-zl-euler-product-identity", "prop-trf-trace-formal-laws", "sk-thm-sfb-qlbar-two-colimit"]
+++
Fix the global finite-field datum
$p,a,q,k_0,k$, where $q=p^a$, let $X_0$ be a separated finite-type
$k_0$-scheme, and put $X=X_0\times_{k_0}k$. Let
$\Lambda\in\{E,\Qlb\}$, with $E/\Ql$ finite (so $\Lambda=\Ql$ is
included), and let $(K,\theta)$ be a Weil complex with coefficients in
$\Lambda$ in the sense of [def-weil-weil-sheaf-complex]: $K\in\Dbc(X,\Lambda)$
and $\theta:g_X^*K\xrightarrow{\sim}K$. No lattice, integrality or
finite-level hypothesis is imposed. Write
$F$ for the global geometric Frobenius on
$H_c^i(X,K)$ of [det-thm-tf-uniform-formula-weil], and for a closed point $x\in|X_0|$ of degree
$e_x=[\kappa(x):\Fq]$ write $F_x$ for the one-circuit local Frobenius
on the stalk $K_{\bar x}$ (well defined up to conjugation). Put

$$
\det\bigl(1-T^{e_x}F_x\mid K_{\bar x}\bigr)
:=\prod_{j\in\mathbf Z}
\det\bigl(1-T^{e_x}F_x\mid H^j(K_{\bar x})\bigr)^{(-1)^j},
\qquad
L(X_0,K,T)=\prod_{x\in|X_0|}
\det\bigl(1-T^{e_x}F_x\mid K_{\bar x}\bigr)^{-1}.
$$

Then:

1. The product defining $L(X_0,K,T)$ is locally finite for the
$T$-adic topology, and $L(X_0,K,T)\in1+T\Lambda[[T]]$.
1. As formal power series in $\Lambda[[T]]$,
$$
L(X_0,K,T)=\prod_{i\in\mathbf Z}
\det\bigl(1-TF\mid H_c^i(X,K)\bigr)^{(-1)^{i+1}},
$$
the product being finite.
1. If $\dim X_0\leq1$ and $K$ is a sheaf placed in degree zero, then
$H_c^i(X,K)=0$ for $i\notin\{0,1,2\}$, so the product in (2) runs
over $0\leq i\leq2$:
$$
L(X_0,K,T)=
\frac{\det(1-TF\mid H_c^1(X,K))}
{\det(1-TF\mid H_c^0(X,K))\,\det(1-TF\mid H_c^2(X,K))}.
$$
1. For every field embedding $\iota:\Qlb\to\mathbf C$, applying
$\iota$ coefficientwise carries the identity (2) (for $\Lambda=\Qlb$)
to the corresponding identity in $\mathbf C[[T]]$.
