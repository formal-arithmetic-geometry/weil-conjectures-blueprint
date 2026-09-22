+++
id = "lem-kun-derived-tensor-well-defined"
kind = "lemma"
title = "Independence of the K-flat model"
order = 6025
lean = ["AlgebraicGeometry.Etale.derivedTensor_indep_kflat"]
uses = ["def-kun-derived-tensor"]
+++
Let $\Lambda$ be a commutative ring, $T$ a scheme, and let
$\mathcal P^\bullet\to\mathcal Q^\bullet$ be a quasi-isomorphism of K-flat
[def-kun-derived-tensor] complexes of $\Lambda_T$-module sheaves. Then for
every complex $\mathcal F^\bullet$ of $\Lambda_T$-module sheaves the induced
map
$$
\mathcal F^\bullet\otimes_\Lambda\mathcal P^\bullet\longrightarrow
\mathcal F^\bullet\otimes_\Lambda\mathcal Q^\bullet
$$
is a quasi-isomorphism; consequently
$K_1\otimes^{\mathbf L}_\Lambda K_2$ is independent, up to canonical
isomorphism in $D(T_{\Et},\Lambda)$, of the chosen K-flat model of $K_1$.

(*Source:* Stacks Project, Lemma 21.17.12, [Tag
06YT](https://stacks.math.columbia.edu/tag/06YT), and Definition 21.17.13,
[Tag 06YU](https://stacks.math.columbia.edu/tag/06YU).)

## Proof

This is the recorded classical input named in the statement, Stacks Project,
Lemma 21.17.12 and Definition 21.17.13 ([Tag
06YT](https://stacks.math.columbia.edu/tag/06YT), [Tag
06YU](https://stacks.math.columbia.edu/tag/06YU)): a quasi-isomorphism
between K-flat complexes induces a quasi-isomorphism after tensoring with
any complex, so the derived tensor product is independent of the K-flat
model. No separate proof is given.

Unresolved dependencies: def:weil-pbc-derived-categories
