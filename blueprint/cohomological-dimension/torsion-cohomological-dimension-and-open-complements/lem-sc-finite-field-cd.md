+++
id = "lem-sc-finite-field-cd"
kind = "lemma"
title = "The torsion cohomological dimension of a finite field"
order = 4909
lean = ["Field.torsionCohomologicalDimensionLE_one_of_finite"]
uses = ["def-sc-etale-torsion-cd"]
+++
For a finite field $k$, one has $\operatorname{cd}_{\rm tor}(k)\leq1$, in the
sense of [def-sc-etale-torsion-cd].

## Proof

Finite-field theory identifies $G_k$ with $\widehat{\mathbf Z}$, generated
topologically by Frobenius; each open subgroup has the same form. For trivial
$\mathbf F_\ell$, continuous cochains factor through finite cyclic quotients.
The usual two-periodic cyclic resolution, with differentials $\sigma-1$ and
$1+\cdots+\sigma^{m-1}$, gives
$H^2(\mathbf Z/m,\mathbf F_\ell)=\mathbf F_\ell/m\mathbf F_\ell$.

Inflation from the quotient of order $m$ to that of order $m\ell$ multiplies
this class by $\ell$, hence kills it. For example, describe a degree-two
class by the relation $\widetilde\sigma^m=a$ in its central extension; the
lift of the generator for the inflated extension satisfies
$\widetilde\sigma^{m\ell}=\ell a$. Therefore
$H^2(\widehat{\mathbf Z},\mathbf F_\ell)=0$.

Apply the degree-two criterion for continuous cohomology for each prime and
use the field equivalence between étale module sheaves and discrete Galois
modules. Primary decomposition and the filtered-union description of torsion
sheaves give the assertion for every torsion sheaf.

Unresolved dependencies: lem:exc-field-discrete-modules, lem:sc-group-cd-one, def:exc-continuous-cohomology, lem:weil-pbc-torsion-filtered-union, lem:weil-pbc-cohomology-filtered-colimit
