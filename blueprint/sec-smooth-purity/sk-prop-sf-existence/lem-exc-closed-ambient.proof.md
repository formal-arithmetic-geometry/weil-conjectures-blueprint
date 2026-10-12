+++
kind  = "proof"
of    = "lem-exc-closed-ambient"
+++
For an etale module sheaf $N$, set
$\Gamma_ZN=\ker(N\to j_*j^*N)$.
The stalk description and the conservativity in
[lemma-weil-pbc-geometric-stalk-conservative] identify sheaves whose
restriction to $U$ is zero with sheaves on $Z$, by the exact fully
faithful $i_*$. Its inverse on these sheaves is the $i^*$ of
[def-weil-pbc-inverse-image]. Every map $i_*M\to N$ factors
uniquely through $\Gamma_ZN$; thus $i^!=i^*\Gamma_Z$ is right
adjoint to $i_*$ on sheaves.

Take a K-injective resolution $K\to I$ with injective terms, using
[prop-weil-pbc-kinjective-resolutions-exist]. Both $j^*I$ and
$i^!I$ are K-injective: their left adjoints $j_!$ and $i_*$
are exact, so Hom from an acyclic complex into either restriction is
acyclic. The complex-level adjunction gives
$i_*\dashv Ri^!$. Here derived direct image is that of
[def-weil-pbc-direct-image]; no constructibility has been used.
