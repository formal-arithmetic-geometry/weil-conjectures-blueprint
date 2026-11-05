+++
kind = "proof"
of = "theorem-comparison-constructible-sheaves--1"
order = 149003
uses = ["definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--2", "proposition-etale-implications--1", "lemma-stability--4", "lemma-stability--6", "lemma-stability--7", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--1", "definition-w-local-w-strictly-local--2", "definition-w-local-w-strictly-local--3", "proposition-w-local-components--1", "example-locally-constant-functions-w-local--1", "proposition-pro-etale-affines-form-basis--2", "theorem-classical-sheaves-essential-image--1"]
+++
On one stratum use Proposition [proposition-locally-constant-sheaves-finite-presentation--1]; induct on the number of strata.

Given a point, we shrink to an affine open on which the stratum
containing it is closed, with inclusion $i$ and open complement $j$.
The exact sequence

$$
0\longrightarrow j_!j^*F\longrightarrow F
\longrightarrow i_*i^*F\longrightarrow0
$$

reduces the assertion to fewer strata, because on pro-étale sheaves of
modules the functors $j_!$ and $i_*$ preserve classical sheaves, by
(2.10) and Theorem [theorem-comparison-direct-images],
and classical sheaves are closed under extensions
(Corollary [corollary-bounded-below-classical-complexes]). Since $\nu_X^*$ is
fully faithful, sheaves that are classical on the members of a Zariski
covering are classical, so the local statement suffices. The
derived statement follows from Corollary [corollary-bounded-below-classical-complexes]
and bounded truncation; see [Stacks, [09AK](https://stacks.math.columbia.edu/tag/09AK), [09AL](https://stacks.math.columbia.edu/tag/09AL)].

*Source:* the proof of Theorem [theorem-comparison-constructible-sheaves].
