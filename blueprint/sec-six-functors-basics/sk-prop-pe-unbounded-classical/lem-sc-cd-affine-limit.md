+++
id = "lem-sc-cd-affine-limit"
kind = "lemma"
title = "Passing a uniform torsion bound to an affine limit"
lean = ["AlgebraicGeometry.Scheme.HasTorsionCohomologicalDimensionLE.of_isLimit"]
order = 1900
uses = ["def-sc-etale-torsion-cd", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-cohomology-filtered-colimit", "lemma-weil-pbc-etale-cohomology-continuity", "lemma-weil-pbc-torsion-filtered-union"]
+++
Let $X=\varprojlim_i X_i$ be a filtered inverse limit of
quasi-compact
quasi-separated schemes with affine transition maps.
If $\operatorname{cd}_{\rm tor}(X_i)\leq c$ for every $i$,
then $\operatorname{cd}_{\rm tor}(X)\leq c$, with bounds as in
[def-sc-etale-torsion-cd].
