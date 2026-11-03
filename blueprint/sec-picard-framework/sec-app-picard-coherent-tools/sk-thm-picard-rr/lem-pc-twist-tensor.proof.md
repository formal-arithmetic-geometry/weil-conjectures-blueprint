+++
kind  = "proof"
of    = "lem-pc-twist-tensor"
+++
By [def-pc-projective-space-twist] the modules
$\mathcal O_P(d)\otimes\mathcal O_P(e)$ and $\mathcal O_P(d+e)$ carry the
bases $e_i^{(d)}\otimes e_i^{(e)}$ and $e_i^{(d+e)}$ over $U_i$, and the
$U_i$ cover $P$ ([def-pc-proj]). For each $i$ let $\varphi_i$ be the
isomorphism $\mathcal O_{U_i}e_i^{(d)}\otimes\mathcal O_{U_i}e_i^{(e)}\to \mathcal O_{U_i}e_i^{(d+e)}$ sending $e_i^{(d)}\otimes e_i^{(e)}$ to
$e_i^{(d+e)}$. On $U_i\cap U_j$ the transition rules give
$e_i^{(d)}\otimes e_i^{(e)}=(x_i/x_j)^d e_j^{(d)}\otimes(x_i/x_j)^e e_j^{(e)}=(x_i/x_j)^{d+e}e_j^{(d)}\otimes e_j^{(e)}$, so $\varphi_i$ and
$\varphi_j$ agree on the overlap. Isomorphisms between
$\mathcal O_P$-modules that agree on the members of an open cover glue
(the sheaf axiom for $\mathcal O_P$, whose sections over the standard
opens are the rings of [def-pc-proj]); the glued map is an
isomorphism because it is one locally
([def-sc-invertible-module]). This is the required canonical
isomorphism.
