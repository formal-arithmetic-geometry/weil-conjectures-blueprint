+++
id = "theorem-pure-lisse-sheaves-over-relative--1"
kind = "theorem"
title = "Punctual bounds, reality and mixedness over relative affine curves"
name_showing = false
order = 1345001
aliases = ["bp-r416-1"]
lean = ["AlgebraicGeometry.hasWeightsAtMost_higherLowerShriek_of_isAffine_fiber", "AlgebraicGeometry.isReal_higherLowerShriek_of_isAffine_fiber", "AlgebraicGeometry.exists_isMixedOfWeightsAtMost_higherLowerShriek_of_isAffine_fiber"]
uses = ["definition-weil-structure", "definition-lisse-sheaves", "definition-weights", "definition-real-sheaves", "proposition-construction-independence-rf-shriek"]
+++
Let $k_0=\Fq$, fix $\iota:\overline{\mathbf Q}_\ell\hookrightarrow\mathbf C$
with $\ell\nmid q$, and let $h:U_0\to Y_0$ be a smooth separated
morphism of relative dimension one between separated finite-type
$k_0$-schemes, with affine fibres. Let $F$ be a lisse Weil sheaf on
$U_0$, punctually $\iota$-pure of weight $w\in\mathbf R$. For every
$i\in\mathbf N$ the following statements hold.

1. The sheaf $R^ih_!F$ is punctually of weights at most $w+i$:
   at every closed point $y$ of $Y_0$, every eigenvalue $\alpha$ of $\operatorname{Frob}_y$ on
   $(R^ih_!F)_{\bar y}$ satisfies
   $|\iota(\alpha)|\le q_y^{(w+i)/2}$.
2. If $E$ is a lisse $\iota$-real Weil sheaf on $U_0$, punctually
   $\iota$-pure of weight zero, then $R^ih_!E$ is $\iota$-real.
3. There is $v\in\mathbf R$ such that $R^ih_!F$ is $\iota$-mixed
   of weights at most $v$.
