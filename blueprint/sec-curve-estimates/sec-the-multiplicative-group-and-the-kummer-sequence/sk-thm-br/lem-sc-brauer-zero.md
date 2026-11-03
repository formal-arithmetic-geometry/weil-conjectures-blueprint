+++
id = "lem-sc-brauer-zero"
kind = "lemma"
title = "The Brauer group of a smooth curve"
lean = ["AlgebraicGeometry.IsCurve.subsingleton_cohomologicalBrauerGroup_of_connectedSpace"]
order = 1458
uses = ["def-br", "def-sc-curves", "lem-sc-affine-open-proper", "lem-sc-brauer-injectivity", "lem-sc-compactification", "lem-sc-dim0-finite", "lem-sc-divisor-exact-sequence", "lem-sc-point-z-cohomology", "lem-sc-proper-affine-finite", "lem-sc-tsen"]
+++
Let $C$ be a smooth separated connected curve over
algebraically closed $k$. Then its Brauer group ([def-br]) vanishes:

$$
H^2(C_{\Et},\mathbf G_m)=0.
$$
