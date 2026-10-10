+++
id = "lemma-nagata-blowup-invertible-factor"
kind = "lemma"
title = "Blow-up is unchanged after multiplying by an invertible factor"
order = 131
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.exists_blowup_mul_isInvertible_iso"]
uses = ["def-nagata-effective-cartier-ideal", "def-nagata-extended-ideal", "def-nagata-global-blowup", "def-nagata-invertible-ideal", "lemma-nagata-cartier-total-transform-blowup", "lemma-nagata-ideal-invertible-product-factor", "lemma-nagata-invertible-ideal-mul", "lemma-nagata-invertible-product-factor", "prop-nagata-global-blowup-cover-independent", "thm-nagata-blowup-principalizes-center", "thm-nagata-blowup-universal-property"]
+++
Let $X$ be a scheme, let $\mathcal L$ be an invertible ideal on $X$, and
let $\mathcal J$ be any quasi-coherent ideal on $X$. Then there is an
isomorphism
$\operatorname{Bl}_{\mathcal L\mathcal J}(X)\cong\operatorname{Bl}_{\mathcal J}(X)$
over $X$.
