+++
kind = "proof"
of = "lemma-degree-zero-top-cohomology--1"
order = 1150008
uses = ["proposition-lattices-representations-normal-scheme"]
+++
Restriction of a global section to the base point is invariant under
monodromy. The monodromy equivalence is faithful, so this restriction
is injective; it is full, so every invariant vector is the value of a
morphism from the constant sheaf and hence of a global section.

Restriction intertwines the global Frobenius with the chosen Frobenius
lift. Any other element of degree one differs from that lift by an
element of $\pi_1(U)$, which acts trivially on the invariant vectors.
This proves the formula. On a smooth geometrically connected curve,
the required monodromy equivalence comes from Proposition
[proposition-lattices-representations-normal-scheme]. Finally,
`AlgebraicGeometry.WeilSheaf.cohomologyZeroEquiv` identifies
$H^0(U,\mathcal F)$ with $\Gamma(U,\mathcal F)$, compatibly with Frobenius.
