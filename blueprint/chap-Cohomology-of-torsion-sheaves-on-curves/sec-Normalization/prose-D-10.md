+++
id = "prose-D-10"
kind = "hidden"
title = "Normalization (1)"
order = 1598
+++
So far we have computed with constant coefficients on smooth curves,
whereas Theorem [theorem-cohomology-curves] concerns arbitrary curves of
dimension at most one and arbitrary torsion sheaves. Two reductions close
the gap: normalization and removing finitely many points. Both rest
on Lemma [lemma-sheaves-finite-support-finite-morphisms], which says
that a sheaf supported on finitely many points has no higher cohomology.
Hence passing between a curve, its normalization and a dense open subset
changes cohomology only in degrees zero and one, and only by finite groups
that do not change under field extension.

For example, let $C:y^2=x^3+x^2$ be the nodal cubic. Its normalization
$\mathbf A^1\to C$ has two points over the node. For $M=\mathbf Z/n$ the
normalization sequence of
Lemma [lemma-normalization-constant-sheaf] has cokernel
$M^2/\Delta M\simeq M$ at the node. If $n$ is invertible in $k$, then
$H^1(\mathbf A^1,\mathbf Z/n)=0$, and the long exact sequence gives
$H^1(C,\mathbf Z/n)\simeq\mathbf Z/n$. This is the analogue of the loop
created by the node.
