+++
id = "proposition-jacobian-over-ground-field"
kind = "proposition"
title = "The Jacobian over the ground field"
order = 1562
lean = ["AlgebraicGeometry.exists_jacobian_descent", "AlgebraicGeometry.nonempty_representableBy_picardFunctorDegree_baseChange", "AlgebraicGeometry.exists_jacobian_galoisAction"]
uses = ["definition-compactification-refinement", "definition-abelian-variety", "lemma-abelian-variety-commutative", "definition-tate-module", "proposition-integral-tate-module", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
Let $C_0/k$ be a smooth proper geometrically connected curve of genus
$g$, and put $C=C_0\times_k\bar k$.
There is an abelian variety $J_0/k$ of dimension $g$ representing the
degree-zero relative Picard fppf sheaf of $C_0$. For every field
extension $k'/k$, the base change $J_0\times_kk'$ represents the degree-zero
Picard sheaf of $C_0\times_kk'$; in particular $J_0\times_k\bar k$ represents
$\operatorname{Pic}^0_{C/\bar k}$, and the canonical identification

$$
J_0(\bar k)=\operatorname{Pic}^0(C)
$$

is Galois-equivariant.
