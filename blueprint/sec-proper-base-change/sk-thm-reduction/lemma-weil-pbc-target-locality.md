+++
id = "lemma-weil-pbc-target-locality"
kind = "lemma"
title = "Target locality"
lean = ["AlgebraicGeometry.Etale.hasTorsionBaseChange_of_affineOpens"]
order = 1257
uses = ["def-weil-pbc-derived-exchange", "def-weil-pbc-property", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-qcqs-higher-direct-image", "lemma-weil-pbc-geometric-stalk-conservative"]
+++
For proper $f:X\to Y$, the assertion $\mathrm{PBC}(f)$ of
[def-weil-pbc-property] is local on $Y$ for the etale topology. More
precisely, after an etale covering $\coprod_iV_i\to Y$, the exchange map is an
isomorphism if and only if its pullback over every $V_i$ is an isomorphism.
