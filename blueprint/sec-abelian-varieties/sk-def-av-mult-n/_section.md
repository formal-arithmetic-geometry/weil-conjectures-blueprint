+++
id = "sk-def-av-mult-n"
kind = "definition"
title = "Multiplication by $n$ and $n$-torsion"
lean = ["AlgebraicGeometry.torsionSubgroupScheme"]
order = 433
tags = ["sketch"]
+++
Let $A$ be a group scheme over $k$ and $n\ge0$. The $n$-th
*multiplication map* $[n]:A\to A$ is the $n$-th power map, given on
points by $a\mapsto a+\dots+a$ ($n$ summands), and the $n$-th
*torsion subgroup scheme* is its kernel

$$
A[n]:=\ker\bigl([n]\bigr)=A\times_{[n],A,e}\Spec k.
$$

When $A$ is commutative (e.g. an abelian variety) this is a closed
subgroup scheme of $A$ ([sk-def-av-group-scheme]); we write
$A(k)[n]=A[n](k)$ for the group of $k$-points of the kernel.
