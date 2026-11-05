+++
kind  = "proof"
of = "det-def-sfb-transport"
uses = ["def-sfb-modobj-transport", "def-sfb-modobj-transport-adjunction", "def-sfb-projection-formula", "def-sfb-modobj-linearization", "def-sfb-modobj-linearization-right-adjoint", "def-sfb-modobj-linearized-adjunction", "def-sfb-adjunction-has-projection-formula", "def-sfb-adjunction-projection-formula", "def-sfb-modobj-linearization-transport-adjunction"]
+++
Part 1 is [def-sfb-modobj-transport]. Part 2 is [def-sfb-modobj-transport-adjunction].

Part 3: projection formulas are defined in [def-sfb-projection-formula]. The
linearization $P_{\mathcal B}$ is [def-sfb-modobj-linearization], and
$G_{\mathcal B}$ is [def-sfb-modobj-linearization-right-adjoint]. The adjunction
$P_{\mathcal B}\dashv G_{\mathcal B}$ is [def-sfb-modobj-linearized-adjunction].

Part 4: the projection formula map and the condition that it is invertible are
[def-sfb-adjunction-has-projection-formula]. The resulting projection formula is
[def-sfb-adjunction-projection-formula]. The adjunction
$P_{\mathcal B}\dashv\operatorname{mapMod}(S)$ is
[def-sfb-modobj-linearization-transport-adjunction].
