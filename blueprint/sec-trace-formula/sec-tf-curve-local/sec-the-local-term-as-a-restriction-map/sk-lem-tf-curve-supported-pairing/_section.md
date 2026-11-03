+++
id = "sk-lem-tf-curve-supported-pairing"
kind = "lemma"
title = "The local term as a restriction map"
order = 580
uses = ["sk-d-trace-class", "sk-d-weil", "sk-thm-sf-kunneth-verdier"]
tags = ["sketch"]
+++
Let $X_0$ be a smooth curve over $k_0$, let $X=X_0\times_{k_0}k$,
let $K\in D^b_{\mathrm{ctf}}(X,A)$, and let $y$ be a
fixed point of $\Phi_X^m$. Let $\Gamma\subset X\times X$ be the
transposed graph of $\Phi_X^m$, the image of the closed immersion
$\gamma=(\Phi_X^m,\operatorname{id}_X)$, and let $\Delta\subset X\times X$
be the diagonal, the image of $\delta=(\operatorname{id}_X,\operatorname{id}_X)$.
On the strict localization $T$ of $X\times X$ at $(y,y)$ put

$$
P=(\mathbb D_XK\boxtimes K)|_T.
$$

A morphism $\psi:(\Phi_X^m)^*K\to K$ determines a class
$[\psi]\in H^0_\Gamma(T,P)$, and the local term
$\operatorname{LT}_y(\psi)$ of Definition [sk-d-trace-class] is the
image of this class under the composite

$$
R\Gamma_\Gamma(T,P)
\xrightarrow{\rho}
R\Gamma_y(\Delta,\delta^*P)
\xrightarrow{\mathrm{ev}_K}
R\Gamma_y(X,\omega_X)
\simeq R\Gamma(y,\omega_y)
\xrightarrow{\int_y} A,
$$

where $\rho$ is restriction from $\Gamma$-supported to $y$-supported
cohomology.
