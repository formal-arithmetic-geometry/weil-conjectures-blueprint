+++
id = "cor-weil-pbc-geometric-fiber-qbar"
kind = "theorem"
title = "Qbar-l geometric-fiber formula"
order = 1420
uses = ["cor-weil-pbc-geometric-fiber-finite", "cor-weil-pbc-geometric-fiber-finite-extension", "sk-thm-sfb-proper-base-change", "det-thm-sfb-proper-base-change-rational"]
tags = ["latex:corollary"]
+++
In the setup of the finite-level geometric-fiber corollary
[cor-weil-pbc-geometric-fiber-finite] (with $f:X\to Y$ proper between
schemes of finite type over $k$), let $K\in\Dbc(X,\Qlb)$ be an object of the
condensed bounded constructible category [sk-def-sfb-bounded-constructible].
The base change morphism is an isomorphism
$$
 L\bar y^*Rf_*K\xrightarrow{\sim}
 Ra_{\bar y,*}Li_{\bar y}^*K
 \quad\text{in }\Dbc(\operatorname{Spec}\Omega,\Qlb).
$$
If $K\simeq\QbarX\otimes_{E_X}K_E$ for a finite $E$ and $K_E\in\Dbc(X,E)$,
as is always possible by [sk-thm-sfb-qlbar-two-colimit] (3), this isomorphism
is the extension of scalars of the isomorphism of
[cor-weil-pbc-geometric-fiber-finite-extension] for $K_E$.
