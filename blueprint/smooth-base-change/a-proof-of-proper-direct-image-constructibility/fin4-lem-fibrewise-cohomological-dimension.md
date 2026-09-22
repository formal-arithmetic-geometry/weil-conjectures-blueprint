+++
id = "fin4-lem-fibrewise-cohomological-dimension"
kind = "lemma"
title = "Cohomological dimension over an algebraically closed field"
order = 5183
lean = ["AlgebraicGeometry.Etale.cohomology_eq_zero_of_dim_lt_of_algClosed"]
uses = ["sbc-def-coefficient-conventions"]
+++
Let $k'$ be algebraically closed, let $X$ be a finite-type $k'$-scheme of
dimension at most $d$, and let $F$ be a constructible $\Lambda$-sheaf, with
finite coefficients as in [sbc-def-coefficient-conventions]. Then
$H^q(X_{\Et},F)=0$ for $q>2d$.

## Proof

The coefficient ring of [sbc-def-coefficient-conventions] is killed by a
positive integer, so $F$ is torsion. The absolute Galois group of $k'$ is
trivial; the field dictionary between étale module sheaves and discrete
Galois modules therefore gives torsion cohomological dimension zero for
$k'$. Apply the cohomological-dimension theorem for finite-type schemes with
$c=0$. It proves the stronger assertion for all torsion étale sheaves. Its
proof uses Zariski Leray and the affine ordinary cohomological-dimension
theorem; no compact-support identification or affine compact-support bound
is involved.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-constructible-complexes, def:weil-pbc-etale-cohomology, thm:sc-finite-type-torsion-cd, lem:exc-field-discrete-modules
