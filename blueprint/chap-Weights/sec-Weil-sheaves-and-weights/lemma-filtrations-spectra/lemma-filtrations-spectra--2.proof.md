+++
kind = "proof"
of = "lemma-filtrations-spectra--2"
order = 1067007
uses = ["lemma-filtrations-spectra--1"]
+++
Apply the identity for the multiset of roots of a product,
`Polynomial.roots_prod`, to [lemma-filtrations-spectra--1]. Each
characteristic polynomial is monic and hence nonzero, so its
hypothesis is satisfied and multiplicities add.

In the proof of
`AlgebraicGeometry.WeilGroup.isPunctuallyPure_subquotient_of_isReal`,
Lean forms the direct sum $S$ of the successive quotient
representations. The filtration identity and
`Representation.charpoly_directSum` show that every group element
has the same characteristic polynomial on $S$ and on the original
representation. Applying `Polynomial.roots_prod` to this direct sum
gives the eigenvalue union as the local fact `heigS`. There is no
separate named declaration for the filtration eigenvalue statement.
