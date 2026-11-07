+++
id = "lemma-rigidification-along-section--1"
kind = "lemma"
title = "Rigidification along a section (1)"
name_showing = false
order = 1523001
aliases = ["bp-r474-1"]
lean = ["AlgebraicGeometry.picardFunctorNormalized", "AlgebraicGeometry.bijective_toPicardFunctor_picardFunctorNormalized", "AlgebraicGeometry.isIso_picardFunctorNormalized_ι_comp_toPicardFunctor"]
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
