+++
id = "proposition-divisors-degree-g-open-chart"
kind = "proposition"
title = "Divisors of degree $g$ as an open chart"
order = 1537
lean = ["AlgebraicGeometry.exists_representableBy_invertibleDirectImageToHilbert", "AlgebraicGeometry.hilbertToPicardNormalized_invertibleDirectImageToHilbert", "AlgebraicGeometry.exists_representableBy_picardFunctorInvertibleDirectImage"]
uses = ["definition-small-pro-etale-site", "definition-constructible-sheaves", "lemma-perfect-complexes-geometric-point", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "theorem-chow-s-lemma-projective-form", "definition-relative-picard-functor", "corollary-serre-duality-field-extension", "lemma-coherent-base-change-invertible-sheaves"]
+++
The functor $F$ is represented by an open subscheme $W\subset \operatorname{Hilb}^{g}_{C/k}$.
The morphism $W\to\operatorname{Pic}_{C/k}$ associates to a divisor its rigidified
invertible sheaf. Consequently, $F$ is smooth of dimension $g$.
