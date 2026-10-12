+++
id = "lemma-nagata-reduced-dense-image-schematic"
kind = "lemma"
title = "Dense image into a reduced scheme is schematically dense"
order = 283
lean = ["AlgebraicGeometry.IsSchemeTheoreticallyDominant.of_isDominant"]
uses = ["def-nagata-dense-compactification", "def-nagata-scheme-theoretic-image"]
+++
Let $X$ be reduced and let $h\colon U\to X$ be a morphism with dense
topological image. Then $h$ is scheme-theoretically dense: its kernel ideal
$\ker(h)$ is zero, i.e. the image inclusion
$\operatorname{SIm}(h)\hookrightarrow X$ is an isomorphism.
