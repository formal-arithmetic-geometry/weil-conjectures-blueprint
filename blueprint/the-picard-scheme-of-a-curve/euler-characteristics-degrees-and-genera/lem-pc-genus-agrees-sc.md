+++
id = "lem-pc-genus-agrees-sc"
kind = "lemma"
title = "Agreement with the genus of the earlier chapter"
order = 4303
lean = ["AlgebraicGeometry.genus_eq_genus_sc"]
uses = ["def-pc-genus", "def-pc-smooth-projective-curve"]
+++
Let $k$ be an algebraically closed field and $C$ a smooth projective curve
[def-pc-smooth-projective-curve] over $k$ (or, more generally, a proper
smooth curve in the sense of the curve-calculation chapter with
$\dim H^0(C,\mathcal{O}_C)=1$). Then the genus $g(C)$ of [def-pc-genus]
equals the genus of that chapter.

## Proof

Both definitions are $g=\dim_kH^1(C,\mathcal{O}_C)$ (Definition 44.6.3 in
the first case, specific to the geometrically irreducible smooth
projective curve; Definition 53.8.1, [Tag
0BY7](https://stacks.math.columbia.edu/tag/0BY7), in the second), so they
agree.

Unresolved dependencies: def:sc-genus, def:sc-curves
