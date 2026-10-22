+++
id = "lem-pc-f-open-subfunctor"
kind = "lemma"
title = "$F$ is an open subfunctor"
order = 830
uses = ["def-pc-derived-category", "def-pc-f-subfunctor", "def-pc-pic-sigma-functor", "def-pc-subfunctor", "def-sc-invertible-module", "lem-pc-flat-rf-open", "lem-pc-smooth-flat"]
lean = ["AlgebraicGeometry.isOpenImmersion_picardFunctorInvertibleDirectImage_ι", "AlgebraicGeometry.exists_opens_isInvertibleDirectImage_map_iff", "AlgebraicGeometry.IsInvertibleDirectImage.map_of_isProper"]
+++
Let $k$ be a field, let $X$ be a $k$-scheme which is
proper, smooth of relative dimension $1$ and geometrically integral over
$k$, with a $k$-rational point $\sigma$, and let
$F\subseteq\operatorname{Pic}_{X/k,\sigma}$ be the
subfunctor

$$
F(T):=\{\mathcal{L}\in\operatorname{Pic}_{X/k,\sigma}(T):Rf_{T,*}\mathcal{L}\text{ is isomorphic to an
invertible }\mathcal{O}_T\text{-module placed in degree }0\}.
$$

Then $F$ is a subfunctor of $\operatorname{Pic}_{X/k,\sigma}$ and the inclusion
$F\subseteq\operatorname{Pic}_{X/k,\sigma}$ is
representable by open immersions.
