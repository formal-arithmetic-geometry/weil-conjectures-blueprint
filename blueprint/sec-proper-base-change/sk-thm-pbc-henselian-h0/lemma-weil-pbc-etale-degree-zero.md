+++
id = "lemma-weil-pbc-etale-degree-zero"
kind = "lemma"
title = "Etale henselian restriction in degree zero"
lean = ["AlgebraicGeometry.Etale.isIso_globalSectionsUpperStarMap_of_henselianRing", "AlgebraicGeometry.Etale.isIso_globalSectionsUpperStarMap_addCommGrpCat_of_henselianRing", "AlgebraicGeometry.Etale.globalSectionsUpperStarMap_naturality"]
order = 1552
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-finite-section-pullback", "def-weil-pbc-henselian-terminology", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-finite-proper", "lemma-weil-pbc-finite-pullback-composition", "lemma-weil-pbc-finite-refinement-etale-cover", "lemma-weil-pbc-spectral-restriction", "lemma-weil-pbc-stein-connectedness"]
+++
Let $(A,I)$ be a henselian pair [def-weil-pbc-henselian-terminology], let
$p:Y\to\operatorname{Spec}A$ be proper [def-weil-pbc-scheme-conventions], and
let $i:Y_0=Y\times_{\operatorname{Spec}A}\operatorname{Spec}(A/I)\to Y$ be the
closed fibre. Let $\Lambda$ be a commutative ring. For every etale sheaf $F$ of
$\Lambda$-modules on the small etale site [def-weil-pbc-etale-site] of $Y$
[def-weil-pbc-etale-sheaves], in particular for every
etale abelian sheaf, the pullback of global sections
[def-weil-pbc-finite-section-pullback] along $i$, i.e. restriction to the closed
fibre,

$$
  i^\sharp:\Gamma(Y,F)\xrightarrow{\sim}\Gamma(Y_0,i^{-1}F),
$$

is an isomorphism. It is natural in $F$.
