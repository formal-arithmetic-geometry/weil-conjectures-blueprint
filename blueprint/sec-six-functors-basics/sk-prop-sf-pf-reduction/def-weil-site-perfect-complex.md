+++
id = "def-weil-site-perfect-complex"
kind = "definition"
title = "Perfect complexes on the coefficient site"
lean = ["AlgebraicGeometry.Etale.DerivedCategory.IsSitePerfect"]
order = 2225
uses = ["def-weil-pbc-proetale-site", "sk-def-sfb-condensed-ring", "sk-def-sfb-qlbar-condensed", "sk-def-sfb-pulled-back-coefficients", "sk-def-sfb-derived-categories"]
+++
Let $Y$ have the small pro-étale site [def-weil-pbc-proetale-site], and let
$\Lambda\in\{A_{E,n},\mathcal O_E,E,\Qlb\}$, regarded as a condensed ring
([sk-def-sfb-condensed-ring], [sk-def-sfb-qlbar-condensed]). For an object
$U$ of $Y_{\mathrm{proét}}$ put $\Lambda_U=p_U^*\Lambda$
([sk-def-sfb-pulled-back-coefficients]). A complex
$K\in D(Y_{\mathrm{proét}},\Lambda)$ ([sk-def-sfb-derived-categories]) is
*perfect on the coefficient site* if there is a pro-étale covering
$\{U_\alpha\to Y\}$ such that each $K|_{U_\alpha}$ is isomorphic to a bounded
complex of finite projective $\Lambda_{U_\alpha}$-modules. Here a finite
projective module is a direct summand of a finite sum
$\Lambda_{U_\alpha}^{\oplus m}$. The definition is the same for every
$\Lambda$ in the list; at $\Lambda=A_{E,n}$ it is the finite-level notion.
