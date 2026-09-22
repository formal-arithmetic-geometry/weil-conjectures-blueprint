+++
id = "def-pc-picard-functor"
kind = "definition"
title = "The Picard functor Pic_{X/S}"
order = 4236
lean = ["AlgebraicGeometry.picardFunctor"]
uses = ["def-pc-picard-presheaf", "def-pc-fppf-site", "def-pc-representable-functor"]
+++
Let $f:X\to S$ be a morphism of schemes as in
[def-pc-picard-presheaf]. The *Picard functor* $\operatorname{Pic}_{X/S}$
is the fppf sheafification of the Picard presheaf
[def-pc-picard-presheaf] on $(\mathit{Sch}/S)_{fppf}$
[def-pc-fppf-site]; if it is representable
[def-pc-representable-functor], the representing scheme is
$\underline{\operatorname{Pic}}_{X/S}$ (Stacks Project, Picard Schemes of
Curves, Definition 44.4.1, [Tag
0B9L](https://stacks.math.columbia.edu/tag/0B9L)). For
$S=\operatorname{Spec}(k)$ we write $\operatorname{Pic}_{X/k}$.

Unresolved dependencies: def:sc-pic0
