+++
kind = "proof"
of = "dag-lem-pe-coefficient-stratified-continuity"
tags = ["sheaf-dag"]
uses = ["dag-lem-pe-coefficient-fp-local-system-origin", "dag-lem-pe-coefficient-stratified-essential-image", "dag-lem-pe-coefficient-comparison-continuity", "dag-det-pe-classical-definition-continuity-map"]
+++
1. Restrict the intrinsic module to constant scalars, obtaining E. For each stratum and every object, retain its covering sieve, constant module and local isomorphism. Noetherianity upgrades the finite module to a finitely presented one, by Module.finitePresentation_of_finite. Apply coefficientFpLocalSystem_essImage on that stratum. (uses [dag-lem-pe-coefficient-fp-local-system-origin], `lem-sc-noetherian-finite-module-finite-presentation`)
2. Apply coefficientFixed_essImage_of_stratification to E and these stratum origins. Obtain an etale module G and a sheaf isomorphism from its canonical fixed-scalar comparison inverse image to E. This uses the same finite-stratification induction as the original plan, with coefficients in the independent universe. (uses [dag-lem-pe-coefficient-stratified-essential-image])
3. For the given affine presentation, coefficientFixedComparison_isColimit makes the restriction cocone of the comparison inverse image of G a colimit. The canonical colimit descent map is therefore invertible. Whisker the sheaf isomorphism with AsSmall.up.op. Naturality of continuityMap identifies the two maps through the induced colimit isomorphism and the component isomorphism at the vertex. Cancel the induced colimit isomorphism to obtain invertibility of the requested continuity map. (uses [dag-lem-pe-coefficient-comparison-continuity], [dag-det-pe-classical-definition-continuity-map])

Proof dependencies not drawn: `lem-sc-noetherian-finite-module-finite-presentation`.
