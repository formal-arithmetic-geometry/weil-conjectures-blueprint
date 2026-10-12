+++
id = "lem-amb-closed-support-hom"
kind = "lemma"
title = "Closed support as a relative section complex"
order = 1907
uses = ["def-weil-pbc-derived-categories", "def-weil-pbc-etale-sheaves", "def-weil-scheme-morphism-properties", "lem-amb-etale-adjoint-locality", "lemma-weil-pbc-finite-direct-image-exact", "lemma-weil-pbc-geometric-stalk-conservative"]
+++
Let $i:D\hookrightarrow T$ be a closed immersion,
with complementary open immersion $v:V\hookrightarrow T$.
For a complex $K$ of etale $A$-module sheaves,
there is a natural isomorphism of ordinary derived
$A$-module complexes

$$
R\operatorname{Hom}_T(i_*A_D,K)
\cong\operatorname{Cone}\bigl(R\Gamma(T,K)
\longrightarrow R\Gamma(V,v^*K)\bigr)[-1].
$$
