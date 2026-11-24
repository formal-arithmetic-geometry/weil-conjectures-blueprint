+++
id = "prose-10-05"
kind = "hidden"
title = "Verdier biduality (1)"
order = 833
+++
On a smooth curve $C$ over an algebraically closed field, with
$\href{@definition-verdier-dual-evaluation}{\omega_C}=\href{@definition-tate-twists}{\Lambda_C(1)}[2]$, [biduality](@theorem-verdier-biduality) is easy to see for the two basic kinds of sheaves. Indeed, for a locally constant sheaf $L$ of free
$\Lambda$-modules the dual is $\href{@definition-tate-twists}{L^\vee(1)}[2]$, and dualizing twice gives
back $L$. For a skyscraper $i_*M$ at a closed point $i:x\to C$, the
[exchange formula](@lemma-internal-adjunction-two-exchange-formulas) $\href{@definition-verdier-dual-evaluation}{\mathbb D_C}i_*\simeq i_*\href{@definition-verdier-dual-evaluation}{\mathbb D_x}$ for the proper
map $i$ shows that the dual is $i_*\href{@definition-verdier-dual-evaluation}{\mathbb D_xM}$, so biduality reduces
to biduality on the point. In general, a [constructible sheaf](@definition-constructible-sheaves) is an extension of $i_*M$ by $j_!L$, where
now $i$ is the inclusion of a finite set of closed points and $L$ is
locally constant on its complement $j:U\hookrightarrow C$. The open piece is the difficult one: we have $\href{@definition-verdier-dual-evaluation}{\mathbb D_C(j_!L)}\simeq Rj_*\href{@definition-verdier-dual-evaluation}{\mathbb D_UL}$, and to dualize $Rj_*$ we would need
the second [exchange formula](@corollary-verdier-exchange-formulas). That formula, however, depends on [biduality](@theorem-verdier-biduality). In dimension one this can still be checked by hand, using the cohomology of the henselian punctured disc, whereas in higher dimension the direct images
$Rj_*$ along the boundary of a stratum have no such description.
