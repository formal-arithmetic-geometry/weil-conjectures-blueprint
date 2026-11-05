+++
id = "proposition-divisors-degree-g-open-chart"
kind = "proposition"
title = "Divisors of degree $g$ as an open chart"
order = 1537
lean = ["AlgebraicGeometry.exists_representableBy_invertibleDirectImageToHilbert", "AlgebraicGeometry.hilbertToPicardNormalized_invertibleDirectImageToHilbert", "AlgebraicGeometry.exists_representableBy_picardFunctorInvertibleDirectImage"]
uses = ["definition-constructible-sheaves", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "theorem-chow-s-lemma-projective-form", "definition-relative-picard-functor", "lemma-rigidification-along-section", "corollary-serre-duality-field-extension", "lemma-coherent-base-change-invertible-sheaves", "theorem-hilbert-schemes-points-smooth-curve"]
+++
The functor $F$ is represented by an open subscheme $W\subset \operatorname{Hilb}^{g}_{C/k}$.
The morphism $W\to\operatorname{Pic}_{C/k}$ associates to a divisor its rigidified
invertible sheaf. Consequently, $F$ is smooth of dimension $g$.
