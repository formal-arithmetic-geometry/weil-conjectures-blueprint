+++
kind = "proof"
of = "proposition-composition-base-change-rf-shriek--3"
order = 516004
uses = ["proposition-construction-independence-rf-shriek", "proposition-comparison-immersions"]
+++
Compute composition using the triangle of compactifications with an
identity on the left, and then with an identity on the right. In either
triangle the exchange and composition maps reduce to the identity maps for
proper direct image and extension by zero. Rewrite the chosen composition
isomorphism using this triangle, and express $R(\mathrm{id})_!\simeq
R(\mathrm{id})_*$ through the identity compactification. The comparison maps
to and from that compactification cancel by their cocycle condition. The
remaining composite is the identity. Lean carries this out in
`AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekComp_padicAlgCl_id_left'`
and
`AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekComp_padicAlgCl_id_right'`.
