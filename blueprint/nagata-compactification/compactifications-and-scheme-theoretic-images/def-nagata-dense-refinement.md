+++
id = "def-nagata-dense-refinement"
kind = "definition"
title = "Dense-refinement construction"
order = 160
lean = ["AlgebraicGeometry.Compactification.denseRefinement"]
uses = ["def-nagata-compactification", "def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-closure", "lemma-nagata-immersion-open-in-scheme-image", "lemma-nagata-scheme-image-of-closed-immersion"]
+++
For a compactification $C=(X\xrightarrow{j}\overline X\to S)$, define
$\mathsf{Dense}(C)$ by replacing $\overline X$ with
$\operatorname{SIm}(j)$ and using $j^{\mathrm{im}}$ as its first map.
