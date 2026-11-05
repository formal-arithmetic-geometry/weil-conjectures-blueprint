+++
kind = "proof"
of = "proposition-forgetting-supports-composition--1"
order = 519004
uses = ["proposition-construction-independence-rf-shriek"]
+++
The unit of $j_!\dashv j^*$ is an isomorphism. Transpose its inverse
under $j^*\dashv Rj_*$; the formula for the adjunction gives the displayed
map $j_!K\to Rj_*K$. This is
`AlgebraicGeometry.Etale.derivedOpenImmersionLowerShriekToLowerStar_app`.
Apply $Rp_*$ and then the ordinary composition isomorphism, using
$f=pj$. The unit, its inverse, and the composition isomorphism are natural,
so this constructs a natural transformation. For the chosen
compactification, the agreement of the two formulas for the ordinary
composition map is
`AlgebraicGeometry.Etale.rightDerivedLowerShriekToLowerStarComp_comp_eq`.
