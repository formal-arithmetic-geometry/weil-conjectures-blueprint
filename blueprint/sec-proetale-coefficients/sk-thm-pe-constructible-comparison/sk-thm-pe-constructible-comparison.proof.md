+++
kind = "proof"
of = "sk-thm-pe-constructible-comparison"
uses = ["det-pe-constructible-comparison-local", "det-pe-constructible-comparison-classical", "det-pe-constructible-comparison-equivalence", "lem-cbc-proetale-extension-zero-comparison"]
+++
The preceding proposition [sk-prop-pe-finite-local-systems] handles a single
stratum. For a finite stratification argue locally
([det-pe-constructible-comparison-local]), by induction on the number of
strata. At a given point, shrink to an affine open on which the stratum
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
[det-pe-constructible-comparison-classical]. The same argument with locally
closed constructible pieces covers the local qcqs definition. The derived
statement follows from [sk-cor-pe-classical-derived] and bounded truncation
([det-pe-constructible-comparison-equivalence]). These comparisons are recorded
in Stacks Project, Tag 09AI.
