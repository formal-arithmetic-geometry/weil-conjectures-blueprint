+++
id = "def-nagata-two-open-graph-extensions"
kind = "definition"
title = "Chosen graph extensions"
order = 265
lean = ["AlgebraicGeometry.TwoOpenSide"]
uses = ["def-nagata-graph-extension", "def-nagata-two-open-dense-compactifications"]
+++
Let $u\colon U\to S$ be a morphism of schemes and $U_i\subseteq U$ an open
subscheme. A *side* for $(u,U_i)$ consists of

* a scheme $X_i$ with a proper morphism $X_i\to S$;
* an open subscheme $V_i\subseteq X_i$;
* a proper morphism $\psi_i\colon V_i\to U$ over $S$, i.e. $u\circ\psi_i$
  is the restriction of $X_i\to S$ to $V_i$;
* an open immersion $U_i\hookrightarrow V_i$ whose composite with $\psi_i$
  is the inclusion $U_i\subseteq U$, whose image is exactly
  $\psi_i^{-1}(U_i)$, and such that $\psi_i^{-1}(U_i)\to U_i$ is an
  isomorphism;

such that the image of $U_i$ is dense in $X_i$.

Applying the graph-extension construction to $U_i\subseteq U$ and $C_i$
gives such a side

$$
X_i^{\mathrm{gr}}\longrightarrow X_i,\qquad
U_i\subseteq V_i\subseteq X_i^{\mathrm{gr}},\qquad
\psi_i\colon V_i\longrightarrow U.
$$

From now on replace $X_i$ by $X_i^{\mathrm{gr}}$ and retain the notation
$X_i$ for the resulting proper ambient scheme.
