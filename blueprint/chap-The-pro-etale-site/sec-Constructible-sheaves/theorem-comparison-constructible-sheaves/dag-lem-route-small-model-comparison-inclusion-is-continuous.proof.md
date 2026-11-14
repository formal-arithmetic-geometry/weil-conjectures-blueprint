+++
kind = "proof"
of = "dag-lem-route-small-model-comparison-inclusion-is-continuous"
tags = ["sheaf-dag"]
+++
1. AsSmall.down is continuous from its induced etale topology by Mathlib CategoryTheory.Sites.InducedTopology. The original inclusion toProEt X is continuous by AlgebraicGeometry.Scheme.isContinuous_toProEt, and AsSmall.up is continuous for the coefficient-sized induced pro-etale topology by AlgebraicGeometry.Scheme.coefficientProEtaleModelUp_isContinuous. Apply Functor.isContinuous_comp twice, first to toProEt X and AsSmall.up, then to AsSmall.down and their composite. This proves the unchanged statement in every coefficient universe.
