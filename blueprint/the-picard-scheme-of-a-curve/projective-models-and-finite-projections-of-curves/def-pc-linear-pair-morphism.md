+++
id = "def-pc-linear-pair-morphism"
kind = "definition"
title = "The morphism determined by two linear forms"
order = 4291
lean = ["AlgebraicGeometry.linearPairMorphism"]
uses = ["def-pc-standard-graded-algebra", "def-pc-proj", "lem-pc-linear-pair-morphism-gluing"]
+++
Let $S$ be a standard graded $k$-algebra
[def-pc-standard-graded-algebra], and let $l_0,l_1\in S_1$ satisfy
$D_+(l_0)\cup D_+(l_1)=\operatorname{Proj}(S)$. The morphism
$\pi_{l_0,l_1}:\operatorname{Proj}(S)\to\mathbf P^1_k$ is obtained on
$D_+(l_0)$ from the ring map $k[t]\to S_{(l_0)}$, $t\mapsto l_1/l_0$, and
on $D_+(l_1)$ from $k[t^{-1}]\to S_{(l_1)}$, $t^{-1}\mapsto l_0/l_1$. That
these two affine descriptions agree on the overlap, and hence define a
morphism, is [lem-pc-linear-pair-morphism-gluing], as
[rem-ptr-pc-linear-pair-morphism-16] records.

*Import note.* The source's sentence ends and the definition closes without
the gluing clause; it is supplied above from the pointer remark, and
nothing else is added.

Unresolved dependencies: def:sc-p1-standard
