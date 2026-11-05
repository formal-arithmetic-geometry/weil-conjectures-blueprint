+++
kind = "proof"
of = "proposition-additivity-trace-classes--2"
order = 942005
uses = ["proposition-additivity-trace-classes--1", "definition-pushforward-correspondence", "lemma-external-duality-trace-morphism", "proposition-six-operations-dctf"]
+++
The counit $\epsilon:K_U\to K$ and the unit $\eta:K\to K_Z$ extend
to a distinguished localization triangle
$K_U\to K\to K_Z\to K_U[1]$, by
`AlgebraicGeometry.ProEtale.CondensedRing.exists_distTriang_pointComplι_rationalPoint`.
The open coefficient map commutes with the counit by
`AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.graphOpenPieceCoeff_comp_counit`.
The closed coefficient map commutes with the unit by
`AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.upperStar_map_unit_comp_graphClosedPieceCoeff`.
After the identification $\id_X^!\simeq\id$, these are the two
compatibility identities in [proposition-additivity-trace-classes--1].

Its four vanishing assumptions follow from the disjointness of $U$ and
$\{x\}$. For the first three, the Künneth–Verdier isomorphism and the
tensor–hom and exceptional adjunctions identify morphisms into
$K_Z\boxtimes\mathbb D_XK_U$ with morphisms
$Rp_{1!}(p_2^*K_U\otimes^{\mathbf L}T)\to K_Z$.
Adjunction along $x$ reduces these to the restriction of the source to
$x$. For $T=Rc_!\Qbarl_X$, the projection formula and $h\circ x=x$
reduce that restriction to $x^*K_U=0$; for the other two sources,
the projection formula reduces it to $x^*K_U=0$ and
$K_U\otimes^{\mathbf L}\mathbb D_XK_Z=0$, respectively. The same
vanishings hold after the shift needed for degree $-1$.

Finally, pulling $K_U\boxtimes\mathbb D_XK_Z$ back along the diagonal
gives $K_U\otimes^{\mathbf L}\mathbb D_XK_Z=0$, so adjunction gives
the fourth vanishing. These are the lemmas
`AlgebraicGeometry.ProEtale.CondensedRing.eq_zero_of_lowerShriek_graph`,
`AlgebraicGeometry.ProEtale.CondensedRing.eq_zero_of_externalProduct_openPiece`,
`AlgebraicGeometry.ProEtale.CondensedRing.eq_zero_of_externalProduct_closedPiece`
and
`AlgebraicGeometry.ProEtale.CondensedRing.eq_zero_of_externalProduct_shift_to_diag`.
Apply [proposition-additivity-trace-classes--1] and interchange the two
summands.
