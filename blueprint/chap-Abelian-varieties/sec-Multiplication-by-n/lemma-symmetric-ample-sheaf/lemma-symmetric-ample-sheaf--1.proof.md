+++
kind = "proof"
of = "lemma-symmetric-ample-sheaf--1"
order = 1498002
uses = ["proposition-cartier-s-theorem", "lemma-connected-components-images-homomorphisms"]
+++
Base change to an algebraic closure $\overline k$ of $k$. Over this field,
first reduce to smooth group schemes: in characteristic zero use
[proposition-cartier-s-theorem], and in positive characteristic pass to the
reduced subgroup scheme and descend sections with affine non-vanishing
loci using a power of Frobenius.

For a smooth group scheme, the decomposition into finitely many translates
of its irreducible identity component
[lemma-connected-components-images-homomorphisms] reduces the construction
of an ample family to the smooth irreducible case. There, translates of
divisors with affine complement yield an invertible sheaf with finitely
many global sections whose non-vanishing loci are affine and cover the
group scheme. Since a group scheme over a field is separated, these
sections give an immersion into projective space.

Finally, descend quasi-projectivity along $\overline k/k$, using
`AlgebraicGeometry.exists_isImmersion_projectiveSpace_of_pullback`: spread
the projective coordinates with affine inverse images of the standard
opens to a finite extension of $k$, then take norms to obtain a coordinate
cover over $k$. This cover again gives an immersion into projective space.
