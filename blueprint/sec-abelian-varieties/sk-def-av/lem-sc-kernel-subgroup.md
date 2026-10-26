+++
id = "lem-sc-kernel-subgroup"
kind = "lemma"
title = "Kernels are closed subgroup schemes"
lean = ["CategoryTheory.GrpObj.ker", "CategoryTheory.GrpObj.kerRepresentableBy", "AlgebraicGeometry.isClosedSubgroupScheme_kerι"]
order = 460
uses = ["def-sc-group-scheme", "def-sc-group-scheme-subgroup", "def-weil-pbc-scheme-conventions"]
+++
Let $f:G\to H$ be a homomorphism of
group schemes over a field $k$, and let $e_H$ be the unit
section of $H$. Then

$$
N:=G\times_{H,f,e_H}\Spec k,
$$

the kernel of $f$ in the sense of [def-sc-group-scheme], is a
group scheme over $k$ with $N(R)=\ker\bigl(f(R)\bigr)$ for every
$k$-algebra $R$, and the projection $N\to G$ exhibits $N$ as a
closed subgroup scheme of
$G$.
