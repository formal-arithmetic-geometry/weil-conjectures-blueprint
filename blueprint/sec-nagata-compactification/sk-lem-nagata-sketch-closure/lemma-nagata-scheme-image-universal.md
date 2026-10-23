+++
id = "lemma-nagata-scheme-image-universal"
kind = "lemma"
title = "Universal property of the scheme-theoretic image"
order = 111
lean = ["AlgebraicGeometry.Scheme.Hom.toImage_imageι", "AlgebraicGeometry.IsClosedImmersion.lift_fac", "AlgebraicGeometry.isClosedImmersion_lift", "AlgebraicGeometry.IsClosedImmersion.eq_lift"]
uses = ["def-nagata-scheme-image-comparison"]
+++
The composite of $g^{\mathrm{im}}$ with
$\operatorname{SIm}(g)\hookrightarrow Y$ is $g$. For every closed
factorization through $Z$, the constructed map $c_{g,Z}$ is a closed
immersion compatible with the maps to $Y$, and it is the unique compatible
morphism $\operatorname{SIm}(g)\to Z$.
