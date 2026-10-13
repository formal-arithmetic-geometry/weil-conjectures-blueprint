+++
id = "thm-trf-frobenius-local-term"
kind = "theorem"
title = "Local term of the Frobenius correspondence"
order = 2700
uses = ["d-curve-pieces", "def-trf-borel-moore-pushforward", "def-trf-coefficient-conventions", "def-trf-coefficient-pushforward", "def-trf-frobenius-coefficient-morphism", "def-trf-frobenius-operators", "def-trf-iterated-weil-map", "def-trf-local-term", "def-weil-extension-by-zero", "def-weil-finite-field-fiber", "def-weil-scheme-morphism-properties", "fix-lem-finite-tor-perfect", "lem-trf-frobenius-degree-formula", "lem-trf-local-term-locality", "lem-trf-local-term-point", "prop-trf-pairing-local-decomposition", "prop-trf-trace-class-additivity", "cor-sf-ambient-adjoint-discharge", "thm-sf-preservation-class", "thm-trf-frobenius-fixed-points", "thm-trf-trace-proper-compatibility"]
+++
Fix the global finite-field datum
$p,a,q,k_0,k$, where $q=p^a$, and the
coefficient conventions,
$A=A_{E,n}$, let $X_0$ be
separated of finite type
over $k_0$, put $X=X_0\times_{k_0}k$, and let
$(K,\varphi)\in D^b_{ctf,\mathrm W}(X,A)$ be a strict Weil complex.
Let $u_m:L\Phi^m{}^*K\to K$ be the scheme-Frobenius map of
[def-trf-iterated-weil-map], and consider the graph correspondence
$c=(\operatorname{id}_X,\Phi^m)$ with $u_m$. For each
$y\in X_0(\mathbf F_{q^m})$, viewed via
[thm-trf-frobenius-fixed-points] as a closed-and-open component of
$\operatorname{Fix}(\Phi^m)$, the local
term is

$$
\operatorname{LT}_y(u_m)
=
\operatorname{tr}_A\bigl(F_{y,m}\mid K_{\bar y}\bigr)
$$

in $A$, where $F_{y,m}$ is the
local geometric Frobenius
operator of [def-trf-frobenius-operators] and $K_{\bar y}$ is the
stalk complex.

More generally, let $K\in D^b_{ctf}(X,A)$ carry no Weil structure and
let $v:L\Phi^{m*}K\to K$ be an arbitrary, not necessarily invertible,
morphism, for instance the iterate $\psi_m$ of a Frobenius coefficient
morphism $\psi$ of [def-trf-frobenius-coefficient-morphism]. Then for
the graph correspondence $(\operatorname{id}_X,\Phi^m)$ with $v$

$$
\operatorname{LT}_y(v)=\operatorname{tr}_A\bigl(v_{\bar y}\mid K_{\bar y}\bigr),
$$

where $v_{\bar y}:K_{\bar y}\cong(L\Phi^{m*}K)_{\bar y}\to K_{\bar y}$
is the stalk map at the fixed point $\bar y$. The first formula is the
case $v=u_m$, whose stalk map at $\bar y$ is $F_{y,m}$
([def-trf-frobenius-operators]).
