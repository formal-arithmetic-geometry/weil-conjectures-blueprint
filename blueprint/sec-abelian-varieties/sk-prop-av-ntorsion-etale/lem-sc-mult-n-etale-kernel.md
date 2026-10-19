+++
id = "lem-sc-mult-n-etale-kernel"
kind = "lemma"
title = "Multiplication by $d$ prime to the characteristic is etale"
lean = ["AlgebraicGeometry.etale_npow_id", "AlgebraicGeometry.etale_torsionSubgroupScheme", "AlgebraicGeometry.isFinite_torsionSubgroupScheme", "AlgebraicGeometry.finrankΓ_torsionSubgroupScheme", "AlgebraicGeometry.IsAbelianVariety.exists_overIso_sigma_torsionSubgroupScheme", "AlgebraicGeometry.IsAbelianVariety.nonempty_addEquiv_torsionBy_points"]
order = 594
uses = ["def-sc-abelian-variety", "def-sc-mult-n"]
+++
Let $A$ be an abelian variety of dimension $g$ over a field $k$
and let $d\geq1$ with $\operatorname{char}k\nmid d$. Then the
kernel $A[d]$ of $[d]:A\to A$ of [def-sc-mult-n] is a finite etale
group scheme of order $d^{2g}$ over $k$, and $[d]$ is etale. Moreover,
for a separably closed field extension $k'\supseteq k$, the base change
$A[d]_{k'}$ is, as a $k'$-scheme, the disjoint union of $d^{2g}$ copies
of $\Spec k'$; and if $k'$ is algebraically closed, the group
$A(k')[d]$ of $d$-torsion points of $A$ with values in $k'$ satisfies
$A(k')[d]\cong(\mathbf Z/d\mathbf Z)^{2g}$.
