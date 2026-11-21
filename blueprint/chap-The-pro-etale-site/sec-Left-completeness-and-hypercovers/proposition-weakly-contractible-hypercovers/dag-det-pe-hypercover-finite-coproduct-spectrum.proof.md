+++
kind = "proof"
of = "dag-det-pe-hypercover-finite-coproduct-spectrum"
tags = ["sheaf-dag"]
uses = ["dag-det-pe-hypercover-product-wcontractible"]
+++
1. Reindex I along its equivalence with Fin (Nat.card I), so that the finite product of the coordinate rings stays in universe u. Apply the finite-product w-contractibility theorem. Mathlib sigmaSpec is an isomorphism for finite index types; compose its inverse with the coproduct of the chosen component isomorphisms and the coproduct reindexing isomorphism. For I empty the product is the zero ring and both schemes are empty. (uses [dag-det-pe-hypercover-product-wcontractible], `lem-weil-pbc-finite-affine-coproduct-spectrum`)

Proof dependencies not drawn: `lem-weil-pbc-finite-affine-coproduct-spectrum`.
