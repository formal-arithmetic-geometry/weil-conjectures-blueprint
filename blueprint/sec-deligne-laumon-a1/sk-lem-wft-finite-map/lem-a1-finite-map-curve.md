+++
id = "lem-a1-finite-map-curve"
kind = "lemma"
title = "Finite map to the affine line"
lean = ["Algebra.exists_finite_formallyUnramified_away", "AlgebraicGeometry.AffineSpace.exists_isFinite_etale_morphismRestrict", "AlgebraicGeometry.AffineSpace.exists_isFinite_etale_morphismRestrict_of_finite", "AlgebraicGeometry.AffineSpace.exists_isOpenImmersion_isFinite_etale_morphismRestrict"]
order = 4029
uses = ["def-sc-curves", "def-sc-genus", "def-weil-pbc-scheme-conventions", "lem-sc-compactification", "lem-sc-point-cartier", "lem-sc-riemann-roch", "lem-weil-pbc-finite-pullback-identities", "thm-pqf-finite-iff-proper-finite-fibres"]
+++
Let $C_0$ be a smooth affine curve which is geometrically a connected
curve. There is a smooth curve $C'_0$, geometrically a connected curve, containing $C_0$ as a
dense open with finite complement, and a finite generically etale
morphism $g:C'_0\to\mathbf A^1_{k_0}$.
