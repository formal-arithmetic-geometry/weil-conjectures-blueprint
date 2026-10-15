+++
id = "sk-def-sf-weil-complexes"
kind = "definition"
title = "Weil structure"
order = 2415
lean = ["AlgebraicGeometry.Etale.WeilComplex"]
tags = ["sketch"]
+++
Fix $k_0=\mathbb F_q$ and its algebraic closure $k$, and let $f:X\to Y$ be
obtained from a smooth morphism $f_0:X_0\to Y_0$ over $k_0$ by extension to
$k$. For a scheme $T=T_0\times_{k_0}k$, let
$\operatorname{Fr}_T:T\to T$ be the semilinear automorphism induced by the
geometric Frobenius $\sigma=\sigma_{\mathrm{ar}}^{-1}\in\operatorname{Gal}(k/k_0)$,
and for an admissible coefficient ring $\Lambda$ let
$\operatorname{Fr}_T^*:\Dctf(T,\Lambda)\to\Dctf(T,\Lambda)$ be the induced
pullback.

For $K\in\Dctf(Y,\Lambda)$, a *Weil structure* is an isomorphism in
$\Dctf(Y,\Lambda)$

$$
\phi_K:\operatorname{Fr}_Y^*K\xrightarrow{\sim}K.
$$

A *Weil complex* is a pair $(K,\phi_K)$ with this structure. A morphism
$(K,\phi_K)\to(L,\phi_L)$ is a morphism $h:K\to L$ in $\Dctf(Y,\Lambda)$
satisfying

$$
h\circ\phi_K=\phi_L\circ\operatorname{Fr}_Y^*(h).
$$

The same definition applies on $X$ or on any $T=T_0\times_{k_0}k$.
