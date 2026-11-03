+++
kind  = "proof"
of    = "lemma-nagata-immersion-open-in-scheme-image"
+++
Since $g$ is a quasi-compact immersion, it factors as an open immersion
followed by a closed immersion, and the closed part may be taken to be
$\operatorname{SIm}(g)\hookrightarrow Y$; locally on $Y$ the factor map
$g^{\mathrm{im}}$ is a base change of an open immersion, hence an open
immersion. It is quasi-compact because $g=g_{\mathrm{im}}\circ g^{\mathrm{im}}$
is quasi-compact and $g_{\mathrm{im}}$ is separated. By
[lemma-nagata-scheme-image-ideal-qc] the support of $\ker(g)$ is the closure
of $g(T)$, so the range of $g^{\mathrm{im}}$ is topologically dense, and the
map $\mathcal O_{\operatorname{SIm}(g)}\to (g^{\mathrm{im}})_*\mathcal O_T$ is
injective on sections over the affine opens of $\operatorname{SIm}(g)$ pulled
back from affine opens of $Y$. These form a basis, so this map of sheaves is
injective, i.e. $\ker(g^{\mathrm{im}})=0$ and $g^{\mathrm{im}}$ is
scheme-theoretically dense.
