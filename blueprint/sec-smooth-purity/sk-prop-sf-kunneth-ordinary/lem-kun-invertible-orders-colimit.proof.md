+++
kind  = "proof"
of    = "lem-kun-invertible-orders-colimit"
+++
Since $F$ is torsion, $F=\varinjlim_{n\ge1}F[n]$ by
[lemma-weil-pbc-torsion-filtered-union], and the canonical map
$\varinjlim_{n\in I_K}F[n]\to F$ is the comparison of the
sub-colimit over the divisibility-ordered subset
$I_K\subseteq\mathbf N_{>0}$. Geometric stalks commute with these
colimits ([lem-kun-stalks-commute-colimits]), so this comparison
is an isomorphism if and only if it is an isomorphism on every
geometric stalk ([lemma-weil-pbc-geometric-stalk-conservative]); on
a stalk it says that every element is killed by some $n\in I_K$,
which is exactly the defining condition of
[def-kun-torsion-invertible]. The notion of a torsion sheaf is
that of [def-weil-pbc-etale-sheaves].
