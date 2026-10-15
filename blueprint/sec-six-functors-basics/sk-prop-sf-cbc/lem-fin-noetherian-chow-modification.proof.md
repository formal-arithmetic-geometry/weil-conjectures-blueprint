+++
kind  = "proof"
of    = "lem-fin-noetherian-chow-modification"
+++
Apply [lemma-nagata-dense-affine-cover-exists] to obtain finitely many
affine opens $U_i$ containing all generic points of $X$.
Their intersection $U$ is dense and is scheme-theoretically dense
in each $U_i$: a function on a reduced affine scheme vanishing
at all its generic points belongs to all minimal primes and is zero.
By [lem-chow-affine-immersion], embed $U_i$
in a projective space over $S$, and take its closed model $Z_i$
by [lem-chow-closed-model].
The closure $W$ of the diagonal copy of $U$ in $\prod_i Z_i$
is the model of [lem-chow-graph].
Put $V_i=W\times_{Z_i}U_i$ and $Y=\bigcup_iV_i$.
The projections glue to $\pi:Y\to X$ by
[lem-chow-glue].
The fibre calculation of [lem-chow-preimage]
and [thm-chow-lemma]
show that $\pi$ is proper and is an isomorphism over $U$.
Finally [cor-chow-lemma-proper]
makes the resulting immersion $Y\to\mathbf P^N_S$ closed.
All hypotheses of this construction hold on the given Noetherian
scheme; no descent of an arbitrary proper morphism to a
Noetherian approximation is needed.
