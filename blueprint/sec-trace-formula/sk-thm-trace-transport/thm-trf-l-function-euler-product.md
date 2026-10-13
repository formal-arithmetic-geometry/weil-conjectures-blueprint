+++
id = "thm-trf-l-function-euler-product"
kind = "theorem"
title = "Euler-product form of the trace formula"
order = 2744
uses = ["def-trf-frobenius-operators", "def-weil-finite-field-fiber", "def-weil-pbc-rational-category", "def-weil-scheme-morphism-properties", "lem-sf-separably-closed-torsion-cd", "lem-trf-compactification-cohomology", "lem-trf-frobenius-degree-formula", "lem-trf-iterated-weil-cocycle", "lem-trf-local-frobenius-conjugacy", "lem-zl-euler-product-identity", "prop-trf-adic-coefficient-morphism-systems", "prop-trf-rational-frobenius-integral-model", "prop-trf-trace-formal-laws", "prop-weil-pbc-rational-transport", "thm-nagata-compactification", "thm-sc-finite-type-torsion-cd", "thm-trf-grothendieck-lefschetz-qbar", "thm-trf-trace-formula-e"]
+++
Fix the global finite-field datum
$p,a,q,k_0,k$, where $q=p^a$, let $X_0$ be a separated finite-type
$k_0$-scheme, and put $X=X_0\times_{k_0}k$. Let
$\Lambda\in\{E,\Qlb\}$ and let $K$ be a Weil complex with
coefficients in $\Lambda$ satisfying the hypotheses of
[thm-trf-trace-formula-e] (if $\Lambda=E$) or of
[thm-trf-grothendieck-lefschetz-qbar] (if $\Lambda=\Qlb$). These are
only the finite-level hypotheses (explicit etale-origin witnesses and
compactification admissibility for the reductions of a lattice of an
$E$-representative $K_E$). The Weil map $\varphi_E$ of $K_E$ is an
isomorphism of $D^b_c(X,E)$, but it need not be integral, or invertible
on any lattice after any rescaling. Write
$F=F^{\,1}_{c,K}$ for the global geometric Frobenius on
$H_c^i(X,K)$, and for a closed point $x\in|X_0|$ of degree
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
