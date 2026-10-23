+++
kind  = "proof"
of    = "lem-weil-pbc-reduction-projective-space"
+++
The projection $(\mathbf P^1_T)^n\to T$ is a composite of $n$ projective-line
projections over the successive bases $(\mathbf P^1_T)^k$, so it has torsion base
change over $\Lambda$ by the hypothesis and
[prop-weil-pbc-composition-stability] (1) applied stepwise. The symmetric-product
morphism $\sigma_n$ of [def-weil-pbc-symmetric-product-morphism] is finite by
[lem-weil-pbc-symmetric-product-finite], hence has torsion base change by
[prop-weil-pbc-finite-morphism], and is surjective by
[lem-weil-pbc-symmetric-product-surjective]. Since
$(\mathbf P^1_T)^n\xrightarrow{\sigma_n}\mathbf P^n_T\to T$ composes to the product
projection, [lemma-weil-pbc-cancellation] (2) gives torsion base change for
$\mathbf P^n_T\to T$. The case $n=0$ is the identity.
