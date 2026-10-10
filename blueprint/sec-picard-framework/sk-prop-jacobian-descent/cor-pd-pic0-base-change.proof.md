+++
kind  = "proof"
of    = "cor-pd-pic0-base-change"
+++
By [lem-pd-picard-base-change] the functor
$\operatorname{Pic}_{C/k}$ restricts to
$\operatorname{Pic}_{C_{k'}/k'}$ on the slice over $k'$, and the restriction of
a functor to a slice is the base change in the sense of
[def-pc-base-change]. The degree morphism of
[def-pd-degree-morphism] is defined through the fibrewise degree, and
[lem-pd-degree-locally-constant](3) says precisely that it is compatible
with this restriction: the restriction of
$\deg:\operatorname{Pic}_{C/k}\to\underline{\Z}$ is the degree morphism of
$C_{k'}$. Restricting the kernel of a morphism of sheaves to a slice gives
the kernel of the restricted morphism, so the two degree-zero parts agree after
base change, which is the displayed isomorphism.
