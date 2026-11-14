+++
kind = "proof"
of = "dag-lem-pur-tensor-pushout-action"
tags = ["sheaf-dag"]
+++
1. Map B⊗_A R into the endomorphism ring of B⊗_A M using the R-action on M. On pure tensors its action is (s⊗r)(t⊗x)=st⊗rx. Transport it through each e_U. Double tensor induction and naturality of c,d show that restrictions are semilinear. Taking r=1 identifies the original B-action.
2. The underlying abelian presheaf has the prescribed tensor sheaf as its sheafification. Descend the new action through the locally bijective unit using PresheafOfModules.Sheafify.module. The unit intertwines the action. Locally lifting sections proves the B-normalization, and the pure tensor formula proves the R-normalization. For any other normalized action, double tensor induction shows that the same unit intertwines all T-scalars. The uniqueness of a sheafified scalar product makes the two actions equal, and Module.ext' identifies the module structures. (uses `def-weil-presheaf-modules-sheafification`)

Proof dependencies not drawn: `def-weil-presheaf-modules-sheafification`.
