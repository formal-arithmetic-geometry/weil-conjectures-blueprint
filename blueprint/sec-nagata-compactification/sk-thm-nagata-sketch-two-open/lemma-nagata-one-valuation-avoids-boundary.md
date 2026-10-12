+++
id = "lemma-nagata-one-valuation-avoids-boundary"
kind = "lemma"
title = "One valuation extension avoids the forbidden boundary"
order = 301
lean = ["AlgebraicGeometry.TwoOpenSide.KeyDisjoint.avoids"]
uses = ["def-nagata-two-open-graph-extensions", "def-nagata-two-open-intermediate-schemes", "lemma-nagata-key-boundary-disjointness", "lemma-nagata-valuation-open-closed-point", "lemma-nagata-valuation-pair-factors-comparison"]
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
