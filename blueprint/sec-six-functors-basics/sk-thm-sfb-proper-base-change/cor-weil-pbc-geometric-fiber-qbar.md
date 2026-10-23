+++
id = "cor-weil-pbc-geometric-fiber-qbar"
kind = "theorem"
title = "Qbar-l geometric-fiber formula"
order = 2215
uses = ["cor-weil-pbc-geometric-fiber-finite-extension", "det-def-sfb-bounded-constructible", "sk-def-sfb-base-change-morphism", "sk-thm-sfb-qlbar-two-colimit"]
tags = ["latex:corollary"]
+++
In the setting of [cor-weil-pbc-geometric-fiber-finite-extension] ($k$
algebraically closed, $f:X\to Y$ proper between separated schemes of finite
type over $k$, $\bar y:\operatorname{Spec}k\to Y$ a $k$-point), let
$K\in\Dbc(X,\Qlb)$ be an object of the condensed bounded constructible
category [det-def-sfb-bounded-constructible]. The base change morphism
[sk-def-sfb-base-change-morphism] is an isomorphism
$$
 L\bar y^*Rf_*K\xrightarrow{\sim}
 Ra_{\bar y,*}Li_{\bar y}^*K
 \quad\text{in }\Dbc(\operatorname{Spec}k,\Qlb).
$$
If $K\simeq\QbarX\otimes_{E_X}K_E$ for a finite $E$ and $K_E\in\Dbc(X,E)$,
as is always possible by [sk-thm-sfb-qlbar-two-colimit] (3), this isomorphism
is the extension of scalars of the isomorphism of
[cor-weil-pbc-geometric-fiber-finite-extension] for $K_E$.
