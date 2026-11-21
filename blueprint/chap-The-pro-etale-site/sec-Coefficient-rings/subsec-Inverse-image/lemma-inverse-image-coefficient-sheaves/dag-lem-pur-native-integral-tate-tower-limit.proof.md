+++
kind = "proof"
of = "dag-lem-pur-native-integral-tate-tower-limit"
tags = ["sheaf-dag"]
uses = ["dag-lem-pur-native-integral-tate-finite-representation", "dag-def-pur-sheaf-inverse-limit"]
+++
1. Represent each single finite native Tate level by a finite etale Y-scheme. Apply full faithfulness of lifted Yoneda to transport all actual transition maps, identities and composition laws, giving a diagram of finite etale objects and a natural isomorphism to the underlying set-valued native diagram. No compatibility choice of integral bases at different levels is needed. (uses [dag-lem-pur-native-integral-tate-finite-representation])
2. Reindex the representing diagram by AsSmall of the opposite natural numbers. The source library AffineOverLimit.limitCone constructs its scheme limit, and weaklyEtale_of_isLimit makes its structure morphism weakly etale. It is therefore a cone in Y.ProEt. The fully faithful embedding in Over Y reflects its limit property. Over.pullback preserves this limit, and the embedding in Over X reflects the base-changed limit. Transfer preservation back through the index equivalence. These geometric steps are completely proved in the private helper finiteEtale_geometric_limit. (uses [dag-def-pur-sheaf-inverse-limit], `def-weil-proetale-inverse-image`)
3. Lifted Yoneda preserves these limits. The Kan-extension formula on representables, followed by sheafification, identifies inverse image of lifted Yoneda with lifted Yoneda of geometric base change. Transfer limit preservation through this natural isomorphism and the represented diagram isomorphism. Abelian forgetting commutes with inverse image by sheafPullbackForgetIso: base change is representably flat, so its pointwise Kan-extension indices are filtered and abelian forgetting preserves those colimits. Forgetting abelian groups preserves and reflects limits. Finally internal module forgetting preserves its limit, and reflection gives exactly the abelian cone displayed in the theorem. (uses [dag-def-pur-sheaf-inverse-limit], `lem-weil-pbc-sheaf-pullback-forget-comparison`)

Proof dependencies not drawn: `def-weil-proetale-inverse-image`, `lem-weil-pbc-sheaf-pullback-forget-comparison`.
