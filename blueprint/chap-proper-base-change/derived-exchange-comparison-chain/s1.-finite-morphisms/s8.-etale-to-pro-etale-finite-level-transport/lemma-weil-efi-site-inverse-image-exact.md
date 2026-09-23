+++
id = "lemma-weil-efi-site-inverse-image-exact"
kind = "lemma"
title = "Exactness of the packaged comparison inverse image"
order = 1778
uses = ["def-weil-pbc-epsilon-comparison", "lemma-weil-efi-site-inverse-image-finite-limits", "prop-weil-efi-site-sheaf-adjunction-certificate"]
+++
The functor $\epsilon_X^{-1}$ is exact on $A$-module sheaves.

## Proof

Finite-limit preservation gives preservation of kernels. The adjunction
certificate makes $\epsilon_X^{-1}$ a left adjoint, so it preserves
cokernels. Kernel and cokernel preservation gives exactness in the abelian
category of $A$-module sheaves.
