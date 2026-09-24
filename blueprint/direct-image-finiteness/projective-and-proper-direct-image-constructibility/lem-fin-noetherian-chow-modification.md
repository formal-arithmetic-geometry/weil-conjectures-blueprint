+++
id = "lem-fin-noetherian-chow-modification"
kind = "lemma"
title = "A projective modification of a reduced proper scheme"
order = 3250
uses = ["def-pc-projective-morphism", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-chow-affine-immersion-projective", "lem-weil-pbc-chow-closed-model-proper", "lem-weil-pbc-chow-fibres-proper-over-cover", "lem-weil-pbc-chow-generic-cover", "lem-weil-pbc-chow-product-image-model", "lem-weil-pbc-chow-projection-gluing", "lem-weil-pbc-chow-proper-surjective-isomorphism", "prop-weil-pbc-chow-closed-model-factorization"]
+++
Let $S$ be affine Noetherian and $X\to S$
proper, with $X$ reduced.
There are a proper map $\pi:Y\to X$ and a dense open $U\subset X$
such that $\pi^{-1}(U)\to U$ is an isomorphism and $Y\to S$ is
projective.

## Proof

Apply [lem-weil-pbc-chow-generic-cover] to obtain finitely many
affine opens $U_i$ containing all generic points of $X$.
Their intersection $U$ is dense and is scheme-theoretically dense
in each $U_i$: a function on a reduced affine scheme vanishing
at all its generic points belongs to all minimal primes and is zero.
By [lem-weil-pbc-chow-affine-immersion-projective], embed $U_i$
in a projective space over $S$, and take its closed model $Z_i$
by [lem-weil-pbc-chow-closed-model-proper].
The closure $W$ of the diagonal copy of $U$ in $\prod_i Z_i$
is the model of [lem-weil-pbc-chow-product-image-model].
Put $V_i=W\times_{Z_i}U_i$ and $Y=\bigcup_iV_i$.
The projections glue to $\pi:Y\to X$ by
[lem-weil-pbc-chow-projection-gluing].
The fibre calculation of [lem-weil-pbc-chow-fibres-proper-over-cover]
and [lem-weil-pbc-chow-proper-surjective-isomorphism]
show that $\pi$ is proper and is an isomorphism over $U$.
Finally [prop-weil-pbc-chow-closed-model-factorization]
makes the resulting immersion $Y\to\mathbf P^N_S$ closed.
All hypotheses of this construction hold on the given Noetherian
scheme; no descent of an arbitrary proper morphism to a
Noetherian approximation is needed.
