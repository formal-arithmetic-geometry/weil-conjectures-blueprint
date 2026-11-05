+++
kind = "proof"
of = "lemma-additivity-open-subscheme-complement--1"
order = 1002003
uses = ["proposition-extension-zero-restriction-closed-subscheme", "proposition-composition-base-change-rf-shriek"]
+++
The pullback structure is the composite
$e_U^*j_0^*K\simeq j_0^*e_X^*K\xrightarrow{j_0^*\phi}j_0^*K$,
and similarly for $i_0$. The pushforward structures use compact-support
base change for the squares formed by the automorphisms; these squares
are cartesian. This is the construction of
`AlgebraicGeometry.ProEtale.CondensedRing.weilUpperStar` and
`AlgebraicGeometry.ProEtale.CondensedRing.weilLowerShriek`.

The underlying localization triangle follows from open–closed
recollement, as in [proposition-extension-zero-restriction-closed-subscheme].
The counit and unit commute with the structures by
`AlgebraicGeometry.ProEtale.CondensedRing.counit_comm_weilStr` and
`AlgebraicGeometry.ProEtale.CondensedRing.unit_comm_weilStr`.
To check the connecting map, use
`AlgebraicGeometry.ProEtale.CondensedRing.map_comp_connecting_eq_of_isCompl`:
the morphism completing the first two squares is unique, since every
map from $(e_X^*Rj_{0!}j_0^*K)[1]$ to $Ri_{0*}i_0^*K$ vanishes by
disjointness of the open and closed supports.
Transporting across $Ri_{0!}\simeq Ri_{0*}$ gives the asserted
equivariant triangle.

For the stalk traces, exact pullback commutes with cohomology sheaves,
and this comparison respects their Weil structures
(`AlgebraicGeometry.ProEtale.CondensedRing.nonempty_homologyFunctor_weilUpperStar_iso`).
The stalk comparison identifies the local operators up to isomorphism
on each cohomology sheaf, so their traces agree degree by degree.
Taking the alternating sum gives both equalities.
