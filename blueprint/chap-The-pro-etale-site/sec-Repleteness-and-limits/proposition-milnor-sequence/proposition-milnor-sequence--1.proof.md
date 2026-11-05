+++
kind = "proof"
of = "proposition-milnor-sequence--1"
order = 91004
uses = ["proposition-exact-products"]
+++
By [proposition-exact-products], cohomology commutes with the termwise
countable products in the Roos complex. Apply the long exact
cohomology sequence of its cone triangle. For a tower concentrated in
degree zero, the cokernel term in degree $-1$ vanishes, so the map
from $H^0$ to the inverse limit is an isomorphism. In degree $1$ the
limit of the degree-one cohomology sheaves vanishes, so the map from
the cokernel of $1-T$ to $H^1$ is an isomorphism. These give $e_0$ and
$e_1$ after identifying the degree-zero cohomology tower with $(M_n)$.
In every other degree both end terms vanish, giving the asserted
vanishing.

A map of towers induces the diagonal product map on both summands of
the cone. It commutes with the boundary and projection maps. Factoring
through their cokernels and kernels gives naturality of the short
exact sequences, and hence of $e_0$ and $e_1$.
