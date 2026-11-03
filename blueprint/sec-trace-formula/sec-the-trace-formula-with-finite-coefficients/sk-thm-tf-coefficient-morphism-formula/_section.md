+++
id = "sk-thm-tf-coefficient-morphism-formula"
kind = "theorem"
title = "Trace formula for a Frobenius correspondence"
order = 600
uses = ["sk-d-weil", "sk-lem-tf-compact-trace", "sk-i-relative-frob", "sk-p-proper", "sk-p-frob", "sk-thm-sf-ctf-stability", "sk-i-global-additivity"]
tags = ["sketch"]
+++
Let $X_0/\mathbf F_q$ be separated and of finite type, put
$X=X_0\times_{\mathbf F_q}k$, let $A$ be any finite commutative
$\ell$-primary ring and $K\in D^b_{\mathrm{ctf}}(X,A)$, and let
$\psi:\Phi_X^*K\to K$ be any Frobenius correspondence on $K$. For every
$m\geq1$, in $A$,

$$
\operatorname{tr}_A(T_{c_m}(\psi_m)\mid R\Gamma_c(X_{\mathrm{pro}\acute{e}t},K))
=\sum_{x\in X_0(\mathbf F_{q^m})}
\operatorname{tr}_A(\psi_{m,\bar x}\mid K_{\bar x}).
$$
