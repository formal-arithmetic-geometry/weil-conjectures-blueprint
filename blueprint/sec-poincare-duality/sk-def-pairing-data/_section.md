+++
id = "sk-def-pairing-data"
kind = "definition"
title = "The pairing data"
order = 3432
uses = ["sk-def-ops", "sk-def-sf-orientation"]
lean = ["AlgebraicGeometry.Etale.mixedSupportCupProduct", "AlgebraicGeometry.Etale.smoothTrace", "AlgebraicGeometry.Etale.TateOrientation.smoothTrace"]
tags = ["sketch"]
+++
In the setting of [sk-def-ops], the *mixed-support cup product* is

$$
\smile_c:\RGammac(X,K)\otimes^L_\Lambda\RGamma(X,L)\longrightarrow
\RGammac\bigl(X,K\otimes^L_{\Lambda_X}L\bigr),
$$

the composite of the projection transformation for $Ra_{X!}$ and the
counit $La_X^*Ra_{X*}\to\id$; the *normalized smooth trace*
$\Trsm_{a_X,\Lambda}: \RGammac(X,\Lambda_X(d)[2d])\to\Lambda$ is the
counit of $Ra_{X!}\dashv Ra_X^!$ read through the orientation.
