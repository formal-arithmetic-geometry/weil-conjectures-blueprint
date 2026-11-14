+++
kind = "proof"
of = "dag-lem-pe-constructible-comparison-module-exact"
tags = ["sheaf-dag"]
uses = ["dag-lem-pe-coefficient-comparison-data"]
+++
1. Construct the pullback presentation of constant set sheaves by uniqueness of the constant-sheaf adjunction and the comparison adjunction. Verify its unit equation first at the terminal object and then on every object by naturality. Commute constant sheafification with the underlying-set functor. This gives a ring presentation whose unit is exactly constructibleComparisonRingMap. The module inverse-image unit comparison identifies the underlying additive sheaf of the intrinsic module pullback with the abelian-sheaf pullback. (uses [dag-lem-pe-coefficient-comparison-data], `lem-weil-pbc-module-inverse-image-unit-comparison`)
2. The site comparison is representably flat, so its abelian-sheaf inverse image preserves finite limits. The module forgetful functor reflects finite limits. Transport through the proved underlying additive-sheaf comparison to obtain finite-limit preservation of constructibleComparisonPullback. (uses `def-weil-pbc-site-comparison-morphism`, `lem-weil-pbc-module-inverse-image-unit-comparison`)
3. Repeat the source comparison-unit argument for AddCommGrpCat in universe max(v,u+1): the affine pro-etale Kan extension carries standard cofiltered presentations to filtered colimits, using preservation of limits by maps to etale schemes. Exactness of filtered colimits makes the restriction a sheaf. Density of the affine pro-etale basis and invertibility of the affine etale Kan-extension unit show that the abelian comparison unit is invertible. Its inverse image is therefore faithful. Transport through AsSmall sheaf equivalences using uniqueness of left adjoints; then the underlying additive-sheaf comparison reflects equality of module morphisms. (uses `det-pe-classical-sheaves-modules`, `def-weil-pbc-site-comparison-morphism`, `lem-weil-pbc-module-inverse-image-unit-comparison`)

Proof dependencies not drawn: `lem-weil-pbc-module-inverse-image-unit-comparison`, `def-weil-pbc-site-comparison-morphism`, `det-pe-classical-sheaves-modules`.
