+++
id = "det-nagata-density-normalization-setup"
kind = "lemma"
title = "The schematic closure inside a Noetherian compactification"
lean = ["AlgebraicGeometry.Scheme.Hom.image", "AlgebraicGeometry.Scheme.Hom.imageι", "AlgebraicGeometry.Scheme.Hom.toImage", "AlgebraicGeometry.Scheme.Hom.toImage_imageι", "AlgebraicGeometry.Scheme.Hom.ker_toImage"]
order = 1351
uses = ["def-nagata-compactification", "lemma-nagata-immersion-open-in-scheme-image"]
+++
Let $X\xrightarrow{j}\overline X\xrightarrow{p}S$ be a compactification with
$\overline X$ Noetherian, let $i:Z\hookrightarrow\overline X$ be the
scheme-theoretic image of $j$, and put $V=\overline X\setminus Z$ with open
immersion $j_V:V\hookrightarrow\overline X$. Then:

1. $j$ factors as $j=i\circ j_Z$ with $j_Z:X\hookrightarrow Z$ a
   quasi-compact open immersion, and $j_Z$ is scheme-theoretically dense;
1. $\overline X$ and $Z$ are quasi-compact and quasi-separated, and $V$ is a
   quasi-compact open of $\overline X$ whose closed complement is $Z$;
1. $j(X)\cap V=\varnothing$, so $X\times_{\overline X}V=\varnothing$ and
   $X\times_{\overline X}Z=X$ (via $j_Z$);
1. $p\circ i:Z\to S$ is proper.
