+++
kind = "proof"
of = "det-tf-blowup-strict-transform"
uses = ["det-tf-blowup-configuration"]
+++
*Finiteness.* $B'$ is a closed subscheme of the projective
$T$-scheme $\widetilde T$, so $B'\to B$ is proper. It is an isomorphism
over $B-t$, and its fibre over $t$ is $B'\cap P$, the finite set of
tangent directions of the branches of $B$. So $B'\to B$ is proper and
quasi-finite, hence finite.

*Decomposition.* $B$ is a closed subscheme of the strictly local scheme
$T$, hence strictly local. A finite algebra over a strictly henselian
local ring is a finite product of strictly henselian local rings, one
for each point of its closed fibre
([Stacks, Tag 04GG](https://stacks.math.columbia.edu/tag/04GG)). Thus
$B'$ is the disjoint union of strictly local curves $B'_s$, indexed by
$s\in B'\cap P$, each with closed point $s$ and $B'_s\cap P=\{s\}$.

*Position.* The hypothesis $C_tD\cap C_tB=\{0\}$ says that no tangent
direction of $B$ is one of $D$, so $s\notin D'$ and $s\in Y$. Every point
of the local scheme $B'_s$ specializes to $s$, and $D'$ is closed, so
$B'_s\cap D'=\emptyset$; hence $B'_s$ is a closed curve in
$Z=\widetilde T-D'$ with $B'_s\cap Y=\{s\}$. Being strictly local, it is
its own strict localization at $s$.

*Restriction.* Since $f$ is an isomorphism off $P$, it identifies
$B'-P$ with $B-t$, and $B'-P=\coprod_s(B'_s-s)$. By
[det-tf-blowup-configuration], $f$ identifies $Z-Y$ with $T-D$, and
these identifications are compatible with the inclusions of $B-t$ and
$B'-P$. Cohomology of a finite disjoint union is the direct sum of the
cohomologies of the pieces, and the restriction map to $B-t$ is the
tuple of the restriction maps to the pieces $B'_s-s$.
