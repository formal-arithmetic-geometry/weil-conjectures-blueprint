+++
kind  = "proof"
of    = "lem-kun-kflat-criteria"
+++
For a $\Lambda_T$-module sheaf as in
[def-weil-pbc-etale-sheaves] the notion of K-flatness is that of
[def-kun-derived-tensor]: a complex $\mathcal K^\bullet$ is K-flat if
$\mathcal K^\bullet\otimes_\Lambda\mathcal A^\bullet$ is acyclic for
every acyclic complex $\mathcal A^\bullet$. We prove (2), then (3),
then (1).
(2) Tensoring a distinguished triangle with the acyclic complex
$\mathcal A^\bullet$ gives a distinguished triangle; if two of its
terms are acyclic then so is the third, by the long exact cohomology
sequence. Hence if two terms of the original triangle are K-flat, the
third is as well. A cone is the third term of the triangle determined
by the map.
(3) Let $\mathcal K^\bullet=\varinjlim_i\mathcal K_i^\bullet$ be a
filtered colimit of K-flat complexes. Filtered colimits of
$\Lambda_T$-module sheaves are exact and commute with tensor products,
and homology commutes with filtered colimits, so for every acyclic
$\mathcal A^\bullet$,

$$
\mathcal K^\bullet\otimes_\Lambda\mathcal A^\bullet
=\varinjlim_i\bigl(\mathcal K_i^\bullet\otimes_\Lambda\mathcal
A^\bullet\bigr)
$$

is a filtered colimit of acyclic complexes, hence acyclic; thus
$\mathcal K^\bullet$ is K-flat. A direct sum is the filtered colimit
of its finite partial sums, and a finite direct sum of K-flat
complexes is K-flat by (2) applied to the split triangles
$\mathcal K_1^\bullet\to\mathcal K_1^\bullet\oplus\mathcal K_2^\bullet
\to\mathcal K_2^\bullet\to\mathcal K_1^\bullet[1]$.
(1) First let $\mathcal F^\bullet$ be a bounded complex of flat
sheaves; we show it is K-flat by induction on the number of nonzero
terms. If there are none, $\mathcal F^\bullet=0$. Otherwise let $N$
be the largest degree with $\mathcal F^N\ne0$. The stupid truncation
of [def-kun-truncations] gives a termwise split short exact sequence
of complexes

$$
0\to\mathcal F^N[-N]\to\mathcal F^\bullet\to
\sigma_{\le N-1}\mathcal F^\bullet\to0 ,
$$

hence a distinguished triangle. The complex $\mathcal F^N[-N]$ is
K-flat: $\mathcal F^N[-N]\otimes_\Lambda\mathcal A^\bullet$ is a shift
of $\mathcal F^N\otimes_\Lambda\mathcal A^\bullet$, which is acyclic
for acyclic $\mathcal A^\bullet$ because $\mathcal F^N$ is flat, i.e.
$\mathcal F^N\otimes_\Lambda-$ is exact. The complex
$\sigma_{\le N-1}\mathcal F^\bullet$ is a bounded complex of flat
sheaves with fewer nonzero terms, hence K-flat by induction. By (2),
$\mathcal F^\bullet$ is K-flat.
Now let $\mathcal F^\bullet$ be a bounded-above complex of flat
sheaves. Its stupid truncations $\sigma_{\ge-n}\mathcal F^\bullet$
($n\ge0$) are subcomplexes of $\mathcal F^\bullet$, they form an
increasing sequence, and in each degree $i$ the sequence
$(\sigma_{\ge-n}\mathcal F^\bullet)^i$ is constant equal to
$\mathcal F^i$ once $n\ge-i$. Hence
$\mathcal F^\bullet=\varinjlim_n\sigma_{\ge-n}\mathcal F^\bullet$ is a
filtered colimit of bounded complexes of flat sheaves, which are
K-flat by the previous paragraph, and $\mathcal F^\bullet$ is K-flat
by (3).
