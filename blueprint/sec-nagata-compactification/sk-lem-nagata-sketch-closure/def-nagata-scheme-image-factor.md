+++
id = "def-nagata-scheme-image-factor"
kind = "definition"
title = "Canonical factor through a scheme-theoretic image"
order = 28
lean = ["AlgebraicGeometry.Scheme.Hom.toImage"]
uses = ["def-nagata-scheme-theoretic-image", "lemma-nagata-scheme-image-ideal-qc"]
+++
Define

$$
g^{\mathrm{im}}\colon T\longrightarrow\operatorname{SIm}(g)
$$

to be the canonical factorization of $g$ through its scheme-theoretic
image, so that $g_{\mathrm{im}}\circ g^{\mathrm{im}}=g$, where
$g_{\mathrm{im}}\colon\operatorname{SIm}(g)\hookrightarrow Y$ is the
closed immersion.
