+++
id = "lemma-rigidification-along-section--1"
kind = "lemma"
title = "Rigidification along a section (1)"
name_showing = false
order = 1520001
aliases = ["bp-r474-1"]
lean = ["AlgebraicGeometry.picardFunctorNormalized", "AlgebraicGeometry.bijective_toPicardFunctor_picardFunctorNormalized"]
uses = ["definition-relative-picard-functor"]
+++
Let $f:C\to S$ be a morphism of schemes with a section $\sigma:S\to C$.
The normalized Picard functor is the subfunctor

$$
\operatorname{Pic}_{C/S,\sigma}(T)
=\{[\mathcal L]\in\operatorname{Pic}(C_T):
\sigma_T^*\mathcal L\simeq\mathcal O_T\}
$$

of $T\mapsto\operatorname{Pic}(C_T)$, with maps given by pullback.
Suppose that

$$
\mathcal O_T\longrightarrow f_{T,*}\mathcal O_{C_T}
\quad\text{is an isomorphism for every }T\to S.
\tag{$\ast$}
$$

Then the inclusion followed by the sheafification map induces a bijection

$$
\operatorname{Pic}_{C/S,\sigma}(T)
\longrightarrow\operatorname{Pic}_{C/S}(T)
$$

for every $T\to S$, naturally in $T$.
Here a normalized class records that $\sigma_T^*\mathcal L$ is trivial;
it does not include a chosen trivialization.
