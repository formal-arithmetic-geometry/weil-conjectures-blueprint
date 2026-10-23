+++
id = "lem-pbc-f1-prime-biproduct-unconditional"
kind = "lemma"
title = "Finite biproduct equivalence for unconditional curve assertions"
uses = ["def-weil-pbc-eight-curve-assertions", "def-weil-pbc-etale-constructible-sheaf"]
lean = ["AlgebraicGeometry.IsCurve.prime_biproduct_unconditional_iff"]
order = 1670
+++
Let $\Lambda$ be a commutative ring, $k$ a field, $X$ a scheme and $f:X\to\operatorname{Spec}k$.
Let $I$ be a finite index set and $G_a$ module sheaves on the small etale site of $X$.
Let $H$ be a module sheaf equipped with an isomorphism $e:H\simeq\bigoplus_a G_a$,
the finite direct sum (biproduct). The predicates $C_1,\ldots,C_8$
are those of [def-weil-pbc-eight-curve-assertions], with their stated conditional hypotheses.
Assume each $G_a$ and $H$ is constructible [def-weil-pbc-etale-constructible-sheaf]. Then
$(C_1(H)\land C_2(H)\land C_5(H)\land C_7(H)\land C_8(H))$ holds if and only if
$C_1(G_a)\land C_2(G_a)\land C_5(G_a)\land C_7(G_a)\land C_8(G_a)$ holds for every $a$.
There is no prime annihilator hypothesis.
