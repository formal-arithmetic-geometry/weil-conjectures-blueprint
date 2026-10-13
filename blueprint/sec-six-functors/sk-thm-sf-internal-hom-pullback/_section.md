+++
id = "sk-thm-sf-internal-hom-pullback"
kind = "theorem"
title = "Internal Hom versus pullback for a site-perfect first variable"
order = 2506
uses = ["sk-def-sf-operations"]
lean = ["AlgebraicGeometry.Etale.DerivedCategory.nonempty_iso_leftDerivedUpperStar_derivedHom"]
tags = ["sketch"]
+++
Let $\Lambda=A_{E,n}$, let $g:Y'\to X$ be a morphism of schemes, let
$M\in D(X,\Lambda)$ be site-perfect, that is, dualizable — locally on the site,
a bounded complex of finite free $\Lambda$-modules — and let
$N\in D(X,\Lambda)$. Then the canonical comparison

$$
Lg^*\RHom_\Lambda(M,N)\ \xrightarrow{\ \sim\ }\
\RHom_\Lambda\bigl(Lg^*M,Lg^*N\bigr)
$$

is an isomorphism, natural in both variables and compatible with shifts and
with distinguished triangles in $N$.
