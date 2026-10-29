+++
id = "lem-pc-twist-cocycle"
kind = "lemma"
title = "The cocycle rule for the transition units of the twists"
lean = ["AlgebraicGeometry.ProjectiveSpace.transitionUnit_mul_transitionUnit"]
order = 627
uses = ["def-pc-proj", "def-pc-projective-space-twist"]
+++
Let $A$ be a commutative ring, $n\ge0$ and
$P=\operatorname{Proj}(A[x_0,\ldots,x_n])$ with standard affine opens
$U_i=D_+(x_i)$, and let $d\in\mathbf Z$
([def-pc-projective-space-twist]). Then the units
$u_{ij}:=(x_i/x_j)^d\in\Gamma(U_i\cap U_j,\mathcal O_P^*)$ satisfy
$u_{ij}u_{jk}=u_{ik}$ on $U_i\cap U_j\cap U_k$, for all
$i,j,k\in\{0,\ldots,n\}$.
