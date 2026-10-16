+++
id = "lem-sc-zero-generic-acyclic"
kind = "lemma"
title = "Acyclicity of a sheaf with zero generic restriction"
lean = ["AlgebraicGeometry.IsCurve.subsingleton_H_of_genericVanishing"]
order = 1012
uses = ["def-sc-curves", "def-weil-pbc-etale-cohomology", "def-weil-pbc-etale-sheaves", "lem-weil-pbc-cohomology-filtered-colimit", "lem-weil-pbc-zero-dimensional-cohomology", "lemma-weil-pbc-finite-direct-image-exact", "prop-weil-pbc-geometric-stalks-exact"]
+++
Let $C$ be an integral separated
curve over an algebraically closed field,
and let $F$ be a torsion etale
sheaf whose restriction to the generic point is zero.
Then $H^q(C,F)=0$ for all $q>0$, in the sense of
[def-weil-pbc-etale-cohomology].
