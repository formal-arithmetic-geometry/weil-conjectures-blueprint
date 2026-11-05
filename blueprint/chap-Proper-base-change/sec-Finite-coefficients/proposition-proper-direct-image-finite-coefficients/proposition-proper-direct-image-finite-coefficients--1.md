+++
id = "proposition-proper-direct-image-finite-coefficients--1"
kind = "proposition"
title = "Bounded constructibility on the étale site"
name_showing = false
order = 410001
aliases = ["bp-r124-1"]
lean = ["AlgebraicGeometry.Etale.boundedConstructible_rightDerivedLowerStar_of_isProper_of_isNoetherian"]
uses = ["definition-constructible-sheaves"]
+++
The mainline proof bypasses the Tor-amplitude bound and uses the following
étale finiteness statement.

Let $k$ be a field and let $A$ be a finite commutative ring annihilated by
a positive integer invertible in $k$. Let $Y$ be a Noetherian $k$-scheme
and let $p:X\to Y$ be proper. Then $Rp_*$ maps
$D^b_c(X_{\acute{e}t},A)$ into $D^b_c(Y_{\acute{e}t},A)$.
