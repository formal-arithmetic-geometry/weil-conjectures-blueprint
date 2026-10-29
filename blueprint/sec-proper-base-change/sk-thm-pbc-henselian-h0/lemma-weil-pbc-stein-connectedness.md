+++
id = "lemma-weil-pbc-stein-connectedness"
kind = "lemma"
title = "Stein connectedness"
lean = ["AlgebraicGeometry.Scheme.Hom.spectralSpace_and_isClosed_and_isConnected_inter"]
order = 1651
uses = ["def-weil-pbc-henselian-terminology", "def-weil-pbc-scheme-conventions", "lemma-weil-pbc-spectral-restriction"]
+++
Let $(A,I)$ be henselian [def-weil-pbc-henselian-terminology] and let
$p:Y\to\operatorname{Spec}A$ be proper
[def-weil-pbc-scheme-conventions], with closed fibre
$Y_0=p^{-1}(V(I))$. Then the underlying space of $Y$ is spectral, $Y_0$ is
closed in $Y$, and every irreducible closed subset of $Y$ meets $Y_0$ in a
nonempty connected subset. These are the hypotheses of the Zariski
restriction criterion [lemma-weil-pbc-spectral-restriction] for the pair
$(Y,Y_0)$.
