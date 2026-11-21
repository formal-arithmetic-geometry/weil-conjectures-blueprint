+++
kind = "proof"
of = "dag-lem-pur-signed-line-derived-base-change"
tags = ["sheaf-dag"]
uses = ["dag-lem-pur-identified-ring-pullback-finite-limits", "dag-lem-pur-signed-line-pullback-unique", "dag-lem-pur-signed-line-pullback-naturality", "dag-lem-pur-signed-line-derived-action"]
+++
1. The specified module pullback is additive by its adjunction and preserves colimits because it is a left adjoint. Its invertible structural ring adjunct makes it preserve finite limits. (uses [dag-lem-pur-identified-ring-pullback-finite-limits])
2. Apply the existing normalized signed-line pullback existence theorem to P and t. Its normalized uniqueness gives the inner and outer uniqueness clauses. Apply isomorphism and arbitrary scalar-extension naturality to this same family. (uses [dag-lem-pur-signed-line-pullback-unique], [dag-lem-pur-signed-line-pullback-naturality], `lem-pur-normalized-signed-line-pullback-exists`)
3. For this family construct the normalized ordinary comparisons and their unbounded derived action, including all three coherence equations. Combine these witnesses with exactness and normalized uniqueness. (uses [dag-lem-pur-signed-line-derived-action])

Proof dependencies not drawn: `lem-pur-normalized-signed-line-pullback-exists`.
