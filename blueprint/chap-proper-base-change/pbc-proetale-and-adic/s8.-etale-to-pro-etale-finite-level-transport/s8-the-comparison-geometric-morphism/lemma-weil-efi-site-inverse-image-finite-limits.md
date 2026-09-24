+++
id = "lemma-weil-efi-site-inverse-image-finite-limits"
kind = "lemma"
title = "Finite-limit preservation by comparison inverse image"
order = 1784
uses = ["def-weil-pbc-epsilon-comparison", "def-weil-pbc-epsilon-factorization-index-v1", "lemma-weil-pbc-epsilon-factorization-index-filtered-v1", "prop-weil-efi-site-continuity-certificate"]
+++
The functor $\epsilon_X^{-1}$ preserves finite limits of $A$-module sheaves.

## Proof

Before sheafification, evaluation at $W$ is the filtered colimit
$\varinjlim_{I_W}F(U)$. Filtered colimits of $A$-modules commute with finite
limits. Sheafification of $A$-module presheaves is left exact, and the
pullback equation in the continuity certificate identifies the transition
diagrams. The resulting sheaf functor therefore preserves finite limits.
