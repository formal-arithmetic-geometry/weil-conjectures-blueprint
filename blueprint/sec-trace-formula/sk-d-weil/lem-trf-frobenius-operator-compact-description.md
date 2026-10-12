+++
id = "lem-trf-frobenius-operator-compact-description"
kind = "lemma"
title = "Compact-support description of the global Frobenius"
order = 2638
uses = ["def-trf-coefficient-conventions", "def-trf-frobenius-operators", "def-trf-iterated-weil-map", "def-weil-derived-direct-image", "def-weil-finite-field-fiber", "def-weil-global-geometric-frobenius", "prop-trf-scheme-galois-comparison", "thm-weil-pbc-universal-homeomorphism-invariance"]
+++
Fix the global finite-field
datum and the coefficient
conventions, and let $(K,\varphi)\in D^b_{ctf,\mathrm W}(X,A)$. Then
the $m$-th iterate $F_{c,K}^{\,m}$ of the global geometric
Frobenius of [def-trf-frobenius-operators] is the composite

$$
F_{c,K}^{\,m}=R\Gamma_c(X,\varphi^{[m]})\circ g_{\gamma,c}^{m,*},
$$

where $\varphi^{[m]}$ is the iterated Weil isomorphism of
[def-trf-iterated-weil-map] and $g_{\gamma,c}^{m,*}$ is the
compact-support base-change isomorphism along the automorphism
$g_\gamma^m$ of the
global geometric
Frobenius action.
