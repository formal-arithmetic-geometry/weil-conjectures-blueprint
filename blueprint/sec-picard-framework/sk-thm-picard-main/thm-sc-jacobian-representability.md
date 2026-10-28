+++
id = "thm-sc-jacobian-representability"
kind = "theorem"
title = "The Jacobian over a separably closed field"
order = 862
uses = ["def-pc-genus", "def-pc-geometrically-irreducible", "def-pc-smooth-projective-curve", "def-sc-abelian-variety", "def-sc-jacobian", "def-sc-pic0", "def-sc-picard-functor", "lem-pc-curves-are-sc", "lem-pc-picard-functor-agrees-sc", "lem-sc-abelian-variety-projective", "lem-sc-pic-tangent-space", "thm-sc-theorem-of-the-base"]
lean = ["AlgebraicGeometry.exists_jacobian", "AlgebraicGeometry.exists_jacobian_baseChange"]
+++
Let $k$ be a separably closed field and let $C$ be a
$k$-scheme which is proper and smooth of relative dimension $1$ over $k$
and geometrically integral,
of genus $g=g(C)=\dim_kH^1(C,\mathcal O_C)$ ([def-pc-genus]). There is
an abelian variety $J_C$ over
$k$, the *Jacobian* of $C$ in the sense of [def-sc-jacobian], of dimension $g$, together
with a natural isomorphism of group-valued functors

$$
\operatorname{Pic}^0_{C/k}\cong h_{J_C},
$$

where $\operatorname{Pic}^0_{C/k}$ is the degree-zero part of the
Picard functor; its $k$-points are the
invertible modules of degree $0$ on $C$, and for algebraically closed
$k$ they are the $\operatorname{Pic}^0(C)$ of [def-sc-pic0], so that
$\operatorname{Pic}^0(C)=J_C(k)$ canonically in that case. Moreover $J_C$
is compatible with base change along extensions of separably closed fields:
$J_{C_{k'}}\cong(J_C)_{k'}$ for $k\subseteq k'$ separably closed.
