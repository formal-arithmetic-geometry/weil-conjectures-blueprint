+++
id = "def-sfb-modobj-linearized-adjunction"
kind = "definition"
title = "The linearized adjunction $P_{\\mathcal B}\\dashv G_{\\mathcal B}$"
order = 1548
uses = ["def-sfb-modobj-linearization", "def-sfb-modobj-linearization-right-adjoint"]
lean = ["CategoryTheory.Functor.ProjectionFormula.mapModAdjunction"]
+++
In the situation of [def-sfb-modobj-linearization-right-adjoint], the adjunction
bijection of $P\dashv G$ restricts to a bijection between $\mathcal B$-linear maps
$PM\to N$ and $S\mathcal B$-linear maps $M\to GN$. This gives an adjunction
$$
P_{\mathcal B}\dashv G_{\mathcal B}\colon\Mod_{\mathcal B}(\mathcal D)\to\Mod_{S\mathcal B}(\mathcal C)
$$
between the linearizations of [def-sfb-modobj-linearization] and
[def-sfb-modobj-linearization-right-adjoint].
