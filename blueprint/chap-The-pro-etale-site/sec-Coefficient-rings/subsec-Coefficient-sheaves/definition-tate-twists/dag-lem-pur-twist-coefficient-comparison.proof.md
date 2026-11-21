+++
kind = "proof"
of = "dag-lem-pur-twist-coefficient-comparison"
tags = ["sheaf-dag"]
uses = ["dag-lem-pur-twist-coefficient-tensor", "dag-lem-pur-sectionwise-pushout"]
+++
1. The normalized tensor map is bijective by purTwistCoefficientTensor. Transport CommRingCat.isPushout_tensorProduct along this ring equivalence on each object. Its pure-tensor formula identifies the two given legs. Apply the sectionwise sheaf pushout lemma. The resulting pushout isomorphism is inverse to the canonical comparison, by hom_ext and the comparison leg equations. (uses [dag-lem-pur-twist-coefficient-tensor], [dag-lem-pur-sectionwise-pushout])
