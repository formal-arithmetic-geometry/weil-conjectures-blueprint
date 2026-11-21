+++
kind = "proof"
of = "dag-lem-pe-coefficient-origin-closed-direct-image"
tags = ["sheaf-dag"]
uses = ["dag-lem-pe-coefficient-comparison-continuity", "dag-lem-pe-coefficient-classical-module-origin"]
+++
1. Restrict scalars along the constant-ring sheafification unit. The public equivalence `lem-ctf-finite-comparison-model-realization` identifies intrinsic modules with fixed-scalar sheaves. Prove privately that comparison commutes with this equivalence: the ring-map adjunction equation identifies constant scalar actions on direct images, and uniqueness of left adjoints gives the inverse-image square. Fix an etale antecedent of H. (uses `lem-ctf-finite-comparison-model-realization`)
2. Given any affine etale presentation over X, pull its diagram and cone back along i. Each stage and the vertex remain affine because their projections to the original affine schemes are closed immersions, hence affine. The stage structure morphisms remain etale by base change. The cone is still a limit in the over-category since base change is a right adjoint. Apply [dag-lem-pe-coefficient-comparison-continuity] to the antecedent over Z. Its section cocone is exactly the section cocone of the direct image on the original presentation over X. Thus the direct image has invertible continuity maps. Naturality transports this through the chosen isomorphism to H. (uses [dag-lem-pe-coefficient-comparison-continuity])
3. The counit of the constant-scalar equivalence identifies the fixed-scalar sheaf underlying the inverse-equivalence image of i_*H with i_*H itself. Naturality of continuity transports the preceding result to that intrinsic module. Apply [dag-lem-pe-coefficient-classical-module-origin], then the proved private fixed-comparison isomorphism and the scalar-equivalence counit, to obtain an etale antecedent of i_*H. Empty Z and a full-image nonisomorphic closed immersion use the identical pullback construction. (uses [dag-lem-pe-coefficient-classical-module-origin], `lem-ctf-finite-comparison-model-realization`)

Proof dependencies not drawn: `lem-ctf-finite-comparison-model-realization`.
