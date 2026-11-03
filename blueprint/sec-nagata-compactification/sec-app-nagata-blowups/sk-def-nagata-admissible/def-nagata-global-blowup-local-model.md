+++
id = "def-nagata-global-blowup-local-model"
kind = "definition"
title = "Local blow-up model on an affine open"
order = 93
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.blowupFunctor"]
uses = ["def-nagata-affine-blowup", "def-nagata-affine-blowup-restriction-map", "def-nagata-affine-proj", "def-nagata-rees-algebra", "def-nagata-rees-localization-map", "def-nagata-rees-piece", "lemma-nagata-affine-blowup-restrict-cocycle", "lemma-nagata-localization-ideal-pow", "lemma-nagata-rees-piece-membership", "prop-nagata-rees-graded"]
+++
Let $\mathcal I\subseteq\mathcal O_X$ be quasi-coherent. For an affine open
$V\subseteq X$, put $A_V=\Gamma(V,\mathcal O_X)$ and
$I_V=\Gamma(V,\mathcal I)\subseteq A_V$, and define the local model

$$
\mathsf B_V(\mathcal I)=\operatorname{Bl}_{I_V}(\operatorname{Spec}A_V).
$$

For affine opens $W\subseteq V$, the restriction map $A_V\to A_W$ carries
$I_V$ to a generating set of $I_W$; let
$\mathsf B_W(\mathcal I)\to\mathsf B_V(\mathcal I)$ be the induced morphism
of [def-nagata-affine-blowup-restriction-map]. This defines a functor
$V\mapsto\mathsf B_V(\mathcal I)$ on the poset of affine opens of $X$.
