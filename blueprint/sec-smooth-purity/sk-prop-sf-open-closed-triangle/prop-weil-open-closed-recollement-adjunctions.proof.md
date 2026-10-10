+++
kind  = "proof"
of    = "prop-weil-open-closed-recollement-adjunctions"
+++
The open adjunction is the extension-by-zero adjunction. Both functors are
exact, so they pass to ordinary derived categories with the same adjunction
and triangle identities. The unit is an isomorphism term by term by
[lem-exc-proetale-open-unit].

For the closed adjunction, choose a K-injective resolution $M\to J$ on $Z$.
Since $i^*$ is exact, $i_*J$ is K-injective: its Hom complex from an acyclic
complex $N$ is the Hom complex from the acyclic $i^*N$ to $J$, hence
acyclic. Thus $i_*J$ represents $Ri_*M$, and complex-level adjunction gives
$i^*\dashv Ri_*$. Exactness of $i^*$ lets us compute the derived counit by
$i^*i_*J\to J$. This is an isomorphism in every degree by
[lem-exc-proetale-closed-fully-faithful]. Hence the derived counit is an
isomorphism. This calculation does not assume exactness of $i_*$ for an
arbitrary closed immersion; the complement's quasi-compactness is needed for
the separate sheaf-exactness and recollement theorems above.
