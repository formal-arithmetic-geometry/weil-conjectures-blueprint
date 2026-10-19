+++
id = "lemma-nagata-scheme-image-of-closed-immersion"
kind = "lemma"
title = "Scheme-theoretic image of a closed immersion"
order = 77
lean = ["AlgebraicGeometry.IsClosedImmersion.instIsIsoSchemeToImage"]
uses = ["def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-image", "lemma-nagata-scheme-image-ideal-qc"]
+++
If $i\colon Z\hookrightarrow Y$ is a closed immersion, then the factor map
$i^{\mathrm{im}}\colon Z\to\operatorname{SIm}(i)$ is an isomorphism. Thus
the scheme-theoretic image of a closed immersion is canonically its source,
compatibly with the maps to $Y$.
