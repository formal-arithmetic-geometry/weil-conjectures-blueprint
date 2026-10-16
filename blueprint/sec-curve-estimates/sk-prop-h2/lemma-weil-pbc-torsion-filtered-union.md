+++
id = "lemma-weil-pbc-torsion-filtered-union"
kind = "lemma"
title = "Filtered torsion union"
lean = ["AlgebraicGeometry.Scheme.IsTorsionModuleSheaf.exists_isColimit", "AlgebraicGeometry.Scheme.IsTorsionSheafOfInvertibleOrder.exists_isColimit"]
order = 962
uses = ["def-weil-pbc-etale-sheaves"]
+++
For every torsion sheaf [def-weil-pbc-etale-sheaves] $F$ on $X_{\Et}$,

$$
 F=\varinjlim_{(\mathbf N_{>0},\mid)}F[n],\qquad
 F[n]=\ker(n:F\to F),
$$

as a filtered colimit in $\Ab(X_{\Et})$. Here positive integers are ordered
by divisibility, and for $n\mid m$ the transition map is the inclusion
$F[n]\hookrightarrow F[m]$; this poset is filtered because
$\operatorname{lcm}(n,m)$ is a common upper bound.
