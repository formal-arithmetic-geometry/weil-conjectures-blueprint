+++
kind  = "proof"
of    = "cor-amb-affine-space-adjunction"
+++
Let $j:\mathbf A^1_S\hookrightarrow\mathbf P^1_S$.
The definition in [def-amb-etale-compact-support]
is $Rp_{1!}=Rq_*j_!$. By
[thm-amb-p1-adjunction], [lem-amb-etale-adjoint-locality],
its right adjoint is $j^*q^*(1)[2]=p_1^*(1)[2]$.
For $d=0$ the assertion is the identity adjunction.
The composition of compact-support functors is
[lem-amb-etale-compact-comparisons]. For $d>0$, factor the affine-space projection into
$d$ successive affine-line projections. The right
adjoint of the composite is the reversed composite of
their right adjoints, by their Hom adjunction bijections.
The twists add by [def-coefficient-twists-detailed], giving
$p_d^*(d)[2d]$.
