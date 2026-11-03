+++
kind  = "proof"
of    = "lem-pur-dnc-section-geometry"
+++
Use the blow-up construction of [def-pur-dnc-section-family] and the section invariant of [def-pur-section-invariant]. The local coordinates are those of [sbc-thm-etale-local-normal-form], and the comparison of family fibers uses condition (3) of [def-pur-co-smoothness].
Item (1): the blow-up along $s(B)\times\{0\}$ is fiberwise trivial
away from the center, and the strict transform of
$V\times_B\{0\}$ is removed; the fiber of $\widetilde g$ over
$t\neq0$ is $V$ with the section $s$, and the exceptional
division of the affine cone identifies the fiber over $0$ with the
normal bundle $N_s$ of the section. Items (2): the coordinates are
the ones of the relative linearization; on the chart
$u_i=x_i/t$, the map $\widetilde g$ is the projection
$(u,x',t)\mapsto(x',t)$ into the base coordinates, smooth of
relative dimension $d$; on the remaining charts of the blow-up the
same computation after substituting a generator of the center gives
smoothness. Items (3),(4),(5) are the standard Rees-algebra
calculations, with the normal-bundle identification of
[def-pur-normal-bundle] and its base-change behavior; the family
object of the standard pair is computed by the rank-$d$ vector-bundle
purity of [cor-pur-vector-bundle-purity] since
$\mathbf A^d_B\to B$ is the trivial rank-$d$ bundle.
