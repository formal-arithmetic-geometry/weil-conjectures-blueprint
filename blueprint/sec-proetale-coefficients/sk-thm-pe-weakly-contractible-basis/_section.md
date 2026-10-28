+++
id = "sk-thm-pe-weakly-contractible-basis"
kind = "theorem"
title = "Enough affine weakly contractible objects"
order = 964
lean = ["AlgebraicGeometry.Scheme.ProEt.exists_isWContractibleRing_cover", "AlgebraicGeometry.Scheme.ProEt.isWeaklyContractible_of_iso"]
uses = ["sk-thm-pe-wc-cover", "sk-thm-pe-indetale-refinement", "sk-prop-pe-wc-rings", "sk-def-pe-site"]
tags = ["sketch"]
+++
Every object of $X_{\mathrm{proét}}$ has a covering by affines $U=\operatorname{Spec}(D)$
with $D$ w-contractible. For such $U$, every epimorphism of sheaves $F\to h_U$ has a
section. Equivalently, $h_U$ is projective in $\Sh(X_{\mathrm{proét}})$.
