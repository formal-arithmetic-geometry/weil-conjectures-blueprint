+++
id = "cor-pc-sigma-pic-iso"
kind = "theorem"
title = "$\\operatorname{Pic}_{X/k,\\sigma}$ is isomorphic to $\\operatorname{Pic}_{X/k}$"
lean = ["AlgebraicGeometry.isRepresentable_picardFunctorNormalized_iff", "AlgebraicGeometry.nonempty_picardFunctorNormalized_iso_picardFunctor", "AlgebraicGeometry.isIso_picardFunctorNormalized_\u03b9_comp_toPicardFunctor_of_geometricallyIntegral", "AlgebraicGeometry.isRepresentable_picardFunctorNormalized_iff_of_geometricallyIntegral", "AlgebraicGeometry.nonempty_picardFunctorNormalized_iso_picardFunctor_of_isIntegral"]
order = 632
tags = ["latex:corollary"]
uses = ["def-pc-pic-sigma-functor", "def-pc-picard-functor", "lem-pc-k-sheaf", "lem-pc-rational-hyp", "thm-pc-pic-split"]
+++
Let $k$ be a field and let $X$ be a smooth projective curve over $k$ (more
generally, an integral proper scheme over $k$, or a scheme smooth of
relative dimension $1$, proper and geometrically integral over $k$) with
a $k$-rational point $\sigma$. Then the functors
$\operatorname{Pic}_{X/k,\sigma}$ and
$\operatorname{Pic}_{X/k}$ on
$(\mathit{Sch}/k)_{fppf}$ are isomorphic. In particular
$\operatorname{Pic}_{X/k,\sigma}$ is an fppf sheaf (represented once $\operatorname{Pic}_{X/k}$ is;
and covariantly: if $\operatorname{Pic}_{X/k,\sigma}$ is representable, then so is
$\operatorname{Pic}_{X/k}$, by the group law of [thm-pc-pic-split]).
