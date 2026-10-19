+++
id = "lemma-nagata-valuation-pair-factors-comparison"
kind = "lemma"
title = "A pair of generic extensions factors through $X_{12}$"
order = 299
lean = ["AlgebraicGeometry.TwoOpenSide.exists_comparisonFst_comparisonSnd"]
uses = ["def-nagata-two-open-graph-extensions", "def-nagata-two-open-intermediate-schemes", "def-nagata-two-open-comparison-space"]
+++
Let $A$ be a domain with fraction field $K$. Let
$\eta\colon\operatorname{Spec}(K)\to U_1\cap U_2$ be a morphism and let
$g_i\colon\operatorname{Spec}(A)\to X_i$ be morphisms whose restrictions
to $\operatorname{Spec}(K)$ equal $\eta$ followed by the embedding
$U_i\hookrightarrow X_i$, and such that $g_1$ and $g_2$ induce the same
morphism $\operatorname{Spec}(A)\to S$. Then the pair

$$
(g_1,g_2)\colon\operatorname{Spec}(A)\to X_1\times_SX_2
$$

factors through $X_{12}$: there is a morphism
$l\colon\operatorname{Spec}(A)\to X_{12}$ with $p_1\circ l=g_1$ and
$p_2\circ l=g_2$.
