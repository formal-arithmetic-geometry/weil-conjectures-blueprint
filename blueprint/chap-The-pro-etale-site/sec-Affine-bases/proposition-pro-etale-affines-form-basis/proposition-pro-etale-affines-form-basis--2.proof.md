+++
kind = "proof"
of = "proposition-pro-etale-affines-form-basis--2"
order = 66004
uses = ["proposition-etale-implications", "lemma-stability", "proposition-pro-etale-affines-form-basis--1"]
+++
A pro-étale affine over $X$ is weakly étale over $X$: choose one affine
étale stage of its presentation, apply the ind-étale implication of
[proposition-etale-implications] over that affine stage, and compose
with its étale map to $X$, using [lemma-stability]. The inclusion is
fully faithful because both categories have all $X$-morphisms as
arrows.

By [proposition-pro-etale-affines-form-basis--1], every object of the
pro-étale site is covered by objects of this subcategory. With the
restricted topology, the inclusion is continuous and identifies
$\affproet{X}$ with a dense subsite. The comparison lemma for dense
subsites, applied with the stated limits in $\mathcal A$, now gives
the equivalence by restriction.
