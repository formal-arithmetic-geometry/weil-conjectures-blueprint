+++
id = "def-nagata-two-open-comparison-space"
kind = "definition"
title = "The two-open comparison space"
order = 278
lean = ["AlgebraicGeometry.TwoOpenSide.comparisonSpace"]
uses = ["def-nagata-scheme-theoretic-closure", "def-nagata-scheme-theoretic-image", "def-nagata-two-open-graph-extensions", "def-nagata-two-open-prepared-boundaries", "lemma-nagata-scheme-image-ideal-qc"]
+++
Define

$$
V_{12}=V_1\times_UV_2.
$$

Let $V_{12}\to X_1\times_SX_2$ be the canonical morphism induced by the
inclusions $V_i\subseteq X_i$. Define

$$
X_{12}=\operatorname{SIm}
\bigl(V_{12}\longrightarrow X_1\times_SX_2\bigr)
$$

and let $p_i\colon X_{12}\to X_i$ be the restrictions of the two product
projections.

When $U\to S$ is separated, $V_{12}\to V_1\times_SV_2$ is a closed
immersion, hence $V_{12}\to X_1\times_SX_2$ is an immersion.
