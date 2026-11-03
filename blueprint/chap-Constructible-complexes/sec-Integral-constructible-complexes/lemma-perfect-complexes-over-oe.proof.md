+++
kind = "proof"
of = "lemma-perfect-complexes-over-oe"
order = 232
+++
We use that a minimal complex over the local ring
$\mathcal O_E/\pi_E^n$ is determined up to isomorphism of complexes, not
only up to homotopy, so that the transition maps can be made into
equalities of matrices and passed to the limit.

Represent each $M_n$ by a minimal finite free complex, obtained by
cancelling unit entries in the differential matrices. Its reduction
modulo $\pi_E$ has zero differential. Hence its rank in degree $q$ is
$\dim_{\mathbf F_E}H^q(M_1)$, which is independent of $n$ and nonzero only in
finitely many degrees. The given isomorphism
$M_{n+1}/\pi_E^n\simeq M_n$ between minimal complexes is represented
by a chain homotopy equivalence $f$, with homotopy inverse $g$. Both
complexes have zero differential modulo $\pi_E$. Therefore the relations
$gf-1=dh+hd$ and $fg-1=dh'+h'd$ show that $f$ is an isomorphism modulo
$\pi_E$ in each degree. By Nakayama's lemma its matrices are then invertible over
$\mathcal O_E/\pi_E^n$. Lifting them to invertible matrices over
$\mathcal O_E/\pi_E^{n+1}$ and changing bases, we may assume that the
differential at level $n+1$ reduces exactly to the differential at
level $n$, with the given transition in the derived category.
Induction on $n$ gives compatible matrices, and their limits define
$P^\bullet$. Its differential squares to zero because it does so
modulo every $\pi_E^n$, and the identifications with the $M_n$ are
compatible by construction.
