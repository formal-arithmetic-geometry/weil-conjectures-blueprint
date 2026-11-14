+++
kind = "proof"
of = "dag-lem-pe-coefficient-constructible-locality"
tags = ["sheaf-dag"]
uses = ["dag-lem-pe-coefficient-finite-local-model-pullback"]
+++
1. in the forward direction choose an affine open neighborhood of the point
and forget finite presentation to finite generation. In the converse fix an affine
open U. Intersect each supplied point neighborhood with U, refine to an affine
open W, and pull back its stratification. Finite local models survive further
inverse image and its composition isomorphism. Quasi-compactness of U gives a
finite affine subcover. The global-stratification gluing lemma gives strata each
factoring through one of these local strata. Pull back the local models along
these factorizations. Finally Noetherianity upgrades their finite generation to
finite presentation. The empty cover and empty partition are included. (uses [dag-lem-pe-coefficient-finite-local-model-pullback], `lem-weil-pbc-etale-stratification-local-gluing-core`, `lemma-constructible-pullback-stratification`, `lem-sc-noetherian-finite-module-finite-presentation`)

Proof dependencies not drawn: `lem-weil-pbc-etale-stratification-local-gluing-core`, `lemma-constructible-pullback-stratification`, `lem-sc-noetherian-finite-module-finite-presentation`.
