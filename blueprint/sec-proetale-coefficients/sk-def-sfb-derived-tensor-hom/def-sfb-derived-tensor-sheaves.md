+++
id = "def-sfb-derived-tensor-sheaves"
kind = "definition"
title = "Derived tensor product of pro-étale sheaves"
order = 1617
uses = ["lem-sfb-derived-monoidal", "sk-def-sfb-sheaf-tensor", "sk-def-sfb-derived-categories"]
lean = ["AlgebraicGeometry.ProEtale.derivedTensor"]
+++
Let $\mathcal A$ be a closed symmetric monoidal Grothendieck abelian category whose tensor
product is additive and which has functorial flat resolutions, and let $X$ be a scheme.
The *derived tensor product*
$$
-\otimes^{\mathrm L}-\colon D(X_{\mathrm{proét}},\mathcal A)\times D(X_{\mathrm{proét}},\mathcal A)\to D(X_{\mathrm{proét}},\mathcal A)
$$
is the tensor product of the monoidal structure of [lem-sfb-derived-monoidal] on the
derived category of $\Sh(X_{\mathrm{proét}},\mathcal A)$, equipped with the tensor
product of [sk-def-sfb-sheaf-tensor].
