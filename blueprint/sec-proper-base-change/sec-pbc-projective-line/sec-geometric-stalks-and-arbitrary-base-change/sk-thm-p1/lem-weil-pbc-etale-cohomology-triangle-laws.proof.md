+++
kind = "proof"
of = "lem-weil-pbc-etale-cohomology-triangle-laws"
uses = ["lem-weil-pbc-cohomology-pullback-functorial", "lem-weil-pbc-inverse-image-composition"]
+++
Apply the identity part of cohomologyPullbackFunctorial and upperStarComp_id_left to obtain the identity map. ([lem-weil-pbc-cohomology-pullback-functorial], [lem-weil-pbc-inverse-image-composition]).

Apply naturality and composition of cohomology pullback; combine the three sheaf morphisms using upperStarComp_hom_app_map_upperStarComp_inv_app_assoc, the component associativity coherence of inverse images. Cancel the comparison with its inverse. ([lem-weil-pbc-cohomology-pullback-functorial], [lem-weil-pbc-inverse-image-composition]).
