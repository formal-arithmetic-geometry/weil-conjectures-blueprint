+++
kind = "proof"
of = "theorem-picard-scheme-jacobian-over-separably--5"
order = 1549010
uses = ["lemma-coherent-base-change-invertible-sheaves"]
+++
For a scheme $T$ over $S'$, the fibre products
$X'\times_{S'}T$ and $X\times_S T$ are canonically isomorphic. Pullback
along this isomorphism identifies their Picard groups naturally in
$T$. The fppf coverings of $T$ agree in the two slice sites, so this
identification passes to the sheafifications. Lean uses
`AlgebraicGeometry.picardPresheafIsoOfIsPullback` and
`AlgebraicGeometry.overMapOpCompSheafifyIso`.

For an extension $K/k$, the same fibre-product identification
preserves degree, computed from the Euler characteristics on each
fibre. In Lean this is
`AlgebraicGeometry.pic_map_pullbackIsoOfIsPullback_mem_picardSubfunctorDegree_iff`.
Restrict the Picard presheaf isomorphism to the classes of fibrewise
degree $d$, then sheafify. This gives
`AlgebraicGeometry.picardFunctorDegreeIsoOfIsPullback`.

A representation of a functor restricts to a representation by the
base-changed scheme, using the adjunction between composition with
$S'\to S$ and pullback. In Lean the operation is
`CategoryTheory.Functor.RepresentableBy.ofAdjunction` applied to
`CategoryTheory.Over.mapPullbackAdj`. Compose with the functor
isomorphisms above and use uniqueness of representing objects.
Taking $d=0$ gives the assertion for $J(C)$.
