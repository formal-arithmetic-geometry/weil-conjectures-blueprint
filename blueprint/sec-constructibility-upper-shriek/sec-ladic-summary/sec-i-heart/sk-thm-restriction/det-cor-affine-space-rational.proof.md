+++
kind = "proof"
of    = "det-cor-affine-space-rational"
uses = ["sk-prop-p1-adjunction-rational", "sk-lem-sf-mate"]
+++
Let $d=1$, and write $p=q\circ j$ with
$j:\mathbf A^1_V\hookrightarrow\mathbf P^1_V$ the standard open immersion and
$q:\mathbf P^1_V\to V$ the projection. Then $Rp_!=Rq_*\circ j_!$. On the
categories $\Loc(\Dbc(-,\Lambda))$, $j_!$ is left adjoint to $j^*$ (both
preserve these categories), and $Rq_*$ is left adjoint to $q^*(1)[2]$ by
[sk-prop-p1-adjunction-rational]. Composing, $Rp_!$ is left adjoint to
$j^*q^*(1)[2]=p^*(1)[2]$, and uniqueness of right adjoints gives
$p^!\simeq p^*(1)[2]$. For general $d$, write $p$ as a composite of $d$
projections $\mathbf A^k_V\to\mathbf A^{k-1}_V$ and use
$(gf)^!\simeq f^!g^!$ ([sk-lem-sf-mate]).

The functor $p^*(d)[2d]$ preserves $\Dbc$: pullback and the Tate twist send
lisse sheaves on the strata to lisse sheaves on the pulled-back strata, and
shifts preserve boundedness.
