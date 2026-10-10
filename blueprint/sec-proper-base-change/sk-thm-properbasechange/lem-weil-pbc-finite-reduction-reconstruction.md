+++
id = "lem-weil-pbc-finite-reduction-reconstruction"
kind = "lemma"
title = "Finite reduction of reconstruction"
order = 1249
uses = ["def-weil-pbc-adic-coefficient-datum", "def-weil-pbc-derived-inverse-limit", "prop-weil-pbc-koszul-reconstruction", "prop-weil-pbc-roos-triangle"]
+++
For every $a\geq1$, the derived counit from inverse limit to evaluation
induces a functorial isomorphism

$$
 (\Rlim K_\bullet)\otimes_A^LP_a\xrightarrow{\sim}K_a.
$$

Moreover, $(-)\otimes_A^LP_a$ commutes with the two derived countable
products occurring in the Roos triangle attached to the derived inverse-limit
construction.

## Proof

By [prop-weil-pbc-koszul-reconstruction] the Koszul completion is identified
with $\Rlim K_\bullet$, so we verify the statement for the Koszul completion:
tensoring the strict Koszul tower with the bounded finite-projective
representative of $P_a$ and evaluating at the $a$-th stage gives the
canonical isomorphism. The commutation with the two derived products is the
compatibility of tensor with products in the Roos triangle of
[prop-weil-pbc-roos-triangle].
