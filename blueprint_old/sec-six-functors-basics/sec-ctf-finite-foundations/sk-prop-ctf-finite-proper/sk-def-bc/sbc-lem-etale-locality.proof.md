+++
kind  = "proof"
of    = "sbc-lem-etale-locality"
+++
Restricting to $U_i$ and using the factorizations
$U_i\to V_i\to S$ gives

$$
(f^{-1}g_*\mathcal F)|_{U_i}=f_i^{-1}(g_*\mathcal F|_{V_i})
=f_i^{-1}g_{i,*}\mathcal F_i,
$$

where the first equality is the compatibility of inverse and direct
images with localization of the etale site of
[def-weil-pbc-etale-site] (Sites, Lemma 7.28.2,
[Tag `03EF`](https://stacks.math.columbia.edu/tag/03EF)) and the second uses
$\mathcal F|_{V_i}=\mathcal F_i$, and likewise

$$
(h_*e^{-1}\mathcal F)|_{U_i}=h_{i,*}e_i^{-1}\mathcal F_i.
$$

Since $\{U_i\to X\}$ is an etale covering, a morphism of etale sheaves
whose restrictions to all $U_i$ are isomorphisms is an isomorphism
([def-weil-pbc-etale-site]), which proves (1); the assertions (2)
and (3) are the same argument with the localization compatibility for
the higher direct images and sheafified cohomology
(Cohomology on Sites, Lemma 21.20.4, [Tag `0D6G`](https://stacks.math.columbia.edu/tag/0D6G)), applied
degreewise for the $R^q$'s of [def-weil-pbc-direct-image] and to
$R^q$ of the base-change maps of [sbc-def-base-change-map].
