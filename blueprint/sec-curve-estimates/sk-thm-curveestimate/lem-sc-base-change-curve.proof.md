+++
kind  = "proof"
of    = "lem-sc-base-change-curve"
+++
Separation, quasi-compactness, smoothness of relative dimension one,
properness and affineness are all stable under base change
([def-weil-pbc-scheme-conventions]); for affineness note that for
$C=\operatorname{Spec}A$ one has $C_{k'}=\operatorname{Spec}(A\otimes_kk')$.
A scheme smooth of relative dimension one over a field is locally of finite
type, and each of its affine open pieces has dimension at most one (its
irreducible components have transcendence degree one, or it is empty); hence
$C_{k'}$, being also separated and quasi-compact, is a curve over $k'$.

Now let $k$ be algebraically closed and $C$ a smooth connected curve as in
the second assertion; being smooth, connected and of dimension one, it is
smooth of relative dimension one, so the first part applies. Then
$C_{k'}$ is nonempty, because $C_{k'}\to C$ is
surjective, and of dimension exactly one by the above, being smooth of
relative dimension one and nonempty. It is connected: over a separably
closed field the morphism $C_{k'}\to C$ induces a bijection of connected
components (*reference: Stacks Project, Varieties,
[Tag 0363](https://stacks.math.columbia.edu/tag/0363)*).
