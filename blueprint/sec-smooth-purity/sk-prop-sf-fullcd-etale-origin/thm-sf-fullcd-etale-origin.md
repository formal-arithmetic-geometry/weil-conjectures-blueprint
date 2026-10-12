+++
id = "thm-sf-fullcd-etale-origin"
kind = "theorem"
title = "FullCD for coefficients of étale origin"
order = 2095
uses = ["def-weil-full-cohomological-dimension", "def-weil-pbc-direct-image", "def-weil-pbc-etale-sheaves", "def-weil-pbc-proetale-site", "def-weil-pbc-site-comparison-morphism", "def-weil-scheme-morphism-properties", "lem-sf-etale-direct-image-vanishing", "lem-weil-pbc-comparison-pullback", "prop-weil-pbc-comparison-direct-image"]
+++
Fix the global finite-field datum, a prime $\ell\ne p$, an integer
$n\geq1$, $A=A_{E,n}$, the algebraically closed field
$k=\overline{\mathbf F}_q$, finite-type $k$-schemes $Y$ and
$\overline X$ with $\dim\overline X\leq d$, and a
proper finite-type morphism
$p:\overline X\to Y$. Let $\mathcal F$ be a sheaf of $A$-modules on
$\overline X_{\Proet}$ that is of étale origin:
$\mathcal F\cong\nu_{\overline X}^*\mathcal G$ for a sheaf
$\mathcal G$ of $A$-modules on $\overline X_{\Et}$. Then the vanishing
required by [def-weil-full-cohomological-dimension] holds for
$\mathcal F$ with the bound $2d$: for every $r>2d$ one has
$\mathcal H^r(Rp_*\mathcal F)=0$, and the same holds for every base change
$V\to Y$ whose source has dimension at most $d$, in particular for
every base change by an étale $Y$-scheme.
