+++
kind = "proof"
of = "dag-lem-pur-signed-line-derived-action"
tags = ["sheaf-dag"]
uses = ["dag-lem-pur-signed-line-pullback-tensor", "dag-lem-pur-signed-line-power-flat", "dag-lem-pur-flat-tensor-derived-action", "dag-lem-pur-signed-line-localized-coherence"]
+++
1. For each signed degree, construct the normalized ordinary tensor comparison from T. Both signed powers are flat by local rank-one charts; apply flat_tensor_derived_action to obtain the normalized derived data in that degree. The localized-coherence theorem gives the three simultaneous equations for exactly this family of derived data. (uses [dag-lem-pur-signed-line-pullback-tensor], [dag-lem-pur-signed-line-power-flat], [dag-lem-pur-flat-tensor-derived-action], [dag-lem-pur-signed-line-localized-coherence])

Proof dependencies not drawn: `def-pc-flat-sheaf-modules`.
