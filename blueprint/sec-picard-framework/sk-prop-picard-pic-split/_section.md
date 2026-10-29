+++
id = "sk-prop-picard-pic-split"
kind = "lemma"
title = "Rigidification along a section"
order = 609
uses = ["sk-lem-abelian-seesaw", "sk-def-picard-pic", "sec-abelian-varieties", "sec-nagata-compactification"]
lean = ["AlgebraicGeometry.injective_pic_map_snd", "AlgebraicGeometry.pic_map_sectionBaseChange_snd", "AlgebraicGeometry.bijective_toPicardFunctor_picardFunctorNormalized", "AlgebraicGeometry.bijective_pic_split", "AlgebraicGeometry.range_pic_mapHom_snd_eq_ker_toPicardFunctorHom", "AlgebraicGeometry.picMulEquivProdPicardFunctorNormalized", "AlgebraicGeometry.isIso_picardFunctorNormalized_ι_comp_toPicardFunctor", "AlgebraicGeometry.Scheme.Modules.eq_of_pullback_map_eq", "AlgebraicGeometry.isIso_pushforwardUnitMap_pullback_snd_of_geometricallyIntegral"]
tags = ["sketch"]
+++
Let $f:C\to S$ be a morphism of schemes. Suppose that $f$ has a section
$\sigma:S\to C$ and that

$$
\cO_T\longrightarrow f_{T,*}\cO_{C_T}
\quad\text{is an isomorphism for every }T\to S.
\qquad(\ast)
$$

Then $\operatorname{Pic}_{C/S}(T)$ is naturally the set of isomorphism
classes of pairs $(\cL,\alpha)$, with $\cL$ invertible on $C_T$ and
$\alpha:\sigma_T^*\cL\simeq\cO_T$. Every such pair has only the identity
automorphism. There is a split exact sequence

$$
0\longrightarrow\operatorname{Pic}(T)
\xrightarrow{\ f_T^*\ }\operatorname{Pic}(C_T)
\longrightarrow\operatorname{Pic}_{C/S}(T)
\longrightarrow0,
$$

whose retraction is $\sigma_T^*$. Normalization is given by

$$
\cL\longmapsto\cL\otimes f_T^*(\sigma_T^*\cL)^{-1}.
$$

In particular $\operatorname{Pic}(C_T)=\operatorname{Pic}(T)\oplus\operatorname{Pic}_{C/S,\sigma}(T)$,
and $\operatorname{Pic}_{C/S,\sigma}\to\operatorname{Pic}_{C/S}$ is an
isomorphism.

For a smooth proper geometrically connected curve $C$ over a field $k$,
one has $H^0(C,\cO_C)=k$, and flat coherent base change gives $(\ast)$
for $C\to\Spec k$, since every $k$-scheme is flat over $k$. If $C$ has a
$k$-point $P$, the lemma applies with $\sigma=P$ (Stacks Project,
Tag 0B9U).
