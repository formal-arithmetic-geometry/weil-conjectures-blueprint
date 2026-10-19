+++
id = "def-sc-mult-n"
kind = "definition"
title = "Multiplication by $n$ and $n$-torsion"
lean = ["AlgebraicGeometry.torsionSubgroupScheme", "AlgebraicGeometry.isMonHom_npow_id", "AlgebraicGeometry.isClosedSubgroupScheme_torsionSubgroupScheme_ι"]
order = 444
uses = ["def-sc-abelian-variety", "def-sc-group-scheme", "lem-sc-kernel-subgroup"]
+++
Let $A$ be a group scheme
over $k$ and $n\geq0$. The $n$-th *multiplication map*
$[n]:A\to A$ is the $n$-th power map, given on points by
$a\mapsto a+\cdots+a$ ($n$ summands, written additively). The
$n$-*torsion subgroup scheme* is its kernel

$$
A[n]:=\ker([n])=A\times_{[n],A,e}\operatorname{Spec}k.
$$

When $A$ is commutative (for instance an abelian variety), $[n]$ is a
homomorphism and $A[n]$ is a closed subgroup scheme of $A$
([def-sc-group-scheme], [lem-sc-kernel-subgroup]).
