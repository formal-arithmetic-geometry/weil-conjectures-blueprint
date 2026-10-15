+++
kind  = "proof"
of    = "sk-lem-bounded-continuity"
+++
Choose a hypercovering $W_\bullet\to Y$ by affine weakly contractible objects; by
[sk-prop-pe-hypercover], $R\Gamma(Y,K_i^\bullet)$ is computed by the total complex of the
double complex $K_i^m(W_n)$. The point is that this total complex commutes with filtered
colimits.

First, the functor $M\mapsto M(W_n)$ is exact and commutes with direct sums
([sk-cor-pe-sections]). An exact additive functor that commutes with direct sums commutes
with all colimits, since a colimit is the cokernel of a map between two direct sums.
Second, the term of total degree $q$ is $\bigoplus_{n+m=q}K_i^m(W_n)$ with $n\ge0$ and
$m\ge a$, a finite direct sum with $0\le n\le q-a$. Hence the total complex of
$\varinjlim_iK_i^\bullet$ is the colimit of the total complexes, and since filtered colimits
of modules are exact, taking cohomology proves the first assertion. Details:
[det-lem-bounded-continuity-sections].

For the second, $R^qg_*K$ is the sheafification of $V\mapsto H^q(Y\times_ZV,K)$ on affine
objects $V$ of $Z_{\mathrm{proét}}$. Each $Y\times_ZV$ is quasi-compact and quasi-separated,
so the first assertion applies, and sheafification commutes with colimits. Details:
[det-lem-bounded-continuity-direct-image].
