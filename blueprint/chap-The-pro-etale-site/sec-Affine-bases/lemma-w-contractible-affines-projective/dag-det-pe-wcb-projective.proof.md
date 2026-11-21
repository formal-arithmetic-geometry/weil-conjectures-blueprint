+++
kind = "proof"
of = "dag-det-pe-wcb-projective"
tags = ["sheaf-dag"]
uses = ["dag-sk-def-pe-weak-contractible"]
+++
1. Apply the already proved source theorem [dag-lem-weil-pbc-source-affine-wcontractible-evaluation] to the identity isomorphism of Spec D. This gives weak contractibility of U for Type (u+1)-valued sheaves. Its closed proof uses exactly the finite affine refinement, splitting of the coproduct cover, inverse-image disjoint clopen partition, and gluing route in this unit. No new geometric assertion is assumed. (uses `lem-weil-pbc-source-affine-wcontractible-evaluation`)
2. For every epimorphism φ:F→G, `lem-weil-pbc-site-sheaf-sets-epi-locally-surjective` makes φ locally surjective. The weak-contractibility conclusion from step 1 therefore makes φ_U surjective. This is clause 2, for arbitrary F and G and without any nonemptiness hypothesis. (uses `lem-weil-pbc-site-sheaf-sets-epi-locally-surjective`, `lem-weil-pbc-source-affine-wcontractible-evaluation`)
3. For an epimorphism φ:F→h_U, apply the surjectivity from step 2 to id_U (with the universe lift). Let x be its preimage. The sheaf version of `lem-galois-yoneda-hom-bijection` sends x to a morphism s:h_U→F. Naturality of the Yoneda bijection in the sheaf identifies s≫φ with the identity because both evaluate to id_U. This proves clause 1, including the empty scheme. Mathlib already supplies subcanonicality of ProEt.topology, so det-pe-topos-functoriality-site is not needed. (uses `lem-galois-yoneda-hom-bijection`)

Proof dependencies not drawn: `lem-weil-pbc-source-affine-wcontractible-evaluation`, `lem-weil-pbc-site-sheaf-sets-epi-locally-surjective`, `lem-galois-yoneda-hom-bijection`.
