+++
id = "cor-amb-affine-space-adjunction"
kind = "theorem"
title = "Affine-space ambient adjunction"
order = 5619
tags = ["latex:corollary"]
lean = ["AlgebraicGeometry.Etale.affineSpace.adjunction"]
uses = ["def-coefficient-twists", "def-amb-etale-compact-support", "thm-amb-p1-adjunction", "lem-amb-etale-adjoint-locality", "lem-amb-etale-compact-comparisons"]
+++
For $p_d:\mathbf A^d_S\to S$, on the entire ordinary derived categories of
étale $A$-module sheaves,
$$
Rp_{d!}\dashv p_d^*(d)[2d].
$$

## Proof

Let $j:\mathbf A^1_S\hookrightarrow\mathbf P^1_S$. The definition in
[def-amb-etale-compact-support] is $Rp_{1!}=Rq_*j_!$. By
[thm-amb-p1-adjunction] and [lem-amb-etale-adjoint-locality], its right
adjoint is $j^*q^*(1)[2]=p_1^*(1)[2]$. For $d=0$ the assertion is the
identity adjunction.

The composition of compact-support functors is
[lem-amb-etale-compact-comparisons]. For $d>0$, factor the affine-space
projection into $d$ successive affine-line projections. The right adjoint of
the composite is the reversed composite of their right adjoints, by their
Hom adjunction bijections. The twists add, giving $p_d^*(d)[2d]$.

Unresolved dependencies: def:sbc-affine-space, def:weil-pbc-derived-categories
