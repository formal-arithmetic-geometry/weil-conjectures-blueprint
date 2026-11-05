+++
kind = "proof"
of = "lemma-passing-schematic-closure--1"
order = 1412003
uses = ["proposition-extension-zero-restriction-closed-subscheme", "proposition-proper-direct-image-constructible-complexes"]
+++
First form the restriction comparison $j'_!K\to Lh^*j_!K$ using the unit
of $j_!\dashv Lj^*$, the identity $Lj^*\simeq Lj'^*Lh^*$, and the counit
of $j'_!\dashv Lj'^*$. It is an isomorphism after restriction to $X$ by
the triangle identity. On the closed complement of $X$ in $Z$, both
sides vanish because the square is cartesian. The localization sequence
of [proposition-extension-zero-restriction-closed-subscheme] therefore
shows that it is an isomorphism. This is
`AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleOpenImmersionLowerShriekRefinement`.

It remains to check the unit
$j_!K\to Rh_*Lh^*j_!K$. Restriction to $X$ identifies it, by proper base
change, with the unit for the identity morphism, hence with an
isomorphism. On the closed complement $C=\overline X\setminus X$, the
source vanishes. Proper base change along $C\hookrightarrow\overline X$
identifies the restriction of the target with direct image from
$Z\times_{\overline X}C$; the complex there vanishes since its image in
$\overline X$ misses $X$. Thus the unit is an isomorphism on both pieces,
and hence globally. Lean packages this argument in
`AlgebraicGeometry.ProEtale.CondensedRing.isIso_unit_app_openImmersionLowerShriek`.

Apply [proposition-proper-direct-image-constructible-complexes] for the
chosen coefficient ring to obtain the two base-change isomorphisms.
Composing the unit with $Rh_*$ of the inverse restriction comparison
gives $\rho_K$ and proves the claim.
