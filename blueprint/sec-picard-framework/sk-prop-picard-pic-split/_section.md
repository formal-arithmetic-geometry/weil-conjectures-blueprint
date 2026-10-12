+++
id = "sk-prop-picard-pic-split"
kind = "proposition"
title = "The split exact sequence"
order = 816
uses = ["sk-def-av-jacobian", "sk-def-av-pic"]
lean = ["AlgebraicGeometry.injective_pic_map_snd", "AlgebraicGeometry.pic_map_sectionBaseChange_snd", "AlgebraicGeometry.bijective_toPicardFunctor_picardFunctorNormalized", "AlgebraicGeometry.bijective_pic_split"]
tags = ["sketch"]
+++
Let $f:X\to S$ with a section $\sigma$ and
$\cO_T\overset{\sim}{\to}f_{T,*}\cO_{X_T}$ for all
$T\in\Ob((\Sch/S)_{fppf})$ (for $X\to\Spec k$ a smooth projective
curve with a $k$-point: $H^0(X,\cO_X)=k$ and the flat base change
gives the condition). Then the sequence

$$
0\longrightarrow\Pic(T)\xrightarrow{\ f_T^*\ }\Pic(X_T)
\longrightarrow\Pic_{X/S}(T)\longrightarrow 0
$$

is exact and split by $\sigma_T^*$;
$\Pic(X_T)=\Pic(T)\oplus\Pic_{X/S,\sigma}(T)$, and
$\Pic_{X/S}$ is the sheafification of
$T\mapsto\Pic_{X/S,\sigma}(T)$.
