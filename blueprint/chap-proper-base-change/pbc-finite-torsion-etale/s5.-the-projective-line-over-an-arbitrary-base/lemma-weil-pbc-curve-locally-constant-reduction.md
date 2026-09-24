+++
id = "lemma-weil-pbc-curve-locally-constant-reduction"
kind = "lemma"
title = "Locally constant sheaf reduction"
order = 1681
uses = ["lemma-weil-pbc-finite-exchange", "lemma-weil-pbc-finite-l-group-filtration"]
+++
For irreducible $U$ and finite locally constant $G$ of
$\mathbf F_\ell$-vector spaces, there is a finite etale
$v:V\to U$ of degree prime to $\ell$ such that $v^{-1}G$ has a filtration by
constant $\mathbf F_\ell$-sheaves, and $G$ is a direct summand of
$v_*v^{-1}G$.

## Proof

Choose a geometric point $\bar u$ of $U$. The locally constant sheaf gives
a representation

$$
\rho:\pi_1(U,\bar u)\longrightarrow
\operatorname{GL}_{\mathbf F_\ell}(G_{\bar u})
$$

with finite image $Q$. If $H\subseteq Q$ is an $\ell$-Sylow subgroup, the
inverse image $\rho^{-1}(H)$ defines a connected finite etale cover
$v:V\to U$ of degree $d=[Q:H]$, which is prime to $\ell$. On $V$, the
monodromy factors through $H$.

The representation filtration gives
$0=V_0\subset V_1\subset\cdots\subset V_m=G_{\bar u}$ with
$V_a/V_{a-1}\cong\mathbf F_\ell$ and trivial $H$-action. Passing from
$H$-modules to locally constant sheaves gives, for every $a$, the explicit
short exact sequence

$$
0\longrightarrow G_{a-1}\longrightarrow G_a\longrightarrow
\underline{\mathbf F_\ell}_V\longrightarrow0,
\qquad G_m=v^{-1}G.
$$

All inclusions, quotient maps, and connecting maps commute with extension of
the algebraically closed ground field.

The adjunction unit and the fibrewise sum are

$$
\eta:G\longrightarrow v_*v^{-1}G,\qquad
\operatorname{tr}:v_*v^{-1}G\longrightarrow G.
$$

At a geometric stalk, $\eta(s)=(s,\ldots,s)$ in the direct sum indexed by
the $d$ points of the fibre, while
$\operatorname{tr}(s_1,\ldots,s_d)=\sum_as_a$. Consequently
$\operatorname{tr}\circ\eta=d\,\operatorname{id}_G$. Multiplication by
$d^{-1}\in\mathbf F_\ell$ defines
$r=d^{-1}\operatorname{tr}$ with $r\eta=\operatorname{id}_G$.
The stalk formulas are preserved by base change, so the direct-summand
decomposition and every filtration exact sequence are compatible with the
cohomology comparison maps.
