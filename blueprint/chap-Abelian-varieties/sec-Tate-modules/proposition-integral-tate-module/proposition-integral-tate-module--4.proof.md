+++
kind = "proof"
of = "proposition-integral-tate-module--4"
order = 1509007
uses = ["proposition-multiplication-n"]
+++
Precomposition with $\operatorname{Spec}\sigma^{-1}$ is inverse to
precomposition with $\operatorname{Spec}\sigma$. Precomposition
preserves the group law on points, giving the group automorphism
`AlgebraicGeometry.IsAbelianVariety.geometricPointsAddEquiv`.

For the second assertion, [proposition-multiplication-n] makes
$A[m]$ finite étale. Apply
`AlgebraicGeometry.bijective_toUnit_comp`: identify points with
$k$-algebra homomorphisms from the coordinate ring of $A[m]$.
Composition with $k\to k'$ is injective, and both sets of
homomorphisms have cardinality equal to the rank of $A[m]$.
It is therefore bijective.
