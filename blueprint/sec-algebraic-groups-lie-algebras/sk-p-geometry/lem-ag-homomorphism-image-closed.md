+++
id = "lem-ag-homomorphism-image-closed"
kind = "lemma"
title = "The image of a homomorphism of algebraic groups is closed"
lean = ["AlgebraicGeometry.isClosed_range_of_isMonHom", "AlgebraicGeometry.isClosed_range_of_isMonHom_of_isAlgClosed", "AlgebraicGeometry.GeneralLinearGroup.RationalHom.mem_range_points_iff", "AlgebraicGeometry.GeneralLinearGroup.mem_of_mem_closure_of_isConstructible"]
order = 3687
uses = ["lem-sc-translation-automorphism", "lem-wf-affine-constructible-open", "lem-wf-affine-nullstellensatz-vanishing", "lem-wf-affine-product-reduced"]
+++
Let $f:G\to K$ be a homomorphism of group schemes over an algebraically
closed field $L$, where $G$ is of finite type and $K$ is locally of
finite type over $L$. Then the image $f(G)$ is a closed subset of $K$.

*Complement.* Let $G\subseteq\operatorname{GL}(V)$ and
$K\subseteq\operatorname{GL}(W)$ be closed reduced matrix groups over
$L$, and let $\varphi:G\to K$ be a regular homomorphism, that is, a
morphism of varieties which is a group homomorphism on $L$-points. Then
$S=\varphi(G(L))$ is a closed subgroup of $K(L)$: it is the set of
$L$-points of a closed subgroup of $K$, which we equip with its reduced
structure.
