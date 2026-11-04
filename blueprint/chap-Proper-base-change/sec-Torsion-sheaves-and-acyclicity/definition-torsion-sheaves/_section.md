+++
id = "definition-torsion-sheaves"
kind = "definition"
title = "Torsion sheaves"
order = 340
lean = ["AlgebraicGeometry.Scheme.IsTorsionAbelianSheaf", "AlgebraicGeometry.Scheme.IsTorsionModuleSheaf", "AlgebraicGeometry.Scheme.IsTorsionSheaf", "AlgebraicGeometry.Scheme.isTorsionAbelianSheaf_characterizations"]
+++
A sheaf $F$ of abelian groups, or of $\Lambda$-modules, is
*torsion* if every geometric stalk is a torsion abelian group.
Equivalently,

$$
F=\varinjlim_{n\geq1}F[n],\qquad F[n]=\ker(n:F\to F),
$$

where the positive integers are ordered by divisibility.
