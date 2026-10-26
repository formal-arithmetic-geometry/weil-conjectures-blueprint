+++
id = "def-pc-picard-presheaf"
kind = "definition"
title = "The Picard presheaf"
lean = ["AlgebraicGeometry.picardPresheaf", "AlgebraicGeometry.Scheme.Pic.map", "AlgebraicGeometry.Scheme.Pic.map_id", "AlgebraicGeometry.Scheme.Pic.map_comp"]
order = 568
uses = ["def-pc-base-change", "def-sc-picard-group", "def-sc-invertible-module"]
+++
Let $f:X\to S$ be a morphism of schemes. The *Picard presheaf* is

$$
(\mathit{Sch}/S)^{\mathrm{op}}\longrightarrow\textit{Sets},\qquad
T\longmapsto\operatorname{Pic}(X_T),
$$

with $\operatorname{Pic}$ of [def-sc-picard-group] (in the generality of
[rem-pc-sc-modules]) and $X_T$ of [def-pc-base-change].
For $g:T'\to T$ with $g_X:X_{T'}\to X_T$, the map $\mathcal L\mapsto g_X^*\mathcal L$
sends invertible modules to invertible modules and respects isomorphisms, and
$(g_1\circ g_2)^*=g_2^*g_1^*$, $(\mathrm{id})^*=\mathrm{id}$; so this is a functor.
