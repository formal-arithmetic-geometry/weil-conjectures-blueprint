+++
id = "lem-weil-pbc-exchange-geometric-stalk"
kind = "lemma"
title = "Exchange on a geometric stalk"
order = 1725
uses = ["def-weil-pbc-derived-exchange-detailed", "def-weil-pbc-etale-sheaves", "prop-weil-pbc-strict-henselization-stalk-formula-detailed", "prop-weil-pbc-strict-local-exchange"]
+++
Let $p:\mathbf P^1_S\to S$, let $g:T\to S$, and let $\bar t\to T$ have image
$\bar s\to S$. For a torsion sheaf $F$ and every $q$, the stalk of the
exchange morphism [def-weil-pbc-derived-exchange-detailed] is the canonical restriction

$$
 H^q(\mathbf P^1_{\kappa(\bar s)},F|)
 \longrightarrow
 H^q(\mathbf P^1_{\kappa(\bar t)},F|),
$$

where both residue fields are separably closed.

## Proof

The strict-henselization stalk formula
[prop-weil-pbc-strict-henselization-stalk-formula-detailed] identifies the source and
target stalks with cohomology over the two strict local bases, and the
strict-local comparison of [prop-weil-pbc-strict-local-exchange] identifies
those with the cohomologies of the closed fibres displayed above; expanding
the unit--$\theta_\square$--counit composite of
[def-weil-pbc-derived-exchange-detailed] shows that the induced map is the
field-extension pullback.
