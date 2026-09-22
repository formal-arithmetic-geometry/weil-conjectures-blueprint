+++
id = "lem-sc-normalization-over-normal-locus"
kind = "lemma"
title = "The normalization over the normal locus"
order = 3662
lean = ["AlgebraicGeometry.Scheme.isIso_normalization_over_normalLocus"]
+++
Let $X$ be an integral scheme of finite type over a field $k$ and
$\nu:X^{\nu}\to X$ its normalization. For every open $U\subseteq X$ which
is normal, the induced morphism $X^{\nu}\times_XU\to U$ is an isomorphism.

## Proof

Over a normal open $U$, the integral closure of $\mathcal O_U$ in $k(X)$ is
$\mathcal O_U$ itself (a normal domain is integrally closed in its fraction
field), so $X^{\nu}\times_XU\to U$ is an isomorphism.

Unresolved dependencies: def:sc-normalization
