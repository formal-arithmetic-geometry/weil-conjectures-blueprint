+++
id = "lem-pc-genus-agrees-sc"
kind = "lemma"
title = "Agreement with the genus of file 06"
order = 747
lean = ["AlgebraicGeometry.Scheme.genus_eq_arithmeticGenus", "AlgebraicGeometry.Scheme.arithmeticGenus", "AlgebraicGeometry.Scheme.Hom.genus"]
uses = ["def-pc-genus", "def-pc-smooth-projective-curve", "def-sc-curves", "def-sc-genus", "thm-sc-serre-duality-curve"]
+++
Let $k$ be a field and $C$ a scheme over $k$ which is smooth of relative
dimension $1$ and proper over $k$ (for instance a smooth projective curve
over $k$, or a proper smooth connected curve in the sense of
[def-sc-curves]). Then the genus
$g(C)=\dim_kH^0(C,\Omega^1_{C/k})$ of [def-sc-genus] equals
$\dim_kH^1(C,\mathcal{O}_C)$, the genus of [def-pc-genus].
