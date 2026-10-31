+++
kind = "proof"
of = "sk-thm-pe-constructible-comparison"
uses = ["lem-sf-proetale-constructible-origin", "lem-cbc-proetale-extension-zero-comparison", "sk-prop-pe-finite-local-systems", "sk-thm-pe-direct-image-comparison", "sk-cor-pe-classical-derived", "sk-prop-pe-functor-comparison"]
+++
The preceding proposition treats the case of a single stratum. For a finite
stratification we argue locally, by induction on the number of strata.
Given a point, we shrink to an affine open on which the stratum
containing it is closed, with inclusion $i$ and open complement $j$.
The exact sequence

$$
0\longrightarrow j_!j^*F\longrightarrow F
\longrightarrow i_*i^*F\longrightarrow0
$$

reduces the assertion to fewer strata, because on pro-étale sheaves of
modules the functors $j_!$ and $i_*$ preserve classical sheaves, by
(2.10) and Theorem [sk-thm-pe-direct-image-comparison],
and classical sheaves are closed under extensions. Since $\nu_X^*$ is
fully faithful, sheaves that are classical on the members of a Zariski
covering are classical, so the local statement suffices. The
derived statement follows from Corollary [sk-cor-pe-classical-derived]
and bounded truncation; see [Stacks, Tag 09AK](https://stacks.math.columbia.edu/tag/09AK), [Stacks, Tag 09AL](https://stacks.math.columbia.edu/tag/09AL).
