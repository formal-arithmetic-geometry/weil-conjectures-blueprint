+++
kind = "proof"
of = "det-tf-ibc-proper-step"
+++
The complex $N$ is classical, so we may calculate on small étale sites: the
comparison isomorphisms for inverse images [lem-weil-pbc-comparison-pullback] and for
derived direct images of bounded below complexes [prop-weil-pbc-comparison-direct-image]
are compatible with composites, hence with the units and counits defining the base
change map, and they transport the étale statement to the pro-étale one.

On the étale sites, $R\bar f_*N$ is bounded constructible by
[lem-fin-proper-bounded-constructible], since $\bar f$ is proper between finite-type
$k$-schemes and $A$ is finite with $\ell$ invertible on $k$. The square formed by
$\bar h$, $\bar f$, $p_{\bar X}$ and $p_Y$ is cartesian, because
$\bar X\times_kT=\bar X\times_Y(Y\times_kT)$. The morphism $\bar f$ is proper and $N$
is a bounded complex whose cohomology sheaves are torsion, $A$ being finite. So
bounded-below derived proper base change [thm-weil-pbc-bounded-below] shows that the
exchange map $p_Y^{-1}R\bar f_*N\to R\bar h_*p_{\bar X}^{-1}N$ is an isomorphism; this
exchange map is the base change map of the statement.
