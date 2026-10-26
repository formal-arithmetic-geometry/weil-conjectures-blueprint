+++
id = "cor-sf-fullcd-weakly-contractible-test"
kind = "theorem"
title = "FullCD tested on affine weakly contractible objects"
lean = ["AlgebraicGeometry.ProEtale.hasUniformCohomologicalDimensionLE_iff_forall_isWeaklyContractible"]
order = 2737
tags = ["latex:corollary"]
uses = ["def-weil-derived-cohomology-sheaves", "def-weil-full-cohomological-dimension", "def-weil-pbc-direct-image", "def-weil-pbc-proetale-site", "lem-cbc-proetale-stalk-conservative", "lem-sf-proetale-vanishing-detection"]
+++
In the setting of [def-weil-full-cohomological-dimension] the
condition $\operatorname{FullCD}(p,A;c)$ is equivalent to the following:
for every sheaf $\mathcal F$ of $A$-modules on
$\overline X_{\Proet}$ and every affine weakly contractible object
$W\to Y$ of $Y_{\Proet}$ the evaluations
$\mathcal H^r(Rp_*\mathcal F)(W)$ vanish for $r>c$, and the same holds
after every pro-étale base change of $p$. In particular the test of
$\operatorname{FullCD}$ needs no computation of geometric-point stalks,
and the failure of conservativity of the geometric-point stalks recorded in
clause (4) of [lem-cbc-proetale-stalk-conservative] does not obstruct
it.
