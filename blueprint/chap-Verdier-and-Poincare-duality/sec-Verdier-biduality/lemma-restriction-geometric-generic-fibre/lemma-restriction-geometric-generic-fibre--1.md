+++
id = "lemma-restriction-geometric-generic-fibre--1"
kind = "lemma"
title = "Open direct image under generic base change"
name_showing = false
order = 838001
aliases = ["bp-r251-1"]
lean = ["AlgebraicGeometry.Etale.isIso_derivedBaseChangeMap_app_of_isOpenImmersion_of_generic"]
uses = ["definition-constructible-sheaves", "definition-derived-base-change-map"]
+++
Let $B$ be an integral scheme of finite type over a field $k$, let $A$
be a finite commutative ring whose exponent is invertible on $B$, and let
$t:S\to B$ be a morphism from a noetherian scheme such that every point
of $S$ maps to the generic point of $B$. Work on the classical étale sites.
Let $X$ be of finite type over $B$, let $j:U\hookrightarrow X$ be an
open immersion, and write $g_X:X_S\to X$, $g_U:U_S\to U$ and
$j_S:U_S\hookrightarrow X_S$ for the base changes. For every
$L\in\Dbc(U,A)$ the canonical map

$$
g_X^*Rj_*L\longrightarrow Rj_{S,*}g_U^*L
$$

is an isomorphism. In particular, this applies to
$S=\operatorname{Spec}\overline{k(B)}$.
