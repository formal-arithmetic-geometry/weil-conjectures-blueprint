+++
id = "proposition-proper-direct-image-constructible-complexes--1"
kind = "proposition"
title = "Finite coefficients"
order = 425002
aliases = ["bp-r129-1"]
lean = ["AlgebraicGeometry.ProEtale.boundedConstructible_rightDerivedLowerStar_of_isProper_of_isNoetherian"]
uses = ["definition-constructible-sheaves"]
+++
Let $A$ be a finite commutative ring annihilated by an integer invertible in a field $k$.
Let $Y$ be a Noetherian $k$-scheme and $p:X\to Y$ proper. Then
$$
Rp_{*,A}:\Dbc(X,A)\longrightarrow\Dbc(Y,A).
$$
Here bounded constructibility on the pro-étale site means that the complex is the
pullback of a bounded constructible complex on the étale site. This statement
records bounded constructibility; it does not assert a Tor-amplitude bound.
