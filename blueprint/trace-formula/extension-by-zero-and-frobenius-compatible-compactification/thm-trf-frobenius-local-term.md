+++
id = "thm-trf-frobenius-local-term"
kind = "theorem"
title = "Local term of the Frobenius correspondence"
order = 3945
uses = ["def-trf-coefficient-conventions", "def-trf-frobenius-operators", "def-trf-iterated-weil-map", "def-trf-local-term", "def-weil-finite-field-fiber", "def-weil-scheme-morphism-properties", "lem-trf-contracting-trace-stalk", "lem-trf-frobenius-degree-formula", "lem-trf-frobenius-differential-vanishing", "lem-trf-frobenius-formal-contraction", "lem-trf-local-term-locality", "thm-trf-contracting-local-term", "thm-trf-frobenius-fixed-points"]
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
stalk complex. The degree-dependence of the right-hand side is
[lem-trf-frobenius-degree-formula].

## Proof

By [thm-trf-frobenius-fixed-points] the points
$y\in X_0(\mathbf F_{q^m})$ are exactly the open-and-closed
components of $\operatorname{Fix}(\Phi^m)$, so the local terms of
[def-trf-local-term] are indexed by them. The graph
correspondence $c=(\operatorname{id}_X,\Phi^m)$ with the
scheme-Frobenius map $u_m$ of [def-trf-iterated-weil-map] is a
contracting correspondence at each such component: its differential
vanishes by [lem-trf-frobenius-differential-vanishing] and its
two legs agree modulo the square of the maximal ideal by
[lem-trf-frobenius-formal-contraction]. By
[lem-trf-local-term-locality] the local term depends only on the
stalk $K_{\bar y}$ and on the induced stalk map, which by
[def-trf-frobenius-operators] is the local geometric Frobenius
$F_{y,m}$. With these identifications the asserted equality is
exactly [thm-trf-contracting-local-term], whose proof uses the
normal-cone reduction [lem-trf-contracting-trace-stalk]: that
reduction (Varshavsky,
[loc. cit.](https://arxiv.org/abs/math/0505564), Theorem 2.1.2)
is the single remaining unexpanded input of the Frobenius local-term
calculation and is flagged as an open obligation at
[lem-trf-contracting-trace-stalk].
