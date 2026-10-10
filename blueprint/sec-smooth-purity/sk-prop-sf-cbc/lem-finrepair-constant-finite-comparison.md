+++
id = "lem-finrepair-constant-finite-comparison"
kind = "lemma"
title = "Constant coefficients under a finite normalization comparison"
order = 1615
uses = ["def-weil-pbc-constructible-complexes", "def-weil-pbc-direct-image", "def-weil-pbc-scheme-conventions", "lem-fin-closed-immersion", "lem-fin-finite-morphism", "lem-weil-pbc-grothendieck-spectral-sequence", "lemma-weil-pbc-finite-stalk-formula", "lemma-weil-pbc-geometric-stalk-conservative", "sbc-def-coefficient-conventions", "thm-constructible-serre"]
+++
Let $f:X\to S$ be proper between finite-type $k$-schemes and
let $\nu:Y\to X$ be finite and surjective, in the conventions of
[def-weil-pbc-scheme-conventions]. Suppose $\nu$ is an
isomorphism outside a reduced closed subscheme $i:Z\hookrightarrow X$
for which $f|_Z$ is finite. Put $v=f\nu$, and let $M$ be a
finite module over the ring of [sbc-def-coefficient-conventions].
If all $R^qv_*\underline M$ are constructible, then so are all
$R^qf_*\underline M$. Moreover the natural map

$$
R^qf_*\underline M\longrightarrow R^qv_*\underline M
$$

is an isomorphism for every $q\geq2$.
Here constructibility and direct image have the meanings of
[def-weil-pbc-constructible-complexes], [def-weil-pbc-direct-image].
