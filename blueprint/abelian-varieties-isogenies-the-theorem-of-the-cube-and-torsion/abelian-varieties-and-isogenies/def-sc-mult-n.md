+++
id = "def-sc-mult-n"
kind = "definition"
title = "Multiplication by n and n-torsion"
order = 4009
lean = ["AlgebraicGeometry.AbelianVariety.multByN", "AlgebraicGeometry.AbelianVariety.torsion"]
uses = ["def-sc-abelian-variety"]
+++
Let $A$ be an abelian variety [def-sc-abelian-variety] over $k$ and
$n\geq1$. The $n$-th *multiplication map* $[n]:A\to A$ is the homomorphism
given on points by $a\mapsto a+\cdots+a$ ($n$ summands). The
$n$-*torsion subgroup scheme* is the kernel
$$
 A[n]:=\ker([n]),
$$
a closed subgroup scheme of $A$.

Unresolved dependencies: def:sc-group-scheme
