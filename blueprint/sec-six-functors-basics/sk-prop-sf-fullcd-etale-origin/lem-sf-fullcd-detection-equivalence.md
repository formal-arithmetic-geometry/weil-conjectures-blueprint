+++
id = "lem-sf-fullcd-detection-equivalence"
kind = "lemma"
title = "The full cohomological-dimension condition is a bound on the pro-étale cohomology of the base-changed source"
lean = ["AlgebraicGeometry.ProEtale.hasUniformCohomologicalDimensionLE_iff_forall_ext"]
order = 2140
uses = ["cor-sf-fullcd-weakly-contractible-test", "def-weil-derived-cohomology-sheaves", "def-weil-full-cohomological-dimension", "def-weil-pbc-direct-image", "def-weil-pbc-proetale-site", "lem-sf-proetale-vanishing-detection", "thm-sp-grothendieck"]
+++
In the setting of [def-weil-full-cohomological-dimension] the condition
$\operatorname{FullCD}(p,A;c)$ is equivalent to the following statement: for
every object $V\to Y$ of $Y_{\Proet}$
([def-weil-pbc-proetale-site]) and every sheaf $\mathcal F$ of
$A$-modules on $\overline X_{\Proet}$, with $p_V$ and $(p_V)_*$ as in
the derived direct image of [def-weil-pbc-direct-image], one has

$$
H^r\bigl((\overline X\times_YV)_{\Proet},\mathcal F|_{\overline X\times_YV}\bigr)=0
\qquad(r\in\mathbf Z,\ r>c),
$$

the cohomology being that of the small pro-étale site of the base-changed
source.
