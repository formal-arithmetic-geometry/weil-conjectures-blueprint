+++
id = "lemma-weil-pbc-completed-tensor-reduction"
kind = "lemma"
title = "Finite reduction of completed tensor"
order = 1866
uses = ["def-weil-pbc-completed-tensor-product", "lemma-weil-pbc-adic-completion-reduction"]
+++
For every $a$ there is a functorial isomorphism

$$
(A\widehat\otimes^LB)\otimes^LP_a
\xrightarrow{\sim}A\otimes^LB\otimes^LP_a.
$$

## Proof

The completed tensor is the adic completion of $A\otimes^LB$. Apply finite
reduction of adic completion to that object and use associativity of derived
tensor product.
