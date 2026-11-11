+++
id = "definition-constructible-sheaves--1"
kind = "definition"
title = "Constructible sheaves (1)"
name_showing = false
order = 219002
aliases = ["bp-r063-1"]
lean = ["AlgebraicGeometry.ProEtale.HasFiniteConstantLocalModel", "AlgebraicGeometry.ProEtale.HasFiniteConstantLocalModelOnCover", "AlgebraicGeometry.ProEtale.finiteConstantLocalModelOnCover_iff_scalarMatrix", "AlgebraicGeometry.ProEtale.finiteConstantLocalModel_iff_exists_cover"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "corollary-finite-quotients-their-transition-maps--3", "lemma-inverse-image-coefficient-sheaves--1", "definition-lisse-sheaves--1"]
+++
Consider the following condition on a $\Lambda_X$-module $M$:
there is a pro-étale cover $\{U_i\to X\}$ and finitely presented
modules $P_i$ over the ring $\Lambda(*)$ of sections over the point such that

$$
M|_{U_i}\simeq\Lambda_{U_i}\otimes_{\Lambda(*)}P_i.
$$

Here $\Lambda(*)$ and $P_i$ are constant sheaves on $U_i$, acting
through $\Lambda(*)\to\Lambda_{U_i}$. Equivalently, on each $U_i$ the
module $M$ has a presentation by a finite matrix with entries in
$\Lambda(*)$.
