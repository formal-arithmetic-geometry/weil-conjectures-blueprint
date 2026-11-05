+++
kind = "proof"
of = "proposition-proper-direct-image-constructible-complexes--2"
order = 425005
uses = ["proposition-integral-constructibility-criterion", "theorem-results-from-etale-theory", "theorem-nagata-s-compactification-theorem", "proposition-proper-direct-image-finite-coefficients", "corollary-open-direct-image-over-field"]
+++
First consider a constructible $\mathcal O_E$-sheaf $F$ in degree zero. The
integral finiteness results
`AlgebraicGeometry.ProEtale.CondensedRing.PadicIntegersRingObj.finiteTypeDirectImage_single_boundedAbove`
and
`AlgebraicGeometry.ProEtale.CondensedRing.PadicIntegersRingObj.finiteTypeDirectImage_single_constructible`
give an upper bound for $Rp_*F$ and constructibility of all its cohomology
sheaves. Their integral input uses derived completeness and the residue-field
criterion [proposition-integral-constructibility-criterion]. The finite-coefficient
finiteness input factors the morphism through a compactification
[theorem-nagata-s-compactification-theorem] and combines proper finiteness
[proposition-proper-direct-image-finite-coefficients] with open direct-image
finiteness [corollary-open-direct-image-over-field]. The cohomological bound is
the finite-coefficient bound [theorem-results-from-etale-theory]. Left exactness
of $p_*$ gives the lower bound zero.

Now apply finite truncation dévissage to $K$. The inverse image under $Rp_*$ of
the triangulated subcategory of bounded constructible complexes is triangulated,
and it contains every constructible sheaf in degree zero. It therefore contains
$K$. This is the argument of
`boundedConstructible_rightDerivedLowerStar_obj_of_single`; it does not use
properness.
