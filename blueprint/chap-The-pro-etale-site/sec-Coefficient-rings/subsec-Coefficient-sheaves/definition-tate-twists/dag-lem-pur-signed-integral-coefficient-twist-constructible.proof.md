+++
kind = "proof"
of = "dag-lem-pur-signed-integral-coefficient-twist-constructible"
tags = ["sheaf-dag"]
uses = ["dag-lem-pur-twist-sheaf-locally-free", "dag-lem-pur-finite-locally-free-line-models", "dag-lem-pur-constructible-single-support"]
+++
1. The existing pur_twist_sheaf_locally_free theorem gives rank one for the completed first root line. Apply the rank field of OrdinaryLineScalar.exists_lineData to obtain rank one for every signed tensor power. Integer cases identify its generic signedLinePower with the published coefficientTwistLine, including exponent zero and internal duals at negative exponents. (uses [dag-lem-pur-twist-sheaf-locally-free], `lem-pur-ordinary-line-derived-scalar-comparison`)
2. Apply completedLine_derived to this rank-one completed line. Its second clause gives completeness for the actual augmented integral reduction tower; its first clause identifies each derived reduction with the degree-zero single of ordinary change of rings along the actual completed coefficient projection.
3. Use scalarExtensionDual_localIsomorphism to see that each ordinary reduction is still invertible, hence rank one. The generic finiteLocallyFreeLine_models theorem over the positive finite quotient ring gives constructibility of this sheaf. This argument needs no identification with a separately constructed finite Tate line. (uses [dag-lem-pur-finite-locally-free-line-models], `lem-sp-scalar-extension-dual-local-iso`)
4. Apply constructible_single_support using the canonical derived-reduction isomorphism from the second step. It gives finite cohomological support, constructible homology in every degree, and support contained in {0}. These are exactly intrinsic finite-torsion constructibility and the common interval [0,0]. Pair these with completeness to prove the unchanged integral predicate. The empty scheme has empty support, so the same interval works there too. (uses [dag-lem-pur-constructible-single-support])

Proof dependencies not drawn: `lem-pur-ordinary-line-derived-scalar-comparison`, `lem-sp-scalar-extension-dual-local-iso`, `lem-pur-ordinary-line-scalar-line-data`.
