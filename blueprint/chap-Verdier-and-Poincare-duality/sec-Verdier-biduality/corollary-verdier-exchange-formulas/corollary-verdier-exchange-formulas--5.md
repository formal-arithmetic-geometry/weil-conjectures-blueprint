+++
id = "corollary-verdier-exchange-formulas--5"
kind = "corollary"
title = "Open extension by zero"
order = 847006
aliases = ["bp-r254-5"]
lean = ["AlgebraicGeometry.Etale.verdierDualLowerShriekIso"]
uses = ["definition-verdier-dual-evaluation", "definition-compactification-refinement"]
+++
Let $\Lambda$ be a finite commutative ring, $j:U\hookrightarrow X$ a
quasi-compact open immersion, and $a_X:X\to S$ a morphism. Put
$a_U=a_X\circ j$ and assume that $j$, $a_X$, and $a_U$ admit
compactifications. For the Verdier duals relative to $S$ on the small
étale sites, there is a natural isomorphism on
$D(U_{\mathrm{\acute{e}t}},\Lambda)$,

$$
\mathbb D_Xj_{!,\Lambda}\simeq Rj_{*,\Lambda}\mathbb D_U.
$$

Here $j_{!,\Lambda}$ is the exact extension by zero applied to complexes.
No boundedness or constructibility hypothesis is imposed. The tagged
construction gives this natural isomorphism by identifying $Rj_!$ with
$j_!$; more generally, it accepts a tensor–Hom exchange, an isomorphism
$j^!\omega_X\simeq\omega_U$, and an identification $Rj_!\simeq G$,
and produces $\mathbb D_XG\simeq Rj_*\mathbb D_U$.
