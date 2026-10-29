+++
id = "def-sfb-modobj-linearization-transport-adjunction"
kind = "definition"
title = "Linearization is left adjoint to transport"
order = 1171
uses = ["def-sfb-adjunction-projection-formula", "def-sfb-modobj-linearization", "def-sfb-modobj-linearization-right-adjoint", "def-sfb-modobj-linearized-adjunction", "def-sfb-modobj-transport"]
lean = ["CategoryTheory.Adjunction.mapModLeft", "CategoryTheory.Adjunction.projectionFormula_theta", "CategoryTheory.Adjunction.mapModLeftAdjunction"]
+++
Let $P\dashv S$ be an adjunction with $S$ strong monoidal that satisfies the projection
formula, with the projection formula of [def-sfb-adjunction-projection-formula], and let
$\mathcal B$ be a monoid object of $\mathcal D$. Then the linearization
$P_{\mathcal B}$ ([def-sfb-modobj-linearization]) is left adjoint to transport along $S$
([def-sfb-modobj-transport]):
$$
P_{\mathcal B}\dashv\operatorname{mapMod}(S)\colon\Mod_{\mathcal B}(\mathcal D)\to\Mod_{S\mathcal B}(\mathcal C).
$$
A $\mathcal B$-linear map $PM\to N$ corresponds to the $S\mathcal B$-linear adjoint map
$M\to SN$.
