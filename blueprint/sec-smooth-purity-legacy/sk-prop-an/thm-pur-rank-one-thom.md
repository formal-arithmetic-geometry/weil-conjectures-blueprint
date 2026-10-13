+++
id = "thm-pur-rank-one-thom"
kind = "theorem"
title = "Rank-one Thom isomorphism"
order = 2325
uses = ["def-coefficient-twists-detailed", "def-pur-conventions", "def-pur-vector-bundle-zero-section", "def-weil-derived-cohomology-sheaves", "def-weil-derived-tensor", "def-weil-pbc-etale-origin-witness", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "lem-pur-cfiber-stalk", "lem-pur-divisor-class", "lem-pur-frame-independence", "thm-pur-rank-one-local-calculation"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
let $\pi:E\to B$ be a
vector bundle of constant
rank one, with the zero section $z:B\hookrightarrow E$. The zero
section is an effective Cartier divisor of $E$ (the zero scheme of the
tautological section of $\pi^*E$); let

$$
\operatorname{thom}(E):z_*\Lambda_B\longrightarrow\Lambda_E(1)[2]
$$

be its class $\operatorname{cl}_{z(B)}$ of [lem-pur-divisor-class],
and put

$$
\tau_E:=
R\pi_!\operatorname{thom}(E):
\Lambda_B\longrightarrow R\pi_!\Lambda_E(1)[2].
$$

Then $\tau_E$ is an isomorphism, compatible with base change. Its
inverse $\operatorname{tr}_\pi$ is the *rank-one vector-bundle
trace*. In particular

$$
R\pi_!\Lambda_E\;\cong\;\Lambda_B(-1)[-2].
$$
