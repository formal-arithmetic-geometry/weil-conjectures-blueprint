+++
id = "lemma-weil-pbc-torsion-filtered-union"
kind = "lemma"
title = "Filtered torsion union"
lean = ["AlgebraicGeometry.Scheme.IsTorsionModuleSheaf.exists_isColimit", "AlgebraicGeometry.Scheme.IsTorsionSheafOfInvertibleOrder.exists_isColimit"]
order = 1460
uses = ["def-weil-pbc-etale-sheaves"]
+++
Let $\Lambda$ be a commutative ring and $F$ an etale sheaf of
$\Lambda$-modules on $X_{\Et}$ [def-weil-pbc-etale-sheaves] which is
torsion, i.e. every element of every geometric stalk of $F$ is killed by
a positive integer. Then $F$ is the colimit, in sheaves of
$\Lambda$-modules on $X_{\Et}$, of a filtered diagram of sheaves
$(D_j)_{j\in J}$ each of which is killed by some positive integer $n_j$.
If moreover the geometric stalks of $F$ are torsion of orders invertible
on a scheme $S$, the diagram can be chosen with every $n_j$ invertible
on $S$.
