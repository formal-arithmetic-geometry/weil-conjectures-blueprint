+++
id = "lemma-weil-pbc-gabber-effacement"
kind = "lemma"
title = "Affine Gabber effacement"
lean = ["AlgebraicGeometry.Etale.exists_mono_map_eq_zero_of_henselianRing"]
order = 1559
uses = ["def-weil-pbc-henselian-terminology", "def-weil-pbc-torsion-etale-sheaf"]
+++
Let $(A,I)$ be a henselian pair [def-weil-pbc-henselian-terminology], $T=\operatorname{Spec}A$,
$T_0=\operatorname{Spec}(A/I)$, let $\Lambda$ be a commutative ring and let $F$ be a
sheaf of $\Lambda$-modules on $T_{\Et}$ which is torsion
[def-weil-pbc-torsion-etale-sheaf], with restriction $F_0$ to $T_0$. Every class
$c\in H^q(T_0,F_0)$ with $q>0$ admits a monomorphism $F\hookrightarrow F'$ into a
torsion sheaf of $\Lambda$-modules $F'$ such that the image of $c$ in
$H^q(T_0,F'_0)$ is zero.
