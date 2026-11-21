+++
kind = "proof"
of = "dag-lem-pe-affine-etale-large-limit-maps"
tags = ["sheaf-dag"]
uses = ["dag-lem-pe-affine-etale-large-limit-factorization", "dag-lem-pe-affine-etale-large-limit-equality"]
+++
1. Reflect the specified limiting cone through the fully faithful forgetful functor X.ProEt → Over X. Its opposite cone is a colimit cocone in X.ProEtᵒᵖ. It suffices to show that coyoneda at Vᵒᵖ maps this cocone to a colimit.
2. For any morphism c.pt → V, apply the larger-index factorization theorem to obtain a stage map D(i) → V with the stated composite. Taking opposites proves joint surjectivity of the coyoneda image cocone. (uses [dag-lem-pe-affine-etale-large-limit-factorization])
3. For two maps out of the same stage whose images at the vertex are equal, apply the larger-index eventual-equality theorem. Taking opposites gives a transition of the filtered Hom diagram making the representatives equal. Types.FilteredColimit.isColimitOf' combines this with joint surjectivity to prove the mapped cocone is colimiting. The theorem preservesColimit_of_preserves_colimit_cocone then gives preservation of D.op. (uses [dag-lem-pe-affine-etale-large-limit-equality])
