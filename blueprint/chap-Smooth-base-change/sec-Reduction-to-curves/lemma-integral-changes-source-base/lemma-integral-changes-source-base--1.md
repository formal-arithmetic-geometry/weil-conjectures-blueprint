+++
id = "lemma-integral-changes-source-base--1"
kind = "lemma"
title = "Integral changes of source and base (1)"
name_showing = false
order = 679001
aliases = ["bp-r204-1"]
lean = ["AlgebraicGeometry.Etale.isIso_baseChangeHomologyMap_of_isIntegralHom_of_surjective"]
+++
Let $\Lambda$ be a commutative ring, let $g:T'\to T$ be a morphism of
schemes, and let $q\geq1$ be an integer. Assume that for every qcqs
morphism $h:W\to T$ and every sheaf of $\Lambda$-modules on
$W_{\acute{e}t}$, the base change map along $g$ in degree $q-1$ is an
isomorphism.

Let $f:Z\to T$ be qcqs, let $M$ be a sheaf of $\Lambda$-modules on
$Z_{\acute{e}t}$, and let $\pi:\widetilde Z\to Z$ be integral and
surjective. Write $Z'=T'\times_TZ$, with projections $g_Z:Z'\to Z$ and
$f':Z'\to T'$, and let

$$
b^q_{f,M}:g^{-1}R^qf_*M\longrightarrow R^qf'_*g_Z^{-1}M
$$

be the degree-$q$ map of Definition [definition-derived-base-change-map].
If $b^q_{f\pi,\pi^{-1}M}$ is an isomorphism, then $b^q_{f,M}$ is an
isomorphism. Equivalently, a failure for $f$ and $M$ persists for
$f\pi$ and $\pi^{-1}M$.
