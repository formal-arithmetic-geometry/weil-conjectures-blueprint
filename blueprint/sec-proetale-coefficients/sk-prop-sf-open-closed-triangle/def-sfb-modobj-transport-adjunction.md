+++
id = "def-sfb-modobj-transport-adjunction"
kind = "definition"
title = "Monoidal adjunctions lift to module objects"
order = 1123
uses = ["def-sfb-modobj-restriction", "def-sfb-modobj-transport"]
lean = ["CategoryTheory.Adjunction.mapModAdjunction", "CategoryTheory.Adjunction.isMonHom_unitAlgHom"]
+++
Let $F\colon\mathcal C\rightleftarrows\mathcal D\colon G$ be a monoidal adjunction
$F\dashv G$. That is, $F$ is strong monoidal, $G$ is lax monoidal, and the lax structure
of $G$ is the mate of the monoidal structure of $F$. Let $\mathcal R$ be a monoid object
of $\mathcal C$. The unit $u_{\mathcal R}\colon\mathcal R\to GF\mathcal R$ is a morphism of
monoid objects, for the structure on $GF\mathcal R$ transported along $F$ and then $G$
([def-sfb-modobj-transport]). There is an adjunction
$$
\operatorname{mapMod}(F)\dashv\operatorname{Res}_{u_{\mathcal R}}\circ\operatorname{mapMod}(G)
\colon\Mod_{F\mathcal R}(\mathcal D)\to\Mod_{\mathcal R}(\mathcal C),
$$
with $\operatorname{Res}$ as in [def-sfb-modobj-restriction]. On morphisms it is the
adjunction bijection of $F\dashv G$: an $F\mathcal R$-linear map $FM\to N$ corresponds to an
$\mathcal R$-linear map $M\to GN$, where $\mathcal R$ acts on $GN$ through $u_{\mathcal R}$.
