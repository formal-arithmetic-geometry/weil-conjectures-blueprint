+++
kind = "proof"
of = "theorem-trace-formula-euler-product--6"
order = 1036012
uses = ["proposition-construction-independence-rf-shriek", "proposition-forgetting-supports-composition"]
+++
Write the proper structure morphism as a compactification $a=gj$.
The open immersion $j$ is then also proper, hence closed. Thus
$j_!\simeq j_*$ and

$$
Ra_!K\simeq Rg_*(j_!K)\simeq Rg_*(j_*K)\simeq Ra_*K.
$$

These identifications preserve the Weil structure; in Lean they form
`AlgebraicGeometry.WeilComplex.derivedLowerShriekObjIsoOfIsProper`.
Apply the $i$-th cohomology-sheaf functor and then global sections over
$\operatorname{Spec}\overline{\mathbf F}_q$. This gives the required
Frobenius-equivariant isomorphism. Conjugate Frobenius operators have
the same characteristic polynomial.
