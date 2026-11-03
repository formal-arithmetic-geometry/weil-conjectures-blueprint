+++
id = "sk-lem-pd-generic-restriction"
kind = "lemma"
title = "Restriction to a geometric generic fibre"
order = 510
uses = ["sk-def-ops", "sk-prop-ctf-finite-comparison", "sk-lem-pd-preservation"]
tags = ["sketch"]
+++
Let $B/k$ be a smooth integral curve and
$\bar\eta=\operatorname{Spec}\overline{k(B)}$. For a finite-type
$B$-scheme $T$ let $g_T:T_{\bar\eta}=T\times_B\bar\eta\to T$ be
the projection, with pullback
$g_T^*:D(T_{\mathrm{pro}\acute{e}t},A)\to D(T_{\bar\eta,\mathrm{pro}\acute{e}t},A)$. For finite
$A$, bounded constructible complexes $L$ on $T$ and $K,M$ on
$X$, a separated finite-type $B$-morphism $h:T\to X$, and a closed
immersion $i:Z\hookrightarrow X$, there are isomorphisms
compatible with evaluation

$$
\begin{aligned}
g_X^*Rh_*L&\simeq Rh_{\bar\eta,*}g_T^*L,\\
g_Z^*i^!M&\simeq i_{\bar\eta}^!g_X^*M,\\
g_X^*\cHom_X(K,M)&\simeq
\cHom_{X_{\bar\eta}}(g_X^*K,g_X^*M)
\quad(K\in D^b_{\mathrm{ctf}}(X,A)).
\end{aligned}
$$

Consequently, when $B=\mathbf A^1_k$, locally on $X$

$$
g_X^*\omega_X\simeq\omega_{X_{\bar\eta}}(1)[2],
$$

and the two comparisons for internal Hom identify
$g_X^*\delta_K$ with $\delta_{g_X^*K}$; the extra invertible
twist and shift cancel in the double dual.
