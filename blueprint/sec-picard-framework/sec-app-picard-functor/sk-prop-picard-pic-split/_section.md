+++
id = "sk-prop-picard-pic-split"
kind = "lemma"
title = "Rigidification along a section"
order = 878
lean = ["AlgebraicGeometry.injective_pic_map_snd", "AlgebraicGeometry.pic_map_sectionBaseChange_snd", "AlgebraicGeometry.bijective_toPicardFunctor_picardFunctorNormalized", "AlgebraicGeometry.bijective_pic_split", "AlgebraicGeometry.range_pic_mapHom_snd_eq_ker_toPicardFunctorHom", "AlgebraicGeometry.picMulEquivProdPicardFunctorNormalized", "AlgebraicGeometry.isIso_picardFunctorNormalized_ι_comp_toPicardFunctor", "AlgebraicGeometry.Scheme.Modules.eq_of_pullback_map_eq", "AlgebraicGeometry.isIso_pushforwardUnitMap_pullback_snd_of_geometricallyIntegral"]
uses = ["sk-lem-abelian-seesaw", "sk-def-picard-pic", "sec-abelian-varieties", "sec-nagata-compactification"]
tags = ["sketch"]
+++
Suppose that $f$ has a section $\sigma:S\to C$ and that

$$
\mathcal O_T\longrightarrow f_{T,*}\mathcal O_{C_T}
\quad\text{is an isomorphism for every }T\to S.
\tag{*}
$$

Then $\operatorname{Pic}_{C/S}(T)$ is identified, functorially in $T$,
with the set of isomorphism classes of pairs $(\mathcal L,\alpha)$, with $\mathcal L$ invertible on
$C_T$ and $\alpha:\sigma_T^*\mathcal L\simeq\mathcal O_T$.
Every such pair has only the identity automorphism. There is a split
exact sequence

$$
0\longrightarrow\operatorname{Pic}(T)
\xrightarrow{f_T^*}\operatorname{Pic}(C_T)
\longrightarrow\operatorname{Pic}_{C/S}(T)
\longrightarrow0,
$$

whose retraction is $\sigma_T^*$. The normalization map is

$$
\mathcal L\longmapsto
\mathcal L\otimes f_T^*(\sigma_T^*\mathcal L)^{-1}.
$$
