+++
kind = "proof"
of = "dag-lem-pe-coefficient-fixed-kernel-comparison"
tags = ["sheaf-dag"]
+++
1. Choose an etale antecedent G and an isomorphism nu_U^*G ≅ j^*F from the hypothesis. Its etale open extension is an explicit candidate antecedent over X.
2. Apply coefficientOpenExtensionComparisonIso to G. This gives nu_X^*(j_!^et G) ≅ j_!^proet(nu_U^*G). Apply the constructed pro-etale extension functor to the given isomorphism, giving j_!^proet(nu_U^*G) ≅ j_!^proet(j^*F). (uses `lem-pe-coefficient-open-extension`)
3. Compose with coefficientOpenClosedKernelIso, identifying j_!^proet(j^*F) with the kernel of the canonical closed unit. These three actual Lean isomorphisms exhibit the desired essential-image witness. (uses `lem-pe-coefficient-open-closed-kernel`)

Proof dependencies not drawn: `lem-pe-coefficient-open-extension`, `lem-pe-coefficient-open-closed-kernel`.
