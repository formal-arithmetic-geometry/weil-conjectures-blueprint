+++
kind = "proof"
of = "corollary-torsion-jacobian-field-extension--2"
order = 1558008
uses = ["proposition-multiplication-n", "theorem-picard-scheme-jacobian-over-separably"]
+++
By [proposition-multiplication-n], $A[n]$ is finite étale over
$k$. Apply `AlgebraicGeometry.bijective_toUnit_comp`: on coordinate
rings the map on points is composition with $k\hookrightarrow k'$;
it is injective, and both sets have cardinality equal to the rank
of $A[n]$.

For the human statement, take $A=J(C)$. The base-change comparison
for the degree-zero Picard functor in
[theorem-picard-scheme-jacobian-over-separably] identifies
$J(C)_{k'}$ with $J(C_{k'})$; its functor-level Lean statement is
`AlgebraicGeometry.nonempty_picardFunctorDegree_iso_of_isPullback`.
The map on torsion points respects the group laws, so its
bijectivity gives the asserted group isomorphism.
