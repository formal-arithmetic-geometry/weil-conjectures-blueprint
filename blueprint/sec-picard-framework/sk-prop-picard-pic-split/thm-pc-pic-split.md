+++
id = "thm-pc-pic-split"
kind = "theorem"
title = "The split exact sequence for the Picard functor"
order = 815
uses = ["def-pc-pic-sigma-functor", "def-pc-picard-functor", "def-pc-subfunctor", "lem-pc-pic-exact"]
lean = ["AlgebraicGeometry.injective_pic_map_snd", "AlgebraicGeometry.pic_map_sectionBaseChange_snd", "AlgebraicGeometry.bijective_toPicardFunctor_picardFunctorNormalized", "AlgebraicGeometry.bijective_pic_split"]
+++
Let $f:X\to S$ be a morphism of schemes as in
Definition [def-pc-picard-functor].
Assume $f$ has a section $\sigma$ and that
$\mathcal{O}_T\to f_{T,*}\mathcal{O}_{X_T}$ is an isomorphism for all
$T\in\operatorname{Ob}((\mathit{Sch}/S)_{fppf})$. Then the sequence

$$
0\longrightarrow\operatorname{Pic}(T)\xrightarrow{\ f_T^*\ }\operatorname{Pic}(X_T)
\xrightarrow{\ }\operatorname{Pic}_{X/S}(T)\longrightarrow 0
$$

is exact and split, the splitting being given by
$\sigma_T^*:\operatorname{Pic}(X_T)\to\operatorname{Pic}(T)$ (i.e. for every $T$,
$\operatorname{Pic}(X_T)=\operatorname{Pic}(T)\oplus K(T)$ with
$K(T)=\operatorname{Ker}\sigma_T^*$, and $\operatorname{Pic}_{X/S}$ is the fppf
sheafification of the presheaf $K$).
