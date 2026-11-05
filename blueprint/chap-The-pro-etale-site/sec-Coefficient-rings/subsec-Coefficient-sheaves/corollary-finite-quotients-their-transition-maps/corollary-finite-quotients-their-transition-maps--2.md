+++
id = "corollary-finite-quotients-their-transition-maps--2"
kind = "corollary"
title = "Finite quotients and their transition maps (2)"
name_showing = false
order = 181002
aliases = ["bp-r052-2"]
lean = ["AlgebraicGeometry.ProEtale.PrincipalNormalization.principal_cone_tensor_normalization"]
uses = ["definition-small-pro-etale-site", "prose-02-50", "prose-02-51"]
+++
Put $R=\mathcal O_{E,X}$ and $B_n=(\mathcal O_E/\pi_E^n)_X$. For
$n\geq1$, the augmentation
$$
[R\xrightarrow{\pi_E^n}R]\longrightarrow B_n[0]
$$
is a quasi-isomorphism, with the two terms in degrees $-1,0$.
Reduction from level $n+1$ to level $n$ is represented by the chain map
$(\pi_E,\mathrm{id})$.

More generally, for every possibly unbounded complex $M$ of $R$-modules,
there are isomorphisms in the derived category, natural in $M$,
$$
\kappa_{n,M}:\operatorname{cone}(\pi_E^n:M\to M)
\xrightarrow{\sim}M\otimes_R^{\mathbf L}B_n.
$$
These identify the cone map $(\pi_E,\mathrm{id})$ with the map induced by
$B_{n+1}\to B_n$, and the cone inclusion with the canonical reduction map
$M\to M\otimes_R^{\mathbf L}B_n$. They also commute with shifts, using
the usual signed cone-shift isomorphism, which multiplies the shifted
source summand by $(-1)^r$ for a shift by $r$.
