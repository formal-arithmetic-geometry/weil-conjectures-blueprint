+++
id = "def-sfb-modobj-restrict-coextend-adjunction"
kind = "definition"
title = "Restriction of scalars is left adjoint to coextension"
order = 1150
uses = ["def-sfb-modobj-coextension", "def-sfb-modobj-restriction"]
lean = ["CategoryTheory.Mod.restrictCoextendAdjunction"]
+++
In the situation of [def-sfb-modobj-coextension], let $\varphi$ be a morphism of monoid
objects. Let $\varepsilon_N\colon\Hom_{\mathcal R}(\mathcal S,N)\to N$ be evaluation at
the unit of $\mathcal S$. Then $\varepsilon_N$ is $\mathcal R$-linear on
$\operatorname{Res}_\varphi\Hom_{\mathcal R}(\mathcal S,N)$
([def-sfb-modobj-restriction]). Moreover, $g\mapsto\varepsilon_N\circ\operatorname{Res}_\varphi(g)$
is a bijection, natural in $M$ and $N$, from $\mathcal S$-linear maps
$M\to\operatorname{Coext}_\varphi N$ to $\mathcal R$-linear maps
$\operatorname{Res}_\varphi M\to N$. Its inverse sends $f$ to $m\mapsto(s\mapsto f(sm))$.
This is an adjunction
$$
\operatorname{Res}_\varphi\dashv\operatorname{Coext}_\varphi .
$$
