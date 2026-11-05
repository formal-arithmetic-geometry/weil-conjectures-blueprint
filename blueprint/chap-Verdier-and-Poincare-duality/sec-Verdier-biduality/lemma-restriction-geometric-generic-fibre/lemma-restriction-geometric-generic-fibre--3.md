+++
id = "lemma-restriction-geometric-generic-fibre--3"
kind = "lemma"
title = "Internal Hom under generic base change"
name_showing = false
order = 838003
aliases = ["bp-r251-3"]
lean = ["AlgebraicGeometry.Etale.isIso_derivedHomUpperStarComparison_of_generic"]
uses = ["definition-constructible-sheaves", "prose-10-07"]
+++
Let $B$ be an integral scheme of finite type over a field $k$, let $A$
be a finite commutative ring whose exponent is invertible on $B$, and let
$t:S\to B$ be a morphism from a noetherian scheme such that every point
of $S$ maps to the generic point of $B$. Work on the classical étale sites.
Let $X$ be of finite type over $B$, and write $g_X:X_S\to X$ for the
base change. For $K\in\Dctf(X,A)$ and $M\in\Dbc(X,A)$ the canonical map

$$
g_X^*\cHom_X(K,M)\longrightarrow
\cHom_{X_S}(g_X^*K,g_X^*M)
$$

is an isomorphism. This is the tensor–Hom adjoint of the pullback of
evaluation, using the compatibility of $g_X^*$ with tensor products.
