+++
id = "lem-sc-mult-n-etale-kernel"
kind = "lemma"
title = "Multiplication by $d$ prime to the characteristic is etale"
lean = ["AlgebraicGeometry.etale_npow_id", "AlgebraicGeometry.etale_torsionSubgroupScheme"]
order = 588
uses = ["def-sc-abelian-variety", "def-sc-mult-n"]
+++
Let $A$ be an abelian variety of dimension $g$ over a field $k$
and let $d\geq1$ with $\operatorname{char}k\nmid d$. Then the
kernel $A[d]$ of $[d]:A\to A$ of [def-sc-mult-n] is a finite etale
group scheme of order $d^{2g}$ over $k$, and $[d]$ is etale. Moreover,
for an algebraic closure $\bar k$ of $k$, the base change
$A[d]_{\bar k}$ is the constant group scheme $(\mathbf Z/d\mathbf Z)^{2g}$:
it is the disjoint union of its $d^{2g}$ points
$\Spec\bar k$, and $A[d](\bar k)\cong(\mathbf Z/d\mathbf Z)^{2g}$.
