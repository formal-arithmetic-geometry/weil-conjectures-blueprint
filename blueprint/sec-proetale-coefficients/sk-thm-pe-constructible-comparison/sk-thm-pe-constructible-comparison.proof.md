+++
kind = "proof"
of = "sk-thm-pe-constructible-comparison"
uses = ["lem-sf-proetale-constructible-origin", "lem-cbc-proetale-extension-zero-comparison", "sk-prop-pe-finite-local-systems", "sk-thm-pe-direct-image-comparison", "sk-cor-pe-classical-derived"]
+++
The preceding proposition [sk-prop-pe-finite-local-systems] handles a single
stratum. For a finite stratification argue locally on $X$, by induction on
the number of strata. At a given point, shrink to an affine open on which the stratum
containing it is closed, with inclusion $i$ and open complement $j$. The exact
sequence

$$
0\longrightarrow j_!j^*F\longrightarrow F\longrightarrow i_*i^*F\longrightarrow0
$$

reduces the assertion to fewer strata, because $j_!$ and $i_*$ on pro-étale
module sheaves preserve classical sheaves by the functor comparisons
([lem-cbc-proetale-extension-zero-comparison],
[sk-thm-pe-direct-image-comparison]) and classical sheaves are closed under
extensions ([sk-cor-pe-classical-derived]); see
[lem-sf-proetale-constructible-origin]. The derived statement follows from
[sk-cor-pe-classical-derived] and bounded truncation. These comparisons are recorded
in Stacks Project, Tags 09AK (sheaves) and 09AL (bounded-below complexes).
