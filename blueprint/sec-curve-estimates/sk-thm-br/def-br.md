+++
id = "def-br"
kind = "definition"
title = "Brauer group"
order = 1329
uses = ["def-sc-curves", "def-sc-gm-torsor", "def-weil-pbc-etale-site"]
lean = ["AlgebraicGeometry.Scheme.CohomologicalBrauerGroup"]
+++
For a scheme $X$ (for instance a curve $C$ as in [def-sc-curves]),
the *(cohomological) Brauer group* of $X$ is
$\Br(X)=H^2(X_{\Et},\mathbb G_m)$, the second cohomology of the sheaf
$\mathbb G_m$ of [def-sc-gm-torsor] on the small etale site
$X_{\Et}$ ([def-weil-pbc-etale-site]).
