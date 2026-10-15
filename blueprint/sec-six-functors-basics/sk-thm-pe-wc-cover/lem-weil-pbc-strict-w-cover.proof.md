+++
kind  = "proof"
of    = "lem-weil-pbc-strict-w-cover"
+++
Use the notation of [def-weil-pbc-strict-w-cover]. The map $W\to E$ is
faithfully flat and ind-etale by [lem-weil-pbc-etale-contraction]. Its fibre
over a maximal ideal of $W$ is an algebraic algebra over a field, by
[lem-weil-pbc-weak-etale-field]; all its primes are maximal also in $E$.
Hence $T=V(IE)$ consists of closed points.
[lem-weil-pbc-retained-localization] makes $C_A$ w-local with these closed
points and unchanged local rings there. Those rings are strictly henselian by
[lem-weil-pbc-etale-contraction]. Faithful flatness of $E/W$ shows that $T$
surjects onto the closed points of $W$, which surject onto
$\operatorname{Spec}A$ by [lem-weil-pbc-w-localization-points]. The composite
$A\to C_A$ is ind-etale by [lem-weil-pbc-ind-etale-stability], and hence
flat. The just proved surjectivity makes it faithfully flat.
