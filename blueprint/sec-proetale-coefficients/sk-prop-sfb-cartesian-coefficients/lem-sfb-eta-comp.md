+++
id = "lem-sfb-eta-comp"
kind = "lemma"
title = "$\\eta$ is compatible with composition"
order = 1259
uses = ["def-sfb-eta", "def-sfb-finite-lower-star-comp"]
lean = ["AlgebraicGeometry.ProEtale.condensedPushforwardHom_comp"]
+++
Let $\Lambda$ be a condensed ring, and let $f\colon X\to Y$ and
$g\colon Y\to Z$ be morphisms of schemes. Then
$$
\eta_{g\circ f}=c_{f,g}\circ g_*(\eta_f)\circ\eta_g\colon
\Lambda_Z\longrightarrow(g\circ f)_*\Lambda_X ,
$$
where the $\eta$ are as in [def-sfb-eta] and
$c_{f,g}\colon g_*f_*\cong(g\circ f)_*$ is the composition isomorphism of
[def-sfb-finite-lower-star-comp] at $\Lambda_X$.
