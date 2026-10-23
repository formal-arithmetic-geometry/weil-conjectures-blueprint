+++
id = "lemma-nagata-proj-chart-ring-cocycle"
kind = "lemma"
title = "Coherence of the standard Proj chart rings"
lean = ["HomogeneousLocalization.Away.overlapEquiv", "HomogeneousLocalization.Away.overlapEquiv_awayMap_left", "HomogeneousLocalization.Away.overlapEquiv_awayMap_right", "HomogeneousLocalization.Away.overlapEquiv_self", "HomogeneousLocalization.Away.overlapEquiv_symm", "HomogeneousLocalization.Away.overlapEquiv_cocycle"]
order = 152
uses = ["def-nagata-homogeneous-localization-degree-zero"]
+++
Let $f,g,h\in R$ be homogeneous. Localization induces a canonical ring
isomorphism $\varphi_{fg}\colon R_{(fg),0}\xrightarrow{\sim}R_{(gf),0}$
between the two overlap rings indexed by $fg$, compatible with the
localization maps from $R_{(f),0}$ and from $R_{(g),0}$. These
isomorphisms are the identity for $f=g$, satisfy
$\varphi_{fg}^{-1}=\varphi_{gf}$, and satisfy the cocycle equality on the
triple overlap: after composing with the localization maps into
$R_{(fgh),0}$, each of $\varphi_{fg}$, $\varphi_{gh}$, $\varphi_{fh}$
becomes the identity, so $\varphi_{gh}\circ\varphi_{fg}=\varphi_{fh}$ there.
