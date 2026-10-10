+++
id = "prop-weil-pbc-cone-independence"
kind = "theorem"
title = "Compatibility and independence of common-stage cones"
order = 1539
uses = ["def-weil-pbc-common-stage-cones", "def-weil-pbc-finite-stage-pair-category", "prop-weil-pbc-common-stage-calculus", "prop-weil-pbc-scalar-extension"]
tags = ["latex:proposition"]
+++
If $M\subset N$, exactness of $T_{N/M}$ identifies the scalar extension of a
cone triangle for $u$ with a cone triangle for $u_N$. If two representatives
define the same morphism of $\mathcal P_T$, their cone triangles become
isomorphic after passage to a field where the representatives agree. Any two
cone triangles selected for one finite-stage morphism are isomorphic by a
morphism of triangles whose first two components are identities. Thus
distinguishedness in [def-weil-pbc-common-stage-cones] is independent of
every representative, common field, and cone choice.

## Proof

For $M\subset N$, the functor $T_{N/M}$ of
[prop-weil-pbc-scalar-extension] is exact and its shift comparison carries
the cone triangle for $u$ in $\mathcal C_M$ to a distinguished triangle of
$\mathcal C_N$ which is a cone triangle for $u_N$, identifying the scalar
extension of the first with a cone triangle of the second. If
$(M,u)\sim(N,v)$, then $u_P=v_P$ for some finite $P$, and transporting the
two cone triangles to $P$ via the transport of
[prop-weil-pbc-common-stage-calculus] and the $\sigma$-comparisons of
[prop-weil-pbc-scalar-extension] makes them isomorphic over $P$ by the
finite-stage axiom TR3, with identity components on the common source and
target; any two cone triangles selected for one finite-stage morphism are
isomorphic by a morphism of triangles whose first two components are
identities (the finite-stage uniqueness of cones up to noncanonical
isomorphism). Combining these facts, distinguishedness in
[def-weil-pbc-common-stage-cones] is independent of the representative, of
the common field and of the cone choice, in the sense of the category of
[def-weil-pbc-finite-stage-pair-category].
