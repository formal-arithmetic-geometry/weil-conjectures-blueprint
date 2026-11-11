+++
id = "proposition-divisors-degree-g-open-chart--1"
kind = "proposition"
title = "Divisors of degree $g$ as an open chart (1)"
name_showing = false
order = 1540001
aliases = ["bp-r479-1"]
lean = ["AlgebraicGeometry.exists_representableBy_invertibleDirectImageToHilbert", "AlgebraicGeometry.hilbertToPicardNormalized_invertibleDirectImageToHilbert"]
uses = ["definition-compactification-refinement--1", "lemma-schematic-closure-uniqueness--1", "lemma-uniqueness-maps-dense-open--1", "theorem-chow-s-lemma-projective-form--2", "corollary-serre-duality-field-extension--2", "lemma-coherent-base-change-invertible-sheaves--1", "lemma-coherent-base-change-invertible-sheaves--3"]
+++
Let $C$ be a smooth proper geometrically integral curve of genus $g$ over
the separably closed field $k$, with $P\in C(k)$. Let $F$ be the subfunctor
of the Picard functor normalized along $P$ consisting of classes
$\mathcal L$ for which $Rf_{T,*}\mathcal L$ is an invertible sheaf in
degree $0$. Suppose that a $k$-scheme $H$ represents
$\operatorname{Hilb}^{g}_{C/k}$.

There are an open immersion $j:W\to H$ and a representation
$R:\operatorname{Hom}_k(-,W)\simeq F$ compatible with the zero-scheme map

$$
\Phi_T:F(T)\longrightarrow\operatorname{Hilb}^{g}_{C/k}(T),
\qquad
\mathcal L\longmapsto
Z\bigl(f_T^*f_{T,*}\mathcal L\longrightarrow\mathcal L\bigr).
$$

For every $a:T\to W$, the divisor $\Phi_T(R_T(a))$ is the one classified
by $j\circ a:T\to H$. The representation can be chosen so that the map
$W\to\operatorname{Pic}_{C/k}$ sends that divisor $D$ to
$\mathcal O(D)\otimes f_T^*(P_T^*\mathcal O(D))^{-1}$.
