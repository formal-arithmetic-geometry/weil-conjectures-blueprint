+++
kind  = "proof"
of    = "prop-weil-pbc-rlim-functoriality"
+++
In a Grothendieck abelian category every complex admits a functorial
K-injective resolution, and quasi-isomorphic K-injective complexes are
chain-homotopy equivalent (Stacks Project, Theorem 19.12.6, Tag
[079P](https://stacks.math.columbia.edu/tag/079P)); applied to the tower
category of [def-weil-pbc-adic-coefficient-datum] this supplies the
functorial resolutions fixed in the statement. By
[prop-weil-pbc-derived-inverse-limit-computation] the value of the assignment
at $M_\bullet$ represents the derived limit $\Rlim M_\bullet$ of
[def-weil-pbc-derived-inverse-limit], and the derived limit is a triangulated
functor of the system, being the first term of the Roos triangle, which is
natural in the system; the assignment therefore inherits exactness on
distinguished triangles. A second choice of functorial K-injective
resolutions is related to the first by a chain-homotopy equivalence over each
object, and $\varprojlim_n(-)$ of a levelwise homotopy equivalence of towers
is a homotopy equivalence, so the two assignments agree up to a natural
isomorphism of functors. The K-injectivity used here is that of
[def-weil-pbc-kinjective-resolutions].
