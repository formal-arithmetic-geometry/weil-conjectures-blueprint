+++
id = "def-sfb-derived-tensor-hom-adjunction-modules"
kind = "definition"
title = "Tensor-hom adjunction for module objects"
order = 1620
uses = ["def-sfb-derived-hom-modules"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.derivedTensorHomAdjunction", "AlgebraicGeometry.ProEtale.CondensedRing.derivedTensorHomAdjunction₂"]
+++
The derived hom of [def-sfb-derived-hom-modules] is right adjoint to the derived tensor
product, as an adjunction with a parameter
$-\otimes^{\mathrm L}_{\Lambda_X}-\dashv\RHom_{\Lambda_X}(-,-)$. In particular, for every
$K\in D(\Mod_{\Lambda_X})$ there is an adjunction
$K\otimes^{\mathrm L}_{\Lambda_X}-\dashv\RHom_{\Lambda_X}(K,-)$, and
$\RHom_{\Lambda_X}(K,-)$ is a right adjoint.
