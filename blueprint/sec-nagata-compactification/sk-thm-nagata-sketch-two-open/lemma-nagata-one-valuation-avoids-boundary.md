+++
id = "lemma-nagata-one-valuation-avoids-boundary"
kind = "lemma"
title = "One valuation extension avoids the forbidden boundary"
order = 294
lean = ["AlgebraicGeometry.TwoOpenSide.KeyDisjoint.avoids"]
uses = ["def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-closure", "def-nagata-scheme-theoretic-image", "def-nagata-two-open-boundary-loci", "def-nagata-two-open-comparison-space", "def-nagata-two-open-graph-extensions", "def-nagata-two-open-intermediate-schemes", "lemma-nagata-key-boundary-disjointness", "lemma-nagata-scheme-image-ideal-qc", "lemma-nagata-valuation-factor-closed", "lemma-nagata-valuation-open-closed-point", "lemma-nagata-valuation-pair-factors-comparison"]
+++
Assume the key boundary disjointness of
[lemma-nagata-key-boundary-disjointness]: no point of $X_{12}$ lies over
$\overline Z_{1,2}$ in $X_1$ and over $\overline Z_{2,1}$ in $X_2$.
Let $A$ be a valuation ring with fraction field $K$. Let
$\eta\colon\operatorname{Spec}(K)\to U_1\cap U_2$ be a morphism and let
$g_i\colon\operatorname{Spec}(A)\to X_i$ be morphisms whose restrictions
to $\operatorname{Spec}(K)$ equal $\eta$ followed by the embedding
$U_i\hookrightarrow X_i$, and such that $g_1$ and $g_2$ induce the same
morphism $\operatorname{Spec}(A)\to S$. Then $g_1$ factors through
$X_1\setminus\overline Z_{1,2}$ or $g_2$ factors through
$X_2\setminus\overline Z_{2,1}$.

## Proof

Otherwise the closed point would map into $\overline Z_{1,2}$ under $g_1$
and into $\overline Z_{2,1}$ under $g_2$. By
[lemma-nagata-valuation-pair-factors-comparison], the pair factors
through $X_{12}$, and its closed point then lies in
$X_{12}\cap(\overline Z_{1,2}\times_S\overline Z_{2,1})$, contradicting
the assumed key boundary disjointness. If the closed point avoids
one of the two boundaries, its inverse image of the corresponding open
complement is an open subset of $\operatorname{Spec}(A)$ containing the
closed point. By
[lemma-nagata-valuation-open-closed-point] this open is all of
$\operatorname{Spec}(A)$. The associated $g_i$ therefore factors
through $X_i\setminus\overline Z_{i,j}$.
