+++
kind = "proof"
of = "dag-lem-pur-signed-line-pullback-unique"
tags = ["sheaf-dag"]
uses = ["dag-lem-pur-ringed-site-pullback-pairing-transfer", "dag-def-pur-sheaf-hom"]
+++
1. The module pullback adjunction detects maps by their values on inserted source sections. In degree zero the normalization fixes the value, and in degree one it fixes t. Induct on positive powers, using tensor generation and the specified recursion to identify the maps. (uses `lem-sp-scalar-extension-binary-coherence`)
2. For a negative power, postcompose the two maps with the internal-dual isomorphism induced by the common positive map. Both maps transfer the same evaluation pairing. Pairing-transfer uniqueness identifies them, and cancel the dual isomorphism. (uses [dag-lem-pur-ringed-site-pullback-pairing-transfer])

Proof dependencies not drawn: `lem-sp-scalar-extension-binary-coherence`, `def-sp-scalar-tensor-comparison-data`.
