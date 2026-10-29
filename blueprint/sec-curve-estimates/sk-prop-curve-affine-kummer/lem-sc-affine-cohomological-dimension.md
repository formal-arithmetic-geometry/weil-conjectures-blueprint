+++
id = "lem-sc-affine-cohomological-dimension"
kind = "lemma"
title = "Cohomological dimension of a smooth affine curve"
lean = ["AlgebraicGeometry.IsConnectedCurve.subsingleton_sheafH_of_two_le_of_isAffine_of_smooth"]
order = 1531
uses = ["def-sc-curves", "def-weil-pbc-etale-cohomology", "def-weil-pbc-etale-sheaves", "lem-sc-affine-generic-second", "lem-sc-cohomological-dimension", "lem-sc-generic-cohomology-comparison"]
+++
For a smooth affine connected curve $C$
over an algebraically closed field and any torsion
etale sheaf $F$,
one has $H^q(C,F)=0$ for $q>1$, with cohomology as in
[def-weil-pbc-etale-cohomology].
