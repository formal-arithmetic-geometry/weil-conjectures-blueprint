+++
kind = "proof"
of = "dag-lem-pe-coefficient-constructible-iso"
tags = ["sheaf-dag"]
uses = ["dag-lem-pe-coefficient-finite-local-model-pullback"]
+++
1. on each affine open retain its stratification. Restrict the isomorphism to
each stratum and every slice, using functoriality of scalar restriction and inverse
image. Compose its inverse with the given constant trivialization. Finite type and
finite presentation agree over the Noetherian coefficient ring, so the finite-model
isomorphism-invariance theorem gives exactly the recorded presentation predicate. (uses [dag-lem-pe-coefficient-finite-local-model-pullback], `lem-sc-noetherian-finite-module-finite-presentation`)

Proof dependencies not drawn: `lem-sc-noetherian-finite-module-finite-presentation`.
