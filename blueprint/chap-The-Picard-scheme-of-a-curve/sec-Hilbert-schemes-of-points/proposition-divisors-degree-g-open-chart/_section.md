+++
id = "proposition-divisors-degree-g-open-chart"
kind = "proposition"
title = "Divisors of degree $g$ as an open chart"
order = 1540
lean = ["AlgebraicGeometry.isRepresentable_picardFunctorInvertibleDirectImage"]
uses = ["lemma-acyclic-resolutions", "definition-compactification-refinement", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "lemma-coherent-base-change-invertible-sheaves", "theorem-hilbert-schemes-points-smooth-curve"]
+++
The functor $F$ is represented by an open subscheme $W\subset \operatorname{Hilb}^{g}_{C/k}$.
The morphism $W\to\operatorname{Pic}_{C/k}$ associates to a divisor its rigidified
invertible sheaf. Consequently, $F$ is smooth of dimension $g$.
