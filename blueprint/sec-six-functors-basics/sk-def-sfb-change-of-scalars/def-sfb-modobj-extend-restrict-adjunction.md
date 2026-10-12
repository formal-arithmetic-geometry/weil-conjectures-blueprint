+++
id = "def-sfb-modobj-extend-restrict-adjunction"
kind = "definition"
title = "Extension of scalars is left adjoint to restriction"
order = 1532
uses = ["def-sfb-modobj-extension", "def-sfb-modobj-restriction"]
lean = ["CategoryTheory.Mod.extendRestrictAdjunction"]
+++
In the situation of [def-sfb-modobj-extension], let
$u_M\colon M\to\mathcal S\otimes_{\mathcal R}M$ be the composite
$M\cong\mathbf 1\otimes M\xrightarrow{\eta_{\mathcal S}\otimes M}\mathcal S\otimes M
\to\mathcal S\otimes_{\mathcal R}M$. Then $u_M$ is $\mathcal R$-linear into
$\operatorname{Res}_\varphi(\mathcal S\otimes_{\mathcal R}M)$
([def-sfb-modobj-restriction]). Moreover, $g\mapsto\operatorname{Res}_\varphi(g)\circ u_M$
is a bijection, natural in $M$ and $N$, from $\mathcal S$-linear maps
$\operatorname{Ext}_\varphi M\to N$ to $\mathcal R$-linear maps
$M\to\operatorname{Res}_\varphi N$. This is an adjunction
$$
\operatorname{Ext}_\varphi\dashv\operatorname{Res}_\varphi .
$$
