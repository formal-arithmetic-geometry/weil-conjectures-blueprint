+++
kind = "proof"
of = "proposition-proper-direct-image-constructible-complexes--12"
order = 425025
uses = ["proposition-proper-direct-image-constructible-complexes--4", "proposition-proper-direct-image-constructible-complexes--10", "proposition-proper-direct-image-constructible-complexes--11", "lemma-integral-models", "lemma-change-coefficients-direct-image", "proposition-six-operations-change-coefficients"]
+++
Choose integral models $K_0,M_0$ over a common finite extension
$E\subset\overline{\mathbf Q}_\ell$. Apply
[proposition-proper-direct-image-constructible-complexes--10] to these models.
Pass first from $\mathcal O_E$ to $E$ by
[proposition-proper-direct-image-constructible-complexes--11], and then from $E$
to $\overline{\mathbf Q}_\ell$ by the same projection-map comparison.
Constructibility makes the required tensor products bounded below; the
scalar/direct-image comparisons therefore apply
[lemma-change-coefficients-direct-image]. This is
`AlgebraicGeometry.ProEtale.CondensedRing.isIso_projectionMap_padicAlgClRingObj_of_integral`.

Finally, the restricted projection morphism maps to the ambient one under the
fully faithful inclusion of $\Dbc(Y,\overline{\mathbf Q}_\ell)$. This follows
from `CategoryTheory.Adjunction.ι_map_projectionMorphism_restrictFullyFaithful`.
The inclusion reflects isomorphisms, which proves the stated formula in
$\Dbc$.
