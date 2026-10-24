+++
id = "sk-thm-pbc-henselian-h0"
kind = "theorem"
title = "Henselian-pair comparison in degree zero"
order = 1544
lean = ["AlgebraicGeometry.Etale.isIso_globalSectionsUpperStarMap_of_henselianRing", "AlgebraicGeometry.Etale.isIso_globalSectionsUpperStarMap_addCommGrpCat_of_henselianRing", "AlgebraicGeometry.Etale.globalSectionsUpperStarMap_naturality"]
uses = ["sk-def-conv", "sk-def-pbc-conventions"]
tags = ["sketch"]
+++
Let $(A,J)$ be a henselian pair, let $Z\to\operatorname{Spec}A$ be proper,
and let $i:Z_0=Z\times_A\operatorname{Spec}(A/J)\hookrightarrow Z$. For every
sheaf $F$ of abelian groups, or of $\Lambda$-modules, on $Z_{\Et}$, restriction
is a bijection

$$
\Gamma(Z,F)\xrightarrow{\ \sim\ }\Gamma(Z_0,i^{-1}F).
$$

The comparison is natural in $F$.
