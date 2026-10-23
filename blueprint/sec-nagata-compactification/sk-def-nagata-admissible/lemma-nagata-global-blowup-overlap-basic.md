+++
id = "lemma-nagata-global-blowup-overlap-basic"
kind = "lemma"
title = "The basic-overlap comparison is an isomorphism"
order = 192
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.isPullback_blowupNatTrans_of_basicOpen"]
uses = ["def-nagata-affine-blowup", "def-nagata-affine-blowup-restriction-map", "def-nagata-affine-proj", "def-nagata-global-blowup-local-model", "def-nagata-global-blowup-overlap-basic-map", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-rees-algebra", "def-nagata-rees-localization-map", "def-nagata-rees-piece", "lemma-nagata-localization-ideal-pow", "lemma-nagata-rees-degree-zero", "lemma-nagata-rees-piece-membership", "lemma-nagata-rees-piece-mul", "prop-nagata-rees-graded"]
+++
Let $\mathcal I\subseteq\mathcal O_X$ be quasi-coherent, and let
$W\subseteq V$ be affine opens of $X$ such that $W=D(s)$ is the basic open
of some $s\in\Gamma(V,\mathcal O_X)$. Then the square formed by the
transition map $\mathsf B_W(\mathcal I)\to\mathsf B_V(\mathcal I)$ of
[def-nagata-global-blowup-local-model], the structure morphisms
$\mathsf B_W(\mathcal I)\to W$ and $\mathsf B_V(\mathcal I)\to V$, and the
inclusion $W\subseteq V$ is cartesian; that is,
$\mathsf B_W(\mathcal I)\cong\mathsf B_V(\mathcal I)\times_VW$.
