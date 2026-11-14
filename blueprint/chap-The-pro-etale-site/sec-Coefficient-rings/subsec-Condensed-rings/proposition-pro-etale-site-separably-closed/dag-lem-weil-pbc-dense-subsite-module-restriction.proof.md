+++
kind = "proof"
of = "dag-lem-weil-pbc-dense-subsite-module-restriction"
tags = ["sheaf-dag"]
+++
1. Given a module sheaf on the smaller site, lift its underlying abelian sheaf through the assumed equivalence and use the actual equivalence counit. Conjugate the scalar-action map by this counit and lift it using fullness of set-sheaf restriction. Restriction of the lifted action is the original action under the counit.
2. Check one_smul, mul_smul, smul_zero, smul_add, add_smul and zero_smul after restriction along every arrow from the cover-dense subsite. The counit is injective on each test object, and equality on that covering sieve detects equality of sections. The natural lifted action makes the abelian sheaf a sheaf of modules. The counit is linear, hence an isomorphism of module sheaves, giving essential surjectivity.
3. Lift a morphism using fullness on abelian sheaves. Check its compatibility with scalars by restricting both sides to the dense covering sieve; naturality and linearity of the given restricted morphism prove equality. This proves fullness, while faithfulness follows from faithfulness of abelian restriction and of the forgetful functor. Fullness, faithfulness and essential surjectivity give the desired equivalence for the identity scalar map.
