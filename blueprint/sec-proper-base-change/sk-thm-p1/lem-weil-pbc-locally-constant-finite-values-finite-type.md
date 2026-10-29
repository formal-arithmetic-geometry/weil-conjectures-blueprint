+++
id = "lem-weil-pbc-locally-constant-finite-values-finite-type"
kind = "lemma"
title = "Locally constant with finitely generated values implies finite type"
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site"]
lean = ["AlgebraicGeometry.Scheme.locallyConstant_finiteValues_isFiniteType"]
order = 1989
+++
Let $Y$ be a scheme, $\Lambda$ a commutative ring and $\mathcal G$ a sheaf of $\Lambda_Y$-modules on the small etale site $Y_{\Et}$ [def-weil-pbc-etale-site], [def-weil-pbc-etale-sheaves]. Let $\{u_i:U_i\to Y\}_{i\in I}$ be an etale covering (a jointly surjective family of etale morphisms) and, for each $i$, $M_i$ a finitely generated $\Lambda$-module together with an isomorphism of sheaves of $\Lambda$-modules $\mathcal G|_{U_i}\cong\underline{M_i}$, where $\mathcal G|_{U_i}$ is the restriction to the localised site $Y_{\Et}/U_i=(U_i)_{\Et}$ and $\underline{M_i}$ is the constant sheaf of $\Lambda$-modules with value $M_i$ on $(U_i)_{\Et}$. Then $\mathcal G$ is of finite type; more precisely, if $x_{i1},\dots,x_{in_i}$ generate $M_i$, then the global sections of $\mathcal G|_{U_i}$ corresponding to the images of the $x_{ij}$ in $\underline{M_i}(U_i)$ generate $\mathcal G|_{U_i}$ as a $\Lambda_Y|_{U_i}$-module.
