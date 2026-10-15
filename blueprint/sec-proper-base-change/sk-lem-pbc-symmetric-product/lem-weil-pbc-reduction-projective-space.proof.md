+++
kind  = "proof"
of    = "lem-weil-pbc-reduction-projective-space"
+++
The product projection $(\mathbf P^1_T)^n\to T$ is a composite of $n$
projective-line projections over successive bases, so it has $\mathrm{PBC}$ by
[prop-weil-pbc-composition-stability] applied stepwise. The morphism
$\sigma_n$ is finite by [lem-weil-pbc-symmetric-product-finite], hence has
$\mathrm{PBC}$ by [prop-weil-pbc-finite-morphism], and is surjective by
[lem-weil-pbc-symmetric-product-surjective]. Since $(\mathbf
P^1_T)^n\to\mathbf P^n_T\to T$ composes to the product projection,
[lemma-weil-pbc-cancellation] gives $\mathrm{PBC}$ for $\mathbf P^n_T\to T$.
