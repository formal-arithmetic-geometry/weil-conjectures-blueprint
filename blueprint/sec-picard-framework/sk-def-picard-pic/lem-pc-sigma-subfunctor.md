+++
id = "lem-pc-sigma-subfunctor"
kind = "lemma"
title = "$\\operatorname{Pic}_{X/k,\\sigma}$ is a subfunctor of the Picard presheaf"
lean = ["AlgebraicGeometry.picardPresheaf_map_mem_picardFunctorNormalized"]
order = 579
uses = ["def-pc-base-change", "def-pc-pic-sigma-functor", "def-pc-picard-presheaf", "def-pc-rational-point", "def-pc-subfunctor", "def-sc-picard-group"]
+++
Let $f:X\to S$ be a morphism of schemes and $\sigma:S\to X$ a section
of $f$ (for instance $S=\operatorname{Spec}(k)$ for a field $k$ and
$\sigma\in X(k)$ a $k$-rational point, [def-pc-rational-point]). Then the
assignment

$$
T\longmapsto\operatorname{Ker}\Bigl(\sigma_T^*:\operatorname{Pic}(X_T)
\longrightarrow\operatorname{Pic}(T)\Bigr)
$$

of [def-pc-pic-sigma-functor] is a
subfunctor of the
Picard presheaf on the category of
schemes over $S$.
