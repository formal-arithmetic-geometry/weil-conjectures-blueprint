+++
id = "def-nagata-global-blowup-local-model"
kind = "definition"
title = "Local blow-up model on an affine open"
order = 295
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.blowupFunctor"]
uses = ["def-nagata-affine-blowup", "def-nagata-affine-blowup-restriction-map", "lemma-nagata-affine-blowup-restrict-cocycle", "lemma-nagata-rees-generators-cover-proj", "prop-nagata-proj-standard-open"]
+++
Let $\mathcal I\subseteq\mathcal O_X$ be quasi-coherent and let
$V=\operatorname{Spec}(A)\subseteq X$ be affine. Put
$I_V=\Gamma(V,\mathcal I)\subseteq A$ and define the local model

$$
\mathsf B_V(\mathcal I)=\operatorname{Bl}_{I_V}(V)\longrightarrow V.
$$
