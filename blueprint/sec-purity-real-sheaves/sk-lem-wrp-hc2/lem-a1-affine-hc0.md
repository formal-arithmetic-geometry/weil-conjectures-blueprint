+++
id = "lem-a1-affine-hc0"
kind = "lemma"
title = "Vanishing of $H_c^0$ on a nonproper curve"
lean = ["AlgebraicGeometry.WeilSheaf.subsingleton_compactlySupportedCohomology_zero", "AlgebraicGeometry.WeilSheaf.subsingleton_compactlySupportedCohomology_of_isLisse_of_isAffine"]
order = 3852
uses = ["def-weil-ordinary-compact-cohomology", "def-weil-weil-sheaf-complex", "p-real-integral", "sk-lem-coefficient-heart", "sk-prop-integral-criterion", "sk-prop-pe-milnor", "sk-prop-scalar-six", "sk-thm-sf-ctf-stability"]
+++
Let $U_0$ be a smooth geometrically connected affine curve and let
$\mathcal F$ be a lisse Weil sheaf
on $U_0$, a lisse $\overline{\mathbf Q}_{\ell,U}$-module on $U_{\mathrm{proét}}$
([sk-lem-coefficient-heart]) with a Weil structure ([def-weil-weil-sheaf-complex]). Then, in the
compactly supported
cohomology of [def-weil-ordinary-compact-cohomology],
$H_c^0(U,\mathcal F)=0$.
