+++
id = "def-weil-pbc-primary-torsion"
kind = "definition"
title = "$p$-primary and prime-to-$p$ torsion sheaves"
order = 1138
lean = ["AlgebraicGeometry.Etale.CurveCoefficientPair.IsPPrimary", "AlgebraicGeometry.Etale.CurveCoefficientPair.IsPrimeTo"]
uses = ["def-weil-pbc-curve-setting"]
+++
Let $(C,F)$ be a curve coefficient pair [def-weil-pbc-curve-setting], and let
$\operatorname{char}k=p>0$. The sheaf $F$ is *$p$-primary* if every element of
every geometric stalk $F_{\bar c}$ is killed by a power of $p$, and *prime to
$p$* if every such element has finite order coprime to $p$. In characteristic
zero, "prime to the characteristic" imposes no condition.

Unresolved dependencies: def:weil-pbc-geometric-stalks
