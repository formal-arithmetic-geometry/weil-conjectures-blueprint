+++
id = "lemma-rigidification-along-section--3"
kind = "lemma"
title = "Rigidification along a section (3)"
name_showing = false
order = 1523005
aliases = ["bp-r474-3"]
lean = ["AlgebraicGeometry.bijective_pic_split", "AlgebraicGeometry.injective_pic_map_snd", "AlgebraicGeometry.range_pic_mapHom_snd_eq_ker_toPicardFunctorHom", "AlgebraicGeometry.surjective_toPicardFunctorHom", "AlgebraicGeometry.pic_map_sectionBaseChange_snd"]
uses = ["definition-relative-picard-functor", "definition-relative-picard-functor--1"]
+++
Let $f:C\to S$ have a section $\sigma:S\to C$, and suppose that
$\mathcal O_U\to f_{U,*}\mathcal O_{C_U}$ is an isomorphism for every
$U\to S$. Write $q_T:\operatorname{Pic}(C_T)\to\operatorname{Pic}_{C/S}(T)$
for the sheafification map. For every $T\to S$, the map

$$
\operatorname{Pic}(C_T)\longrightarrow
\operatorname{Pic}(T)\times\operatorname{Pic}_{C/S}(T),
\qquad
[\mathcal L]\longmapsto
\bigl([\sigma_T^*\mathcal L],q_T([\mathcal L])\bigr)
$$

is bijective.
Together with $\sigma_T^*f_T^*=\mathrm{id}$ and the fact that two classes
have the same image under $q_T$ exactly when they differ by a class
pulled back from $T$, it gives the split exact sequence

$$
0\longrightarrow\operatorname{Pic}(T)
\xrightarrow{f_T^*}\operatorname{Pic}(C_T)
\longrightarrow\operatorname{Pic}_{C/S}(T)
\longrightarrow0,
$$

whose retraction is $\sigma_T^*$.
