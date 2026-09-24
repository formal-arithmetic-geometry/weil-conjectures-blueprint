+++
id = "lemma-nagata-key-boundary-disjointness"
kind = "lemma"
title = "Key boundary disjointness"
order = 479
lean = ["AlgebraicGeometry.TwoOpenSide.KeyDisjoint"]
uses = ["lemma-nagata-comparison-boundary-density", "lemma-nagata-prepared-boundaries", "lemma-nagata-two-open-comparison-boundary"]
+++
Inside $X_1\times_SX_2$ one has

$$
X_{12}\cap
(\overline Z_{1,2}\times_S\overline Z_{2,1})
=\varnothing.
$$

## Proof

Put $C=p_1^{-1}(\overline Z_{1,2})$. By
[lemma-nagata-comparison-boundary-density], $Z_{12,2}$ is dense in
$C$. The definition of the comparison boundary and
[lemma-nagata-two-open-comparison-boundary] give

$$
p_2(Z_{12,2})\subseteq Z_{2,2}\subseteq\overline Z_{2,2}.
$$

Equivalently, $Z_{12,2}$ is contained in the closed inverse image
$p_2^{-1}(\overline Z_{2,2})$. Because it is dense in $C$, this closed
inverse image also contains $C$. Thus
$p_2(C)\subseteq\overline Z_{2,2}$.
The two closed subschemes $\overline Z_{2,2}$ and
$\overline Z_{2,1}$ are disjoint by
[lemma-nagata-prepared-boundaries]. Thus no point of $C$ can map into
$\overline Z_{2,1}$, which is precisely the asserted empty intersection.
