+++
id = "lem-weil-pbc-polynomial-presentation-height-field-extension"
kind = "lemma"
title = "Height difference in a polynomial presentation after field extension"
lean = ["AlgebraicGeometry.polynomial_presentation_height_field_extension"]
order = 2017
+++
Let $K/k$ be a field extension, $S$ a commutative $k$-algebra, and
$f\colon k[x_1,\dots,x_n]\to S$ a surjective homomorphism of $k$-algebras. Then there is a
surjective ring homomorphism $g\colon K[x_1,\dots,x_n]\to S\otimes_kK$ such that for every
prime $Q$ of $S\otimes_kK$, with contraction $q$ to $S$,

$$
\operatorname{ht}\bigl(f^{-1}(q)\bigr)+\operatorname{ht}(Q)=\operatorname{ht}\bigl(g^{-1}(Q)\bigr)+\operatorname{ht}(q).
$$
