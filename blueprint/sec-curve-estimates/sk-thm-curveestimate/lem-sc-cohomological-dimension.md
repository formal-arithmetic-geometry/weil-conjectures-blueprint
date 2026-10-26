+++
id = "lem-sc-cohomological-dimension"
kind = "lemma"
title = "Cohomological dimension of a smooth curve"
lean = ["AlgebraicGeometry.IsConnectedCurve.subsingleton_etaleCohomology_of_two_lt", "AlgebraicGeometry.IsCurve.subsingleton_sheafH_of_three_le_of_isIntegral"]
order = 1406
uses = ["def-sc-curves", "def-weil-pbc-etale-cohomology", "def-weil-pbc-etale-sheaves", "lem-sc-function-field-cd-one", "lem-sc-generic-cohomology-comparison", "lem-sc-regular-dim1-dvr", "lem-sc-smooth-regular", "lem-sc-zero-generic-acyclic", "prop-weil-pbc-strict-henselization-stalk-formula", "thm-sp-grothendieck"]
+++
For a smooth separated connected curve $C$
over an algebraically closed field and any torsion
etale sheaf $F$,
one has $H^q(C,F)=0$ for $q>2$, with cohomology as in
[def-weil-pbc-etale-cohomology].
