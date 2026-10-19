+++
id = "sk-lem-pd-generic-restriction"
kind = "lemma"
title = "Restriction to a geometric generic fibre"
order = 2388
uses = ["sk-def-ops", "sk-prop-ctf-finite-comparison", "sk-lem-pd-preservation"]
tags = ["sketch"]
+++
Here $\omega_X$ and $\delta_K$ are the dualizing complex and the double-dual morphism of
[sk-def-ops].

Let $B/k$ be a smooth integral curve and
$\bar\eta=\operatorname{Spec}\overline{k(B)}$. For a finite-type
$B$-scheme $T$ let $g_T\colon T_{\bar\eta}=T\times_B\bar\eta\to T$ be
the projection, with pullback
$g_T^*\colon D(T_{\mathrm{pro\acute et}},A)\to D(T_{\bar\eta,\mathrm{pro\acute et}},A)$. For finite
$A$, bounded constructible complexes $L$ on $T$ and $K,M$ on
$X$, a separated finite-type $B$-morphism $h\colon T\to X$, and a closed
immersion $i\colon Z\hookrightarrow X$, there are isomorphisms in
$D(X_{\bar\eta,\mathrm{pro\acute et}},A)$, resp. $D(Z_{\bar\eta,\mathrm{pro\acute et}},A)$,
compatible with evaluation

$$\begin{aligned}
 g_X^*Rh_*L&\simeq Rh_{\bar\eta,*}g_T^*L,\\
 g_Z^*i^!M&\simeq i_{\bar\eta}^!g_X^*M,\\
 g_X^*\cHom_X(K,M)&\simeq
 \cHom_{X_{\bar\eta}}(g_X^*K,g_X^*M)
 \quad(K\in\Dctf(X,A)).
\end{aligned}$$

Consequently, when $B=\mathbf A^1_k$, locally on $X$

$$
 g_X^*\omega_X\simeq\omega_{X_{\bar\eta}}(1)[2],
$$

and the two internal-Hom comparisons identify
$g_X^*\delta_K$ with $\delta_{g_X^*K}$; the extra invertible
twist and shift cancel in the double dual.
