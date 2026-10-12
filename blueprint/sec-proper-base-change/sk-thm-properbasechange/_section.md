+++
id = "sk-thm-properbasechange"
kind = "theorem"
title = "Proper base change"
order = 1252
lean = ["AlgebraicGeometry.Etale.isIso_baseChange_of_isProper"]
uses = ["sk-def-conv", "sk-def-exchange"]
tags = ["sketch"]
+++
Let $\Lambda$ be a commutative ring, let $f:X\to Y$ be a proper morphism,
and let $g:Y'\to Y$ be an arbitrary morphism, with base change
$f':X'=X\times_YY'\to Y'$ and $g':X'\to X$. For every object $K$ of
$\Dplus(X_{\Et},\Lambda)$ all of whose cohomology sheaves are torsion,
the exchange morphism

$$
\Ex_{\square,K}:g^{-1}Rf_*K\xrightarrow{\ \sim\ }Rf'_*g'^{-1}K
$$

is an isomorphism in $\Dplus(Y'_{\Et},\Lambda)$. In particular
$\mathrm{PBC}(f)$ holds in the sense of [sk-def-pbc].
