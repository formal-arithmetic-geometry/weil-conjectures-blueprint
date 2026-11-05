+++
id = "lemma-restriction-geometric-generic-fibre--2"
kind = "lemma"
title = "Closed exceptional inverse image under generic base change"
name_showing = false
order = 838002
aliases = ["bp-r251-2"]
lean = ["AlgebraicGeometry.Etale.isIso_rightDerivedUpperShriekBaseChangeMap_app_of_generic"]
uses = ["definition-constructible-sheaves", "definition-exceptional-base-change-map"]
+++
Let $B$ be an integral scheme of finite type over a field $k$, let $A$
be a finite commutative ring whose exponent is invertible on $B$, and let
$t:S\to B$ be a morphism from a noetherian scheme such that every point
of $S$ maps to the generic point of $B$. Work on the classical étale sites.
Let $X$ be of finite type over $B$, and let $i:Z\hookrightarrow X$ be
a closed immersion with open complement $j:U\hookrightarrow X$.
Write $g_X:X_S\to X$, $g_Z:Z_S\to Z$ and $i_S:Z_S\hookrightarrow X_S$
for the base changes. For every $M\in\Dbc(X,A)$ the canonical map

$$
g_Z^*i^!M\longrightarrow i_S^!g_X^*M
$$

is an isomorphism. Here $i^!$ denotes the derived exceptional inverse
image. The comparison is the mate of the inverse compact-support base
change isomorphism; equivalently, it is adjoint to the pulled-back counit.
