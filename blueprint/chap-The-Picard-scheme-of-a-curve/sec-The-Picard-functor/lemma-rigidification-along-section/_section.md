+++
id = "lemma-rigidification-along-section"
kind = "lemma"
title = "Rigidification along a section"
order = 1523
lean = ["AlgebraicGeometry.isIso_picardFunctorNormalized_ι_comp_toPicardFunctor", "AlgebraicGeometry.picMulEquivProdPicardFunctorNormalized", "AlgebraicGeometry.picardFunctorNormalized", "AlgebraicGeometry.bijective_toPicardFunctor_picardFunctorNormalized"]
uses = ["definition-relative-picard-functor"]
+++
Suppose that $f$ has a section $\sigma:S\to C$ and that

$$
\mathcal O_T\longrightarrow f_{T,*}\mathcal O_{C_T}
\quad\text{is an isomorphism for every }T\to S.
\tag{$\ast$}
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
