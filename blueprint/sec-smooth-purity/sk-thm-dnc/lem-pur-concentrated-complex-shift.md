+++
id = "lem-pur-concentrated-complex-shift"
kind = "lemma"
title = "Complexes with cohomology in a single degree"
order = 2344
uses = ["def-pur-conventions", "def-sbc-smooth-morphisms", "def-weil-derived-cohomology-sheaves", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "lem-cbc-proetale-stalk-conservative"]
+++
In the purity conventions of [def-pur-conventions],
let $T$ be a separated
finite-type $k$-scheme, let $K\in D^b_{ctf}(T,\Lambda)$ and let
$r\in\mathbf Z$.

1. *concentration in one degree.* If the
[def-weil-derived-cohomology-sheaves] cohomology sheaves
$\mathcal H^i(K)$ vanish for every $i\neq r$, then the
truncation triangles induce a canonical isomorphism
$$
K\;\xrightarrow{\ \sim\ }\;\mathcal H^r(K)[-r].
$$
1. *local constancy detected on an etale cover.* Let
$u:U\to T$ be a surjective
etale morphism and suppose
that $Lu^*K\cong\underline L[-r]$ for a
locally constant
$\Lambda$-sheaf $\underline L$ with finite stalks on $U$.
Then $\mathcal H^i(K)=0$ for every $i\neq r$, and
$\mathcal H^r(K)$ is locally constant with finite stalks on
$T$.
