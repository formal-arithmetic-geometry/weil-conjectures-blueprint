+++
id = "lemma-nagata-prepared-boundaries"
kind = "lemma"
title = "Properties of the prepared boundary closures"
order = 469
lean = ["AlgebraicGeometry.exists_prepared_twoOpenSide"]
uses = ["def-nagata-two-open-prepared-boundaries", "lemma-nagata-blowup-proper", "lemma-nagata-boundary-loci", "lemma-nagata-separate-constructible-closed"]
+++
The constructed replacement $X_i^{\mathrm{prep}}\to X_i^{\mathrm{old}}$
is $V_i$-admissible, the closures
$\overline Z_{i,i}$ and $\overline Z_{i,j}$ are disjoint, and the open
$V_i$ together with the proper map $\psi_i$ is unchanged. The new
structural morphism $X_i^{\mathrm{prep}}\to S$ is proper.

## Proof

By [lemma-nagata-boundary-loci], the subsets $Z_{i,i}$ and
$Z_{i,j}$ are disjoint constructible subsets closed in $V_i$. Apply the
property of the explicitly constructed separation blow-up. It is
$V_i$-admissible, so the selected isomorphism over $V_i$ transports
$\psi_i$ without changing it. The conclusion of
[lemma-nagata-separate-constructible-closed] is exactly the
disjointness of the two closures. The separation blow-up is proper by
[lemma-nagata-blowup-proper]; composing it with the original proper
morphism $X_i^{\mathrm{old}}\to S$ proves that
$X_i^{\mathrm{prep}}\to S$ is proper.
