+++
id = "sk-thm-trace-formula"
kind = "corollary"
title = "Finite-ring Grothendieck–Lefschetz formula"
order = 3523
uses = ["sk-c-proper-global", "sk-d-lines", "sk-d-operator", "sk-d-relative-frob", "sk-d-six", "sk-d-trace", "sk-d-weil", "sk-d-weil-push", "sk-i-global-additivity", "sk-i-relative-frob", "sk-i-topology", "sk-p-frob", "sk-p-local", "sk-p-trace", "sk-thm-sf-package", "sk-def-sf-weil-complexes", "sk-thm-tf-coefficient-morphism-formula", "sk-lem-tf-frobenius-convention", "sk-lem-tf-fixed-points"]
tags = ["sketch"]
+++
Let $X_0/\mathbf F_q$ be separated and of finite type, and put
$X=X_0\times_{\mathbf F_q}k$.
For a Weil complex $(K,\phi)$ of [sk-def-sf-weil-complexes]
with coefficients in a finite commutative $\ell$-primary ring $A$,
let $\operatorname{Frob}_{X,K}$ be its geometric Frobenius on
$R\Gamma_c(X_{\mathrm{pro\acute et}},K)$, defined after
[sk-def-sf-weil-complexes], and let
$\operatorname{Frob}_{y,m}$ be its local operator on $K_{\bar y}$ at
$y\in X_0(\mathbf F_{q^m})$. Then for every $m\geq1$

$$
 \operatorname{tr}_A(\operatorname{Frob}_{X,K}^m\mid R\Gamma_c(X_{\mathrm{pro\acute et}},K))
 =\sum_{y\in X_0(\mathbf F_{q^m})}
       \operatorname{tr}_A(\operatorname{Frob}_{y,m}\mid K_{\bar y}).
$$

*Complement (invertible Frobenius correspondences).* Let
$\psi:\Phi_X^*K\xrightarrow{\sim}K$ be an invertible Frobenius correspondence
of [sk-d-weil] on $K\in\Dctf(X,A)$, for the scheme Frobenius $\Phi_X$. For every
$m\geq1$ the fixed points $\bar x:s\to X$ of $\Phi_X^m$ are the points of
$X_0(\mathbf F_{q^m})$, and

$$
 \operatorname{tr}_A(T_{c_m}(\psi_m)\mid R\Gamma_c(X_{\mathrm{pro\acute et}},K))
 =\sum_{x\in X_0(\mathbf F_{q^m})}
 \operatorname{tr}_A(\psi_{m,\bar x}\mid K_{\bar x}).
$$
