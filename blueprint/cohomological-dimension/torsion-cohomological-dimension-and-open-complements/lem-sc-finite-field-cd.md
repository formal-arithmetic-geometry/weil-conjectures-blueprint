+++
id = "lem-sc-finite-field-cd"
kind = "lemma"
title = "The torsion cohomological dimension of a finite field"
order = 2739
uses = ["def-exc-continuous-cohomology", "def-sc-etale-torsion-cd", "lem-exc-field-discrete-modules", "lem-sc-group-cd-one", "lem-weil-pbc-cohomology-filtered-colimit", "lemma-weil-pbc-torsion-filtered-union"]
+++
For a finite field $k$, one has
$\operatorname{cd}_{\rm tor}(k)\leq1$, in the sense of
[def-sc-etale-torsion-cd].

## Proof

Finite-field theory identifies $G_k$ with
$\widehat{\mathbf Z}$, generated topologically by Frobenius;
each open subgroup has the same form. For trivial
$\mathbf F_\ell$, continuous cochains, as in
[def-exc-continuous-cohomology], factor through finite
cyclic quotients. The usual two-periodic cyclic resolution,
with differentials $\sigma-1$ and $1+\cdots+\sigma^{m-1}$,
gives $H^2(\mathbf Z/m,\mathbf F_\ell)= \mathbf F_\ell/m\mathbf F_\ell$.
Inflation from the quotient of order $m$ to that of order
$m\ell$ multiplies this class by $\ell$, hence kills it.
For example, describe a degree-two class by the relation
$\widetilde\sigma^m=a$ in its central extension; the lift of
the generator for the inflated extension satisfies
$\widetilde\sigma^{m\ell}=\ell a$.
Therefore $H^2(\widehat{\mathbf Z},\mathbf F_\ell)=0$.
Apply [lem-sc-group-cd-one] for each prime and use the
field equivalence of [lem-exc-field-discrete-modules].
Primary decomposition and
[lemma-weil-pbc-torsion-filtered-union], [lem-weil-pbc-cohomology-filtered-colimit]
give the assertion for every torsion sheaf.
