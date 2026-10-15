+++
kind  = "proof"
of    = "det-picard-main-geometry"
+++
(1) Let $W\subset H_g$ be the chart of [det-picard-f-representable-chart];
it is an open subscheme of $\underline{\operatorname{Pic}}_{C/k}$
(the inclusion $F\subset\operatorname{Pic}_{C/k}$ is representable by
open immersions), smooth of pure dimension $g$, and contained in
$\underline{\operatorname{Pic}}^g_{C/k}$ (its classes have $\chi=1$, i.e.
degree $g$). For $M\in\underline{\operatorname{Pic}}_{C/k}(k)$ the
translate $M^{-1}W$ is an open subscheme isomorphic to $W$. These
translates cover: a point $t$ with residue field $K$ is a class $\cL_t$
on $C_K$, and [lem-pc-twist] gives $\cM_0$ on $C$ with
$h^0(\cL_t\otimes\cM_{0,K})=1$, $H^1=0$, i.e. $\cL_t\otimes\cM_{0,K}\in F(K)$,
so $t\in M^{-1}W$ for $M=[\cM_0]$. Hence
$\underline{\operatorname{Pic}}_{C/k}$ is locally of finite type and
smooth of pure dimension $g$. The unit $e:\Spec k\to\underline{\operatorname{Pic}}_{C/k}$
is a $k$-point of a scheme locally of finite type over $k$, hence a closed
immersion. The diagonal is the preimage of $e$ under the morphism
$(x,y)\mapsto x y^{-1}$ of
$\underline{\operatorname{Pic}}_{C/k}\times_k\underline{\operatorname{Pic}}_{C/k}$
to $\underline{\operatorname{Pic}}_{C/k}$, so it is a closed immersion and
the scheme is separated.

(2) The universal divisor $D_g\subset C\times H_g$ ([thm-pc-hilb-curves])
gives, after normalization along $P$, a class in
$\operatorname{Pic}_{C/k}(H_g)$ of fibrewise degree $g$, i.e. a morphism
$\alpha:H_g\to\underline{\operatorname{Pic}}^g_{C/k}$. Surjectivity may
be checked on geometric points: for an algebraically closed $K\supseteq k$
and $\cL$ of degree $g$ on $C_K$, Riemann–Roch ([lem-sc-riemann-roch])
gives $h^0(\cL)\ge\chi(\cL)=g+1-g=1$; the zero divisor $D$ of a nonzero
section is an effective Cartier divisor of degree $g$, a $K$-point of
$H_g$, with $\cO(D)\cong\cL$.

(3) By (2), $\underline{\operatorname{Pic}}^g_{C/k}$ is the image of the
quasi-compact $H_g$, hence quasi-compact, hence (being locally of finite
type) of finite type. It is separated by (1), and it is the surjective
image of the proper $k$-scheme $H_g$, so it is universally closed, hence
proper. As the image of the irreducible $H_g$ it is irreducible, and
since $\alpha_K$ stays surjective for every field extension $K/k$ and
$(H_g)_K$ is irreducible ([thm-pc-hilb-curves]: $H_g$ is geometrically
integral), it is geometrically irreducible. It is smooth of dimension $g$
by (1), hence a smooth proper geometrically irreducible variety of
dimension $g$. By [det-picard-main-degree] (3), tensoring with
$\cO_C((d-g)P)$ identifies it with every $\underline{\operatorname{Pic}}^d_{C/k}$.
