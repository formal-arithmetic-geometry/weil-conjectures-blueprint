+++
id = "lem-kun-derived-tensor-associative"
kind = "lemma"
title = "Associativity of the derived tensor product"
order = 3036
uses = ["def-kun-derived-tensor", "def-weil-pbc-derived-categories", "lem-kun-derived-tensor-well-defined", "lem-kun-flat-resolution-existence"]
+++
Let $\Lambda$ be a commutative ring and $T$ a scheme. For
$K_1,K_2,K_3\in D(T_{\Et},\Lambda)$ there is a canonical isomorphism

$$
(K_1\kunotimes{\Lambda}K_2)\kunotimes{\Lambda}K_3
\xrightarrow{\ \sim\ }
K_1\kunotimes{\Lambda}(K_2\kunotimes{\Lambda}K_3),
$$

natural in $K_1,K_2,K_3$, induced by the associativity constraint of
the underived tensor product of complexes of
$\Lambda_T$-module sheaves.

## Proof

Choose K-flat models $P_i\to K_i$ with flat terms
([lem-kun-flat-resolution-existence]). By
[def-kun-derived-tensor] and
[lem-kun-derived-tensor-well-defined] both sides are represented
by the total complex of
$P_1\otimes_\Lambda P_2\otimes_\Lambda P_3$, with the two
parenthesizations identified by the associativity constraint of the
underived tensor product of complexes; that identification is natural
and does not depend on the chosen models.
