+++
id = "sk-thm-picard-f-representable"
kind = "proposition"
title = "Divisors of degree $g$ as an open chart"
order = 818
uses = ["sk-def-av-jacobian", "sk-def-av-pic", "sk-prop-picard-pic-split", "sk-thm-picard-perfect", "sk-thm-picard-hilb-curves", "sec-nagata-compactification", "sk-def-picard-pic", "sec-abelian-varieties"]
lean = ["AlgebraicGeometry.isRepresentable_picardFunctorInvertibleDirectImage", "AlgebraicGeometry.exists_representableBy_invertibleDirectImageToHilbert", "AlgebraicGeometry.hilbertPresheaf_curve_representable"]
tags = ["sketch"]
+++
Let $C/k$ be a smooth projective geometrically connected curve of genus
$g=\dim_kH^1(C,\cO_C)$, and let $H_g$ be its Hilbert scheme of points of
degree $g$, with universal divisor $D_g$ ([sk-thm-picard-hilb-curves]).
Assume that $C(k)$ contains a point $P$ ($k$ any field), and describe
$\operatorname{Pic}_{C/k}$ by rigidified invertible sheaves as in
[sk-prop-picard-pic-split]. Define a subfunctor
$F\subset\operatorname{Pic}_{C/k}$ by requiring

$$
Rf_{T,*}\cL\simeq\cN[0]
\quad\text{for some invertible }\cN\text{ on }T.
$$

Here $\cN$ may be any invertible sheaf on $T$, trivial or not.
[sk-thm-picard-perfect] shows that $F\subset\operatorname{Pic}_{C/k}$ is
representable by open immersions ([det-lem-picard-f-open]).

Then the functor $F$ is represented by an open subscheme $W\subset H_g$.
The morphism $W\to\operatorname{Pic}_{C/k}$ associates to a divisor its
rigidified invertible sheaf. Consequently, $F$ is smooth of dimension
$g$.
