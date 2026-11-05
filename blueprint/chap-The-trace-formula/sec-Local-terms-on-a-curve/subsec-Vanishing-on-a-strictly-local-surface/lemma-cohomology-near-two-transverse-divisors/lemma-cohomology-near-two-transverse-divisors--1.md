+++
id = "lemma-cohomology-near-two-transverse-divisors--1"
kind = "lemma"
title = "Vanishing at the corner and local constancy along the punctured divisor"
order = 973001
aliases = ["bp-r296-1"]
lean = ["AlgebraicGeometry.Scheme.TransverseCorner.isFiniteLocallyConstantSheaf_homology_boundaryComplex", "AlgebraicGeometry.Scheme.TransverseCorner.isZero_leftDerivedUpperStar_boundaryComplex"]
+++
Let $k$ be an algebraically closed field and let $\ell$ be a prime
invertible in $k$. Let $X$ be a regular, locally noetherian $k$-scheme
which is a smooth surface, or a cofiltered limit of smooth surfaces
with affine étale transition maps. Let $D_1,D_2$ be regular divisors
whose scheme-theoretic intersection is the reduced point $z$ and is a
regular closed subscheme of codimension two in $X$. Write

$$
j:X-D_2\hookrightarrow X,\qquad
j':X-(D_1\cup D_2)\hookrightarrow X-D_2.
$$

Let $A$ be a finite commutative ring in which $\ell$ is nilpotent,
and let $N$ be a bounded complex of étale sheaves of $A$-modules on
$X-(D_1\cup D_2)$. Assume that, for each $n$, there is a finite étale
Galois cover with group a finite $\ell$-group on which $H^n(N)$ becomes
the constant sheaf associated to a finite $A$-module. Put $M=Rj_*j'_!N$.
Then $M_{\bar z}=0$ for every geometric point $\bar z$ over $z$, and
$H^n(M|_{D_2-z})$ is finite locally constant for every $n\in\mathbf Z$.
