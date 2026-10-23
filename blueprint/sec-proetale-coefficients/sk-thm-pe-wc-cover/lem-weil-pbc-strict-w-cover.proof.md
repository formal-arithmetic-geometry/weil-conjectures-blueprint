+++
kind  = "proof"
of    = "lem-weil-pbc-strict-w-cover"
+++
Use the notation of [def-weil-pbc-strict-w-cover]. The map $W\to E$ is
faithfully flat and ind-etale by [lem-weil-pbc-etale-contraction]. Its
residue field extensions are algebraic, by [lem-weil-pbc-weak-etale-field]
applied to its fibres, which are weakly etale over fields
([lem-weil-pbc-ind-etale-stability]). Since $W$ is w-local with closed points
$V(I)$ ([lem-weil-pbc-w-localization-points]), part 3 of
[lem-weil-pbc-retained-localization] shows that the closed points of
$\operatorname{Spec}C_A$ are the points of $V(IC_A)$ and that $W\to C_A$ is
faithfully flat; by part 1, $\operatorname{Spec}C_A$ is w-local and $E\to C_A$
is ind-Zariski, so it identifies local rings. A maximal ideal of $C_A$
contains $IC_A$, so it lies over a prime of $E$ containing $IE$, which is
maximal as in part 3 of [lem-weil-pbc-retained-localization]; its local ring
equals that of $E$, which is strictly henselian by
[lem-weil-pbc-etale-contraction]. The composite $A\to W\to E\to C_A$ is
ind-etale and faithfully flat by [lem-weil-pbc-ind-etale-stability]. Finally
$V(IC_A)\to V(IE)$ is bijective by part 2 of
[lem-weil-pbc-retained-localization], $V(IE)\to V(I)$ is surjective by
faithful flatness of $W\to E$, and $V(I)\to\operatorname{Spec}A$ is bijective
by [lem-weil-pbc-w-localization-points]; so the closed points of $C_A$ surject
onto $\operatorname{Spec}A$.
