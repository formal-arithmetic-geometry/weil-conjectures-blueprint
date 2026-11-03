+++
id = "sk-thm-picard-f-representable"
kind = "proposition"
title = "Divisors of degree $g$ as an open chart"
order = 892
lean = ["AlgebraicGeometry.isRepresentable_picardFunctorInvertibleDirectImage", "AlgebraicGeometry.exists_representableBy_invertibleDirectImageToHilbert", "AlgebraicGeometry.hilbertPresheaf_curve_representable"]
uses = ["sk-prop-picard-pic-split", "sk-lem-abelian-seesaw", "sk-prop-av-isogeny", "sk-def-picard-pic", "sk-thm-picard-perfect", "sk-thm-picard-hilb-curves", "sec-nagata-compactification", "sec-abelian-varieties"]
tags = ["sketch"]
+++
The functor $F$ is represented by an open subscheme $W\subset H_g$.
The morphism $W\to\operatorname{Pic}_{C/k}$ associates to a divisor its rigidified
invertible sheaf. Consequently, $F$ is smooth of dimension $g$.
