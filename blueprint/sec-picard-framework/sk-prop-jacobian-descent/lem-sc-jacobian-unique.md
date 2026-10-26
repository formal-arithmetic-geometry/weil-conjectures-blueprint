+++
id = "lem-sc-jacobian-unique"
kind = "lemma"
title = "Uniqueness of the Jacobian"
lean = ["CategoryTheory.Functor.RepresentableBy.existsUnique_iso", "AlgebraicGeometry.isMonHom_uniqueUpToIso_hom_of_isPicardZeroMul", "AlgebraicGeometry.existsUnique_iso_isMonHom_of_isPicardZeroMul"]
order = 846
uses = ["def-sc-general-curve", "def-sc-jacobian"]
+++
Let $C$ be a geometrically integral smooth
projective curve over $k$ and let $(J,\varphi)$ and $(J',\varphi')$ be
two Jacobians of $C$. Then there is a
unique isomorphism $u:J\to J'$ of $k$-group schemes such that
$\varphi'=h_u\circ\varphi$.
