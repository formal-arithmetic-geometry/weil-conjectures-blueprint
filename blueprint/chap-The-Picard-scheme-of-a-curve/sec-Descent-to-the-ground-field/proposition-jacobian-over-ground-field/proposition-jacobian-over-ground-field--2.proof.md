+++
kind = "proof"
of = "proposition-jacobian-over-ground-field--2"
order = 1562008
uses = ["definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
The identifications $X'\times_{k'}T\simeq X\times_kT$ identify the
Picard presheaves. They preserve the fibrewise degree: after pullback
to a field-valued point of $T$, the two invertible sheaves are
identified, and degree is invariant under the resulting base change.
Thus the degree-$d$ subfunctors agree. Sheafification commutes with
restriction to schemes over $k'$, giving the canonical isomorphism
`AlgebraicGeometry.picardFunctorDegreeIsoOfIsPullback`.

If $r$ is a representation by $J_0$, the adjunction between viewing a
$k'$-scheme as a $k$-scheme and base change to $k'$ makes
$J_0\times_kk'$ represent the restricted functor. This is
`CategoryTheory.Functor.RepresentableBy.ofAdjunction`. Compose with the
canonical isomorphism at $d=0$ to obtain the asserted representation.
