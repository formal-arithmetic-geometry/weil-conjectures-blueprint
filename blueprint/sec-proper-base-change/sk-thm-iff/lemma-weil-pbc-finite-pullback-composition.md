+++
id = "lemma-weil-pbc-finite-pullback-composition"
kind = "lemma"
title = "Finite pullback composition"
order = 1563
lean = ["AlgebraicGeometry.Etale.globalSectionsUpperStarMap_comp"]
uses = ["def-weil-pbc-finite-section-pullback", "lemma-weil-pbc-finite-pullback-identity"]
+++
Let $T''\xrightarrow{v}T'\xrightarrow{u}T$ be morphisms of schemes and $G$ an
etale sheaf on $T$ (with values in $\mathcal A$ as in
[def-weil-pbc-finite-section-pullback]). Then the pullback of global sections
along the composite, followed by the map on global sections induced by the
composition isomorphism $(uv)^{-1}G\cong v^{-1}u^{-1}G$, equals the composite
pullback:

$$
\Gamma(T,G)\xrightarrow{(uv)^\sharp}\Gamma(T'',(uv)^{-1}G)\cong
\Gamma(T'',v^{-1}u^{-1}G)
\quad=\quad
\Gamma(T,G)\xrightarrow{u^\sharp}\Gamma(T',u^{-1}G)\xrightarrow{v^\sharp}
\Gamma(T'',v^{-1}u^{-1}G).
$$
