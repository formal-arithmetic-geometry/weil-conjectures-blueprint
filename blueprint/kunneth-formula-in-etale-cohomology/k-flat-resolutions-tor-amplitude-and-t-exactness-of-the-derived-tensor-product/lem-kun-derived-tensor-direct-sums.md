+++
id = "lem-kun-derived-tensor-direct-sums"
kind = "lemma"
title = "Derived tensor products preserve direct sums"
order = 6082
lean = ["AlgebraicGeometry.Etale.derivedTensor_preservesCoproducts"]
uses = ["def-kun-derived-tensor"]
+++
For $A\in D(T_{\Et},\Lambda)$, each of the functors
$A\otimes^{\mathbf L}_\Lambda-$ and $-\otimes^{\mathbf L}_\Lambda A$
preserves set-indexed direct sums.

## Proof

Tensor products with a fixed complex preserve direct sums degreewise, and a
K-flat replacement of $A$ represents the derived product, so the statement
follows from [def-kun-derived-tensor].

Unresolved dependencies: def:weil-pbc-derived-categories
