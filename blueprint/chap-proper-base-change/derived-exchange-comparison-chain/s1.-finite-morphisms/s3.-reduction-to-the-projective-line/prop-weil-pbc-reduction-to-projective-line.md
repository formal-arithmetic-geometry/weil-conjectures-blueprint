+++
id = "prop-weil-pbc-reduction-to-projective-line"
kind = "theorem"
title = "Reduction of proper base change to $\\mathbf P^1$"
order = 1570
tags = ["latex:proposition"]
uses = ["def-weil-pbc-derived-exchange", "lemma-weil-pbc-cancellation", "lemma-weil-pbc-chow-embedding-over-x", "lemma-weil-pbc-chow-factorization", "lemma-weil-pbc-composition", "lemma-weil-pbc-symmetric-product-p1", "lemma-weil-pbc-target-locality", "prop-weil-pbc-finite-morphism"]
+++
If every projection $\mathbf P^1_S\to S$ satisfies $\mathsf{PBC}$ for every
base scheme $S$, then every proper morphism satisfies $\mathsf{PBC}$.

## Proof

Use target locality and the Chow factorization. The closed immersion
$X'\hookrightarrow\mathbf P^n_Y$ is proper and finite onto its image, so
finite base change plus composition reduces $X'\to Y$ to
$\mathbf P^n_Y\to Y$. The finite surjective map $\sigma_n$ and cancellation
reduce this projection to $(\mathbf P^1_Y)^n\to Y$. Repeated base change and
composition reduce the product projection to the one-dimensional projection.
Finally cancellation along $\pi$ transfers the property from $X'$ and
$X'\to Y$ to $X\to Y$. Every comparison used is the named exchange map of
Definition [def-weil-pbc-derived-exchange].
