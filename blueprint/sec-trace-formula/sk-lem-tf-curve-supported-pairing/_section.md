+++
id = "sk-lem-tf-curve-supported-pairing"
kind = "lemma"
title = "The supported restriction giving the Frobenius local term"
order = 2623
uses = ["sk-d-trace-class", "sk-d-weil", "sk-thm-sf-kunneth-verdier"]
tags = ["sketch"]
+++
Recall that $\omega_X=a_X^!A_s$ and $\mathbb D_XK=\cHom_A(K,\omega_X)$, and that $\Phi_X$ is
the $k$-linear Frobenius of [sk-d-weil].
Let $X_0$ be a smooth curve over $k_0$, let $X=X_0\times_{k_0}k$,
let $K\in\Dctf(X,A)$, and let $y$ be a
fixed point of $\Phi_X^m$. For a morphism $v:(\Phi_X^m)^*K\to K$ in
$\Dctf(X,A)$, let $a=(\Phi_X^m,\operatorname{id}_X)$ be the transposed
graph and $b=\Delta_X$ the diagonal, both closed immersions $X\to X\times X$. On the
strict localization $T$ of $X\times X$ at $(y,y)$ put

$$
 P=(\mathbb D_XK\boxtimes K)|_T.
$$

The morphism $v$ determines a supported class
$[v]\in H^0R\Gamma_a(T,P)$, and the local term
$\operatorname{LT}_y(v)$ of [sk-d-trace-class] is the
image of this class under the composite of morphisms in $D(A)$

$$
 R\Gamma_a(T,P)
 \xrightarrow{\rho_{a,b}}
 R\Gamma_y(b,b^*P)
 \xrightarrow{\mathrm{ev}_K}
 R\Gamma_y(X,\omega_X)
 \simeq R\Gamma(y,\omega_y)
 \xrightarrow{\int_y} A,
$$

where $\rho_{a,b}$ is the supported restriction map.

In this lemma the two product factors are interchanged relative to
the convention $c_m=(\operatorname{id}_X,\Phi_X^m)$ of [sk-d-weil].
