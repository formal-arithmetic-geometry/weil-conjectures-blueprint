+++
id = "lem-sfb-finite-upper-star-exact"
kind = "lemma"
title = "$g^*$ is exact"
order = 913
uses = ["def-sfb-finite-upper-lower-star-adjunction", "def-sfb-finite-upper-star"]
lean = ["AlgebraicGeometry.ProEtale.preservesFiniteLimits_upperStar", "AlgebraicGeometry.ProEtale.preservesFiniteLimits_op_lan_overPullback_of_isGrothendieckAbelian"]
+++
For every morphism $g\colon Z\to Y$ the pullback $g^*$ of [def-sfb-finite-upper-star]
preserves finite limits. Being also a left adjoint
([def-sfb-finite-upper-lower-star-adjunction]), it is exact.
