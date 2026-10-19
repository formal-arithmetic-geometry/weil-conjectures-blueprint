+++
id = "def-nagata-global-blowup-glue-data"
kind = "definition"
title = "Raw global blow-up gluing datum"
order = 62
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.blowupGluingData", "AlgebraicGeometry.Scheme.IdealSheafData.blowupNatTrans_equifibered"]
uses = ["def-nagata-affine-blowup", "def-nagata-affine-blowup-restriction-map", "def-nagata-affine-proj", "def-nagata-global-blowup-local-model", "def-nagata-global-blowup-overlap-basic-map", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-rees-algebra", "def-nagata-rees-localization-map", "def-nagata-rees-piece", "lemma-nagata-global-blowup-overlap-cocycle", "lemma-nagata-global-blowup-overlap-id-symm", "lemma-nagata-global-blowup-overlap-independent", "lemma-nagata-localization-ideal-pow", "lemma-nagata-rees-degree-zero", "lemma-nagata-rees-piece-membership", "lemma-nagata-rees-piece-mul", "prop-nagata-rees-graded"]
+++
Let $\mathcal I\subseteq\mathcal O_X$ be a quasi-coherent ideal. Define
$\mathsf G(X,\mathcal I)$ to be the relative gluing datum over $X$,
indexed by the set of all affine opens of $X$ ordered by inclusion,
consisting of the diagram $V\mapsto\mathsf B_V(\mathcal I)$ of
[def-nagata-global-blowup-local-model] together with the structure
morphisms $\mathsf B_V(\mathcal I)\to V$. These structure morphisms are
compatible with the transition maps, and for all affine opens
$W\subseteq V$ the square

$$
\begin{array}{ccc}
\mathsf B_W(\mathcal I) & \longrightarrow & \mathsf B_V(\mathcal I)\\
\downarrow & & \downarrow\\
W & \longrightarrow & V
\end{array}
$$

is cartesian.
