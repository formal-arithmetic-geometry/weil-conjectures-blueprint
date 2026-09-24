+++
id = "lem-weil-pbc-exact-couple-differential"
kind = "lemma"
title = "Compatibility of the exact-couple differential"
order = 1746
uses = ["def-sp-exact-couple", "def-weil-pbc-derived-exchange-detailed", "def-weil-pbc-truncation-exact-couples-detailed", "lem-sp-couple-morphism"]
+++
Using the standard cohomological cone convention, the morphism of
[def-weil-pbc-truncation-exact-couples-detailed] commutes with the connecting
maps and with every differential of the two spectral sequences. Its $E_2$ map
is the derived exchange morphism for the torsion cohomology sheaf $\mathcal
H^q(K)$; explicitly, in bidegree $(p,q)$ it is

$$
 g^{-1}R^pf_*\mathcal H^q(K)\longrightarrow
 R^pf'_*g'^{-1}\mathcal H^q(K).
$$

## Proof

The datum of [def-weil-pbc-truncation-exact-couples-detailed] is a morphism of
exact couples: the exchange morphisms of [def-weil-pbc-derived-exchange-detailed] on
the three terms of each truncation triangle commute with the connecting maps
by naturality, so the structure maps $\alpha,f,g$ are preserved. A morphism of
exact couples therefore induces morphisms of the two spectral sequences
compatible with every differential, and the connecting maps being part of the
exact-couple structure, the compatibility covers them. The $E_2$-map in
bidegree $(p,q)$ is the first graded component of the couple morphism, namely
the derived exchange morphism of [def-weil-pbc-derived-exchange-detailed] for the
torsion cohomology sheaf $\mathcal H^q(K)$, as displayed.
