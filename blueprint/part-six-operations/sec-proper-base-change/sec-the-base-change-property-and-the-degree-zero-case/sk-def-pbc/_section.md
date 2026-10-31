+++
id = "sk-def-pbc"
kind = "definition"
title = "Torsion and the PBC property"
order = 180
lean = ["AlgebraicGeometry.Etale.HasTorsionBaseChange", "AlgebraicGeometry.Scheme.IsTorsionSheaf", "AlgebraicGeometry.Scheme.IsTorsionModuleSheaf", "AlgebraicGeometry.Scheme.isTorsionAbelianSheaf_characterizations", "AlgebraicGeometry.Scheme.constant_ratModIntSheaf_sections_not_torsion"]
uses = ["sk-def-conv", "sk-def-exchange", "sk-def-pbc-conventions"]
tags = ["sketch"]
+++
A sheaf $F$ of abelian groups, or of $\Lambda$-modules, is
*torsion* if every geometric stalk is a torsion abelian group.
Equivalently,

$$
F=\varinjlim_{n\geq1}F[n],\qquad F[n]=\ker(n:F\to F),
$$

where the positive integers are ordered by divisibility.

For a morphism $f:X\to Y$, write $\mathrm{PBC}_{\Lambda}(f)$ if the base change map
(4.3) is an isomorphism
for every base change
$g:Y'\to Y$ and every $K\in D^+(X_{\acute{e}t},\Lambda)$ with torsion
cohomology sheaves. If $\Lambda$ is torsion as an abelian group, it is
killed by the additive order of $1$, so every sheaf of $\Lambda$-modules
is torsion.
