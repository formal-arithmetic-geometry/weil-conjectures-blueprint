+++
id = "lem-pc-projective-space-coherent-finiteness"
kind = "lemma"
title = "Coherent cohomology of projective space over a Noetherian ring"
order = 4325
lean = ["AlgebraicGeometry.ProjectiveSpace.finite_cohomology_of_isCoherent"]
uses = ["def-pc-projective-space-twist", "lem-pc-projective-space-cohomology-bound", "lem-pc-projective-space-twist-quotient", "lem-pc-projective-space-twist-cohomology"]
+++
Let $A$ be Noetherian, $P=\mathbf P^n_A$
[def-pc-projective-space-twist], and $\mathcal F$ a coherent module. Then
each $H^q(P,\mathcal F)$ is a finite $A$-module.

## Proof

We descend on $q$, proving the assertion for all coherent modules at once.
For $q>n$ it follows from [lem-pc-projective-space-cohomology-bound].
Suppose it is known in degree $q+1$ for every coherent module. For a given
$\mathcal F$, choose the exact sequence
$0\to\mathcal K\to\mathcal E\to\mathcal F\to0$ of
[lem-pc-projective-space-twist-quotient], with $\mathcal E$ a finite sum of
twists and $\mathcal K$ coherent. The long exact cohomology sequence
contains
$$
 H^q(P,\mathcal E)\longrightarrow H^q(P,\mathcal F)
 \longrightarrow H^{q+1}(P,\mathcal K).
$$
The first term is finite by
[lem-pc-projective-space-twist-cohomology]; the last is finite by the
induction hypothesis applied to $\mathcal K$. The middle term is an
extension of a quotient of the first term by a submodule of the last.
Quotients and extensions of finite modules are finite; the submodule is
finite because $A$ is Noetherian. This proves the induction step,
including $q=0$.

Unresolved dependencies: pqf-def-coherent, pqf-def-cohomology
