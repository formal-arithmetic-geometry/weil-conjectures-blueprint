+++
id = "lem-trf-iterated-weil-cocycle"
kind = "lemma"
title = "Cocycle identity for the iterated Weil isomorphism"
order = 2635
uses = ["def-trf-iterated-weil-map", "def-trf-scheme-frobenius", "def-trf-strict-weil-complex"]
+++
Let $(K,\varphi)\in D^b_{ctf,\mathrm W}(X,A)$ be a
strict Weil complex under the
conventions of [def-trf-strict-weil-complex], with
$g_\gamma=g_X$ the
geometric-Frobenius automorphism
of [def-trf-scheme-frobenius], and let

$$
\varphi^{[m]}:Lg_\gamma^{m*}K\xrightarrow{\ \sim\ }K
\qquad(m\in\mathbf Z_{\geq1})
$$

be the iterated Weil isomorphism
of [def-trf-iterated-weil-map]. Then for all
$m,n\in\mathbf Z_{\geq1}$ the identity

$$
\varphi^{[m+n]}=\varphi^{[m]}\circ Lg_\gamma^{m*}\varphi^{[n]}
$$

holds after the canonical pullback identifications
$Lg_\gamma^{m*}Lg_\gamma^{n*}K\cong L(g_\gamma^m\circ g_\gamma^n)^*K=Lg_\gamma^{m+n*}K$.
