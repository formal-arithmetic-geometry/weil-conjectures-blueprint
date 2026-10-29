+++
id = "sk-thm-sfb-proper-base-change"
kind = "proposition"
title = "Proper direct image of constructible complexes"
order = 2385
uses = ["sk-def-sfb-constructible"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_of_isProper", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_of_isProper_padicAlgCl"]
tags = ["sketch"]
+++
Let $p\colon X\to Y$ be proper and let $\Lambda$ be admissible. Then
$Rp_*\colon D(X_{\mathrm{proét}},\Lambda)\to D(Y_{\mathrm{proét}},\Lambda)$ maps $\Dctf(X,\Lambda)$
into $\Dctf(Y,\Lambda)$ ([sk-def-sfb-constructible]), and on these categories the canonical
proper base change and projection formula maps are isomorphisms. Explicitly, for a cartesian
square with $g\colon Y'\to Y$, $g'\colon X'\to X$ and $p'\colon X'\to Y'$, the base change map
$g^*Rp_*\to Rp'_*g'^*$ is an isomorphism of functors $\Dctf(X,\Lambda)\to\Dctf(Y',\Lambda)$. The
projection formula map $Rp_*K\otimes^{\mathbf L}M\to Rp_*(K\otimes^{\mathbf L}p^*M)$ is an
isomorphism for $K\in\Dctf(X,\Lambda)$ and $M\in\Dctf(Y,\Lambda)$.

For $Y=\Spec k$ with $k$ algebraically closed, this says that the cohomology groups
$H^i(X,\Qlb)$ of a proper $X$ are finite-dimensional and vanish outside a bounded range of
degrees.
