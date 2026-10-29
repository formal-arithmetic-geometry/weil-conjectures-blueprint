+++
id = "det-picard-main-jacobian"
kind = "lemma"
title = "The Jacobian of a geometric curve: points, tangent space, base change"
lean = ["AlgebraicGeometry.exists_jacobian", "AlgebraicGeometry.nonempty_tangentSpaceAt_linearEquiv_H_one", "AlgebraicGeometry.nonempty_picardFunctor_iso_of_isPullback", "AlgebraicGeometry.nonempty_representableBy_picardFunctorDegree_baseChange", "AlgebraicGeometry.exists_jacobian_baseChange"]
order = 865
uses = ["det-picard-main-degree", "det-picard-main-geometry", "def-pc-picard-functor"]
+++
In the situation of [det-picard-main-geometry], put
$J(C)=\underline{\operatorname{Pic}}^0_{C/k}$. Then:

1. $J(C)$ is an abelian variety of dimension $g$ (a smooth proper
connected group scheme over $k$; it is commutative);
1. $J(C)(k)=\operatorname{Pic}^0(C)$, the group of invertible sheaves of
degree $0$ on $C$;
1. the tangent space at the unit is $T_0J(C)\cong H^1(C,\cO_C)$ as
$k$-vector spaces;
1. for every field extension $K/k$, $\underline{\operatorname{Pic}}_{C/k}\times_kK$
represents $\operatorname{Pic}_{C_K/K}$, its degree components are
$\underline{\operatorname{Pic}}^d_{C/k}\times_kK=\underline{\operatorname{Pic}}^d_{C_K/K}$,
and $J(C)\times_kK=\underline{\operatorname{Pic}}^0_{C_K/K}$ (which is
$J(C_K)$ when $K$ is algebraically closed).
