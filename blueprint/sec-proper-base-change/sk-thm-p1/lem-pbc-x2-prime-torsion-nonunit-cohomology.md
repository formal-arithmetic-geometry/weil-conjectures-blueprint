+++
id = "lem-pbc-x2-prime-torsion-nonunit-cohomology"
kind = "lemma"
title = "Vanishing with a nonunit prime annihilator"
uses = ["def-weil-pbc-etale-cohomology", "def-weil-pbc-etale-sheaves", "def-weil-pbc-primary-torsion"]
lean = ["AlgebraicGeometry.IsCurve.prime_torsion_nonunit_cohomology"]
order = 1675
+++
Let $k$ be a field, $X,Y$ arbitrary schemes, $a:Y\to X$ any morphism, $\Lambda$ a commutative ring, $r$ a prime, and $F$ a sheaf of $\Lambda$-modules on $X$ [def-weil-pbc-etale-sheaves]. Suppose $r\,\operatorname{id}_F=0$, $r$ is not a unit in $\Gamma(\operatorname{Spec}k,\mathcal O)$, and $F$ has torsion of invertible order on $\operatorname{Spec}k$ [def-weil-pbc-primary-torsion]. For every $q\ge0$, both $H^q(X,F)$ and $H^q(Y,a^*F)$ of the underlying abelian sheaves [def-weil-pbc-etale-cohomology] are subsingletons.
