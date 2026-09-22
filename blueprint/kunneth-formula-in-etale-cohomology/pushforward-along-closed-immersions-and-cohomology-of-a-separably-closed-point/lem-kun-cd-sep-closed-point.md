+++
id = "lem-kun-cd-sep-closed-point"
kind = "lemma"
title = "Cohomological dimension of a separably closed point"
order = 6054
lean = ["AlgebraicGeometry.Etale.cohomologicalDimension_eq_zero_of_isSepClosed"]
uses = ["def-kun-cd", "lem-kun-03QU-sep-closed", "def-kun-separably-closed"]
+++
If $K$ is a separably closed field then $\operatorname{cd}(\Spec(K))=0$.

## Proof

By [def-kun-cd], $\operatorname{cd}(\Spec(K))=0$ means $H^q=0$ for every
torsion étale sheaf and every $q>0$, which is [lem-kun-03QU-sep-closed].
