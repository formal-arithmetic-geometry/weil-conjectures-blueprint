+++
id = "cor-nagata-blowup-product-common-refinement"
kind = "theorem"
title = "Common refinement by the product ideal"
order = 133
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.exists_blowup_mul_iso", "AlgebraicGeometry.Scheme.IdealSheafData.isIso_blowupMap_restrict"]
tags = ["latex:corollary"]
uses = ["def-nagata-blowup-product-domination-maps", "def-nagata-extended-ideal", "def-nagata-global-blowup", "prop-nagata-global-blowup-cover-independent", "thm-nagata-blowup-product-ideal", "thm-nagata-global-blowup-complement"]
+++
The constructed $d_{\mathcal I}$ and $d_{\mathcal J}$ are morphisms over
$X$:

$$
b_{X,\mathcal I}\circ d_{\mathcal I}=b_{X,\mathcal I\mathcal J}
=b_{X,\mathcal J}\circ d_{\mathcal J}.
$$

If $U\subseteq X$ is an open with
$V(\mathcal I)\cap U=V(\mathcal J)\cap U=\varnothing$, then
$b_{X,\mathcal I}$, $b_{X,\mathcal J}$ and $b_{X,\mathcal I\mathcal J}$
are isomorphisms over $U$, and hence so are the restrictions of
$d_{\mathcal I}$ and $d_{\mathcal J}$ over $U$.
