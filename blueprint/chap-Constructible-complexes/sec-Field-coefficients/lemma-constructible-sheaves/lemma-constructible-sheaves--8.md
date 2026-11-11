+++
id = "lemma-constructible-sheaves--8"
kind = "lemma"
title = "Local freeness of finite presentations"
order = 268016
aliases = ["bp-r080-8"]
lean = ["AlgebraicGeometry.ProEtale.exists_finiteFree_cover_of_condensedField_lfp", "AlgebraicGeometry.ProEtale.condensedQbar_lfp_locally_free", "AlgebraicGeometry.ProEtale.IsLocallyFinitelyPresented"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "corollary-finite-quotients-their-transition-maps--3", "lemma-inverse-image-coefficient-sheaves--1"]
+++
Let $X$ be a scheme whose underlying topological space is Noetherian,
and let $\Lambda=E$ or $\overline{\mathbf Q}_\ell$, where
$E/\mathbf Q_\ell$ is a finite extension with its $\ell$-adic topology.
Regard these coefficients as condensed rings.
If a $\Lambda_X$-module $M$ is locally finitely presented on the pro-étale
site, then there is a pro-étale cover $\{U_i\to X\}$ and natural numbers
$r_i$ such that

$$
M|_{U_i}\simeq\Lambda_{U_i}^{r_i}.
$$

Here local finite presentation permits matrices of sections of
$\Lambda_{U_i}$. Thus $M$ is lisse, with ranks allowed to vary on the cover.
