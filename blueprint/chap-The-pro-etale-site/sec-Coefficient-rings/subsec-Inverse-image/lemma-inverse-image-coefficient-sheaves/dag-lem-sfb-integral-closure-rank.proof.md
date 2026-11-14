+++
kind = "proof"
of = "dag-lem-sfb-integral-closure-rank"
tags = ["sheaf-dag"]
+++
1. A PID is Noetherian and integrally closed by `lem-weil-pbc-pid-noetherian-normal`, so `lem-weil-pbc-noetherian-normal-separable-integral-closure-finite` makes $C$ finite over $A$. It is torsion-free since it embeds in the field $L$ and nonzero elements of $A$ stay nonzero there. The PID form of `lem-sc-dvr-fg-torsionfree-free` makes it free. Localizing an $A$-basis of $C$ at the nonzero elements of $A$ gives a $K$-basis of $L$: every $z\in L$ has an integral nonzero multiple $az\in C$, and every finite $K$-linear relation can be multiplied by a common nonzero denominator to give an $A$-linear relation. Thus the two basis cardinalities agree, giving the equality by `def-weil-vector-space-dimension`. This is exactly IsIntegralClosure.rank, whose proof uses IsIntegralClosure.isLocalization and Basis.localizationLocalization; its source and all hypotheses were checked in the pinned Mathlib. (uses `lem-weil-pbc-pid-noetherian-normal`, `lem-weil-pbc-noetherian-normal-separable-integral-closure-finite`, `lem-sc-dvr-fg-torsionfree-free`)

Proof dependencies not drawn: `lem-weil-pbc-pid-noetherian-normal`, `lem-weil-pbc-noetherian-normal-separable-integral-closure-finite`, `lem-sc-dvr-fg-torsionfree-free`.
