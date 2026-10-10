+++
id = "prop-trf-graph-frobenius-operator"
kind = "theorem"
title = "Graph construction of the global Frobenius operator"
order = 2300
tags = ["latex:proposition"]
uses = ["def-exchange-projection", "def-trf-coefficient-conventions", "def-trf-frobenius-operators", "def-trf-global-operator", "def-trf-graph-correspondence", "def-trf-iterated-weil-map", "def-trf-scheme-frobenius", "def-trf-strict-weil-complex", "def-weil-finite-field-fiber", "def-weil-global-geometric-frobenius", "def-weil-scheme-morphism-properties", "lem-trf-adjoint-mate", "lem-trf-frobenius-operator-compact-description", "lem-trf-iterated-weil-cocycle", "prop-functor-package", "prop-trf-graph-operator", "prop-trf-scheme-galois-comparison"]
+++
Fix the global finite-field datum
and the coefficient
conventions, and let $(K,\varphi)$ be a
strict Weil complex of
[def-trf-strict-weil-complex]. For $m\in\mathbf Z_{\geq1}$ let
$\Phi^m$ be the $m$-fold iterate of the
scheme Frobenius of
[def-trf-scheme-frobenius] and
$u_m:L\Phi^{m*}K\to K$ the
scheme-Frobenius map of
[def-trf-iterated-weil-map], and consider the
graph correspondence
$c=(\operatorname{id}_X,\Phi^m)$ with $u_m$. Then its
global operator $T_c(u_m)$ of
[def-trf-global-operator], identified as in
[prop-trf-graph-operator], equals the $m$-th iterate of the
global geometric Frobenius:

$$
T_c(u_m)=F_{c,K}^{\,m}:
R\Gamma_c(X,K)\longrightarrow R\Gamma_c(X,K),
$$

where $F_{c,K}^{\,m}$ is the endomorphism of the
global geometric Frobenius
operator of [def-trf-frobenius-operators] (equivalently the
global geometric Frobenius action of
[def-weil-global-geometric-frobenius]). The equality is natural in
$(K,\varphi)$ and compatible with the cocycle law in $m$.

More generally, let $K\in D^b_{ctf}(X,A)$ carry no Weil structure and
let $v:Lg_\gamma^{m*}K\to K$ be an arbitrary morphism, not necessarily
invertible. Then the graph correspondence $c=(\operatorname{id}_X,\Phi^m)$
with coefficient map $v\circ\kappa^{(m)}_K:L\Phi^{m*}K\to K$ has

$$
T_c\bigl(v\circ\kappa^{(m)}_K\bigr)
=R\Gamma_c(X,v)\circ g_{\gamma,c}^{m,*}:
R\Gamma_c(X,K)\longrightarrow R\Gamma_c(X,K),
$$

where $g_{\gamma,c}^{m,*}:R\Gamma_c(X,K)\xrightarrow{\sim}R\Gamma_c(X,Lg_\gamma^{m*}K)$
is the compact-support base-change isomorphism along $g_\gamma^m$; the
displayed identity $T_c(u_m)=F_{c,K}^{\,m}$ is the case $v=\varphi^{[m]}$.
