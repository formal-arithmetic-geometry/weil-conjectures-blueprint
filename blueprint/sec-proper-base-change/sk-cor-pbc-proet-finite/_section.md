+++
id = "sk-cor-pbc-proet-finite"
kind = "corollary"
title = "Classical finite coefficients on the pro-étale site"
order = 2016
lean = ["AlgebraicGeometry.ProEtale.isIso_derivedBaseChangeMap_app_of_isProper"]
uses = ["sk-thm-properbasechange", "sk-thm-pe-constructible-comparison"]
tags = ["sketch"]
+++
Recall that a discrete finite commutative ring $A$ gives a condensed ring
whose pullback $A_X$ is the usual constant coefficient sheaf. Finite rings
are thus coefficient rings in the same sense as $\mathcal O_E$, $E$ and
$\Qlb$, and [sk-thm-properbasechange] gives proper base change at each
finite level for every admissible coefficient ring, including $\Zl$ and $\Ql$.

Let $A$ be a finite commutative ring, $p:X\to Y$ proper, and $g:Y'\to Y$ any
morphism. Let $p':X'\to Y'$ and $g':X'\to X$ be the projections from
$X'=X\times_YY'$. If $K\in D^+_{\mathrm{class}}(X_{\mathrm{proét}},A)$, then
the pro-étale exchange map of [sk-thm-properbasechange]

$$
g^*Rp_*K\longrightarrow Rp'_*g'^*K
$$

is an isomorphism in $D^+(Y'_{\mathrm{proét}},A)$.
