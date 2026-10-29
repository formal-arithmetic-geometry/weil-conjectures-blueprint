+++
id = "sk-thm-tf-coefficient-morphism-formula"
kind = "theorem"
title = "Trace formula for a Frobenius correspondence"
order = 3826
uses = ["sk-d-weil", "sk-lem-tf-compact-trace", "sk-i-relative-frob", "sk-p-proper", "sk-p-frob", "sk-thm-sf-ctf-stability", "sk-i-global-additivity"]
tags = ["sketch"]
+++
The iterates $\psi_m$, the global operators $T_{c_m}(\psi_m)$ and the local
operators $\psi_{m,\bar x}$ of a Frobenius correspondence are those of
[sk-d-weil].

Let $X_0/\mathbf F_q$ be separated and of finite type, put
$X=X_0\times_{\mathbf F_q}k$, let $A$ be any finite commutative
$\ell$-primary ring and $K\in\Dctf(X,A)$, and let
$\psi:\Phi_X^*K\to K$ be any Frobenius correspondence on $K$, that
is, any morphism in $\Dctf(X,A)$. For every
$m\geq1$, in $A$,

$$
 \boxed{\quad
 \operatorname{tr}_A(T_{c_m}(\psi_m)\mid R\Gamma_c(X_{\mathrm{pro\acute et}},K))
 =\sum_{x\in X_0(\mathbf F_{q^m})}
 \operatorname{tr}_A(\psi_{m,\bar x}\mid K_{\bar x}).
 \quad}
$$

Both sides are traces of endomorphisms of perfect complexes.
