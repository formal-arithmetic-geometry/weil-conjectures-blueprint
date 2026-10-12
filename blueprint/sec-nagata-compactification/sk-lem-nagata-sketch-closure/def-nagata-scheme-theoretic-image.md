+++
id = "def-nagata-scheme-theoretic-image"
kind = "definition"
title = "Scheme-theoretic image"
order = 73
lean = ["AlgebraicGeometry.Scheme.Hom.image"]
uses = ["def-weil-pbc-scheme-conventions", "lemma-nagata-scheme-image-ideal-qc"]
+++
Let $g\colon T\to Y$ be a morphism of schemes. Its *kernel ideal*
$\ker(g)\subseteq\mathcal O_Y$ is the largest quasi-coherent ideal
contained in the kernel of $\mathcal O_Y\to g_*\mathcal O_T$ (this kernel
itself when $g$ is quasi-compact). The *scheme-theoretic image*
$\operatorname{SIm}(g)$ of $g$ is the closed subscheme of $Y$ defined by
$\ker(g)$, with inclusion
$g_{\mathrm{im}}\colon\operatorname{SIm}(g)\hookrightarrow Y$ and factor map
$g^{\mathrm{im}}\colon T\to\operatorname{SIm}(g)$ as in
[lemma-nagata-scheme-image-ideal-qc]. A morphism $g\colon T\to Y$ is
*scheme-theoretically dense* if its scheme-theoretic image is $Y$ itself,
i.e. $\ker(g)=0$. The scheme-theoretic closure of a locally closed
subscheme is the scheme-theoretic image of its immersion.
