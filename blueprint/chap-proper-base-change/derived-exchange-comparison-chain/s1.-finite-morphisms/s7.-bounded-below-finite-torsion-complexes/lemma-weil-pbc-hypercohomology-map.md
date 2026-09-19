+++
id = "lemma-weil-pbc-hypercohomology-map"
kind = "lemma"
title = "Morphism of hypercohomology spectral sequences"
order = 757
uses = ["def-weil-pbc-hypercohomology-filtrations", "def-weil-pbc-truncation-exact-couples", "lemma-weil-pbc-exact-couple-abutment", "lemma-weil-pbc-hypercohomology-convergence", "lemma-weil-pbc-hypercover-exact-couple-map", "prop-weil-proet-finite-proper-base-change"]
+++
The S0 exchange map induces a morphism from the inverse image of the first
spectral sequence to the second, whose $E_2$ component is

$$
g^{-1}R^pf_*\mathcal H^q(K)\longrightarrow
R^pf'_*g'^{-1}\mathcal H^q(K),
$$

the S6 finite-torsion proper-base-change map.

## Proof

Definition [def-weil-pbc-truncation-exact-couples] displays both exact
couples and every structure map. Lemma
[lemma-weil-pbc-hypercover-exact-couple-map] constructs their morphism,
identifies its first page with the S6 map, and checks the differential and
connecting-map sign. Lemma [lemma-weil-pbc-exact-couple-abutment]
proves finite-row convergence and identifies the abutment map with
$\mathcal H^n(\operatorname{Ex}_{\square,K})$. Deriving the exact couples
therefore gives the asserted morphism on every page.
