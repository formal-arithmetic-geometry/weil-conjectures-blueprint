+++
id = "lem-pc-pic-exact"
kind = "lemma"
title = "Exactness of the Picard sequence"
lean = ["AlgebraicGeometry.range_pic_mapHom_snd_eq_ker_toPicardFunctorHom", "AlgebraicGeometry.toPicardFunctor_app_eq_of_iso", "AlgebraicGeometry.exists_iso_tensorObj_of_toPicardFunctor_app_eq", "AlgebraicGeometry.toPicardFunctor_app_eq_iff"]
order = 670
uses = ["def-pc-fppf-site", "def-pc-picard-functor", "def-sc-invertible-module", "def-sc-picard-group", "lem-pc-fpqc-descent"]
+++
Let $f:X\to S$ be a morphism of schemes as in
Definition [def-pc-picard-functor].
If $\mathcal{O}_T\to f_{T,*}\mathcal{O}_{X_T}$ is an isomorphism for all
$T\in\operatorname{Ob}((\mathit{Sch}/S)_{fppf})$, then

$$
0\;\longrightarrow\;\operatorname{Pic}(T)\;\longrightarrow\;\operatorname{Pic}(X_T)\;
\longrightarrow\;\operatorname{Pic}_{X/S}(T)
$$

is an exact sequence for all $T$ (the first map is $f_T^*$, the second the
canonical map).
