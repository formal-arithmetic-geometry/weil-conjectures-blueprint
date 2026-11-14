+++
kind = "proof"
of = "dag-lem-weil-pbc-proetale-locally-classical-etale-cover"
tags = ["sheaf-dag"]
uses = ["dag-lem-weil-pbc-proetale-locally-classical-continuity", "dag-lem-weil-pbc-proetale-continuous-counit-sets", "dag-lem-weil-pbc-proetale-comparison-unit-sets", "dag-def-weil-pbc-ind-etale-basis", "dag-sk-def-pe-morphisms"]
+++
1. Apply affine continuity for locally classical sheaves, then the comparison counit criterion. Its inverse exhibits F as ν_X^*ν_{X,*}F. (uses [dag-lem-weil-pbc-proetale-locally-classical-continuity], [dag-lem-weil-pbc-proetale-continuous-counit-sets])
2. The etale and pro-etale constant-sheaf functors are left adjoint to evaluation at the identity object, and restriction along toProEt preserves that terminal evaluation. Uniqueness of left adjoints gives ν_X^* constant_et ≅ constant_proet. Transport the local trivializations and apply the first step. (uses `def-weil-pbc-site-comparison-morphism`)
3. Write F≅ν_X^*G. Local sections make ν_X^*G→ν_X^*1 an epimorphism by the locally-surjective criterion. The invertible comparison unit makes ν_X^* faithful, so it reflects this epimorphism. Therefore G→1 is locally surjective on the etale site. The family of all pairs (etale object, section of G) covers; the comparison unit and the chosen isomorphism provide sections of F on this family. (uses [dag-lem-weil-pbc-proetale-comparison-unit-sets])

Proof dependencies not drawn: `def-weil-pbc-site-comparison-morphism`.
