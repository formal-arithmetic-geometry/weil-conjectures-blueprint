+++
id = "lemma-nagata-scheme-image-ideal-qc"
kind = "lemma"
title = "Mathlib scheme-theoretic image interface"
order = 72
lean = ["AlgebraicGeometry.Scheme.Hom.image"]
+++
For a morphism $g\colon T\to Y$, the scheme-theoretic image is the closed
subscheme $\operatorname{SIm}(g)$ cut out by the quasi-coherent ideal sheaf
$\operatorname{ker}(g)$; it comes with the closed immersion
$g_{\mathrm{im}}\colon\operatorname{SIm}(g)\hookrightarrow Y$ and a factor
map $g^{\mathrm{im}}\colon T\to\operatorname{SIm}(g)$ with
$g_{\mathrm{im}}\circ g^{\mathrm{im}}=g$.
When $g$ is quasi-compact, the maps on sections and stalks
$\mathcal O_{\operatorname{SIm}(g)}\to g^{\mathrm{im}}_*\mathcal O_T$ are
injective and the support of $\operatorname{ker}(g)$ is the closure of the
topological range of $g$.
