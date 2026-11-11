+++
kind = "proof"
of = "theorem-comparison-constructible-sheaves"
order = 150
uses = ["proposition-etale-implications", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "proposition-pro-etale-affines-form-basis", "theorem-classical-sheaves-essential-image", "lemma-acyclic-resolutions"]
+++
The preceding proposition treats the case of a single stratum. For a finite
stratification we argue locally, by induction on the number of strata.
Once the sheaves are known to be classical, the equivalences follow from
full faithfulness of $\nu_X^*$ and its version for $D^+$.

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
