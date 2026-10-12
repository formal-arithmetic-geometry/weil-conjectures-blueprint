+++
id = "def-sfb-derived-tensor-hom-adjunction-sheaves"
kind = "definition"
title = "Tensor-hom adjunction for pro-étale sheaves"
order = 1603
uses = ["def-sfb-derived-hom-sheaves"]
lean = ["AlgebraicGeometry.ProEtale.derivedTensorHomAdjunction", "AlgebraicGeometry.ProEtale.derivedTensorHomAdjunction₂"]
+++
The derived hom of [def-sfb-derived-hom-sheaves] is right adjoint to the derived tensor
product, as an adjunction with a parameter $-\otimes^{\mathrm L}-\dashv\RHom(-,-)$. In
particular, for every $K\in D(X_{\mathrm{proét}},\mathcal A)$ there is an adjunction
$K\otimes^{\mathrm L}-\dashv\RHom(K,-)$, and $\RHom(K,-)$ is a right adjoint.
