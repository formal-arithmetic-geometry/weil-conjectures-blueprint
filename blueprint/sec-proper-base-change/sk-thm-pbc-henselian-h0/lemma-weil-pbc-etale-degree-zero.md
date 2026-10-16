+++
id = "lemma-weil-pbc-etale-degree-zero"
kind = "lemma"
title = "Etale henselian restriction in degree zero"
lean = ["AlgebraicGeometry.Etale.bijective_cohomologyMap_zero_of_henselianRing", "AlgebraicGeometry.Etale.isIso_globalSectionsUpperStarMap_of_henselianRing"]
order = 1116
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-finite-section-pullback", "def-weil-pbc-henselian-terminology", "def-weil-pbc-scheme-conventions", "def-weil-pbc-strict-henselian-setup", "lem-weil-pbc-closed-immersion-products", "lem-weil-pbc-finite-proper", "lem-weil-pbc-finite-pullback-identities", "lemma-weil-pbc-finite-pullback-closed-fibre", "lemma-weil-pbc-finite-pullback-composition", "lemma-weil-pbc-finite-pullback-descent", "lemma-weil-pbc-finite-pullback-identity", "lemma-weil-pbc-finite-refinement-etale-cover", "lemma-weil-pbc-spectral-restriction", "lemma-weil-pbc-stein-connectedness"]
+++
Let $(A,I)$ be henselian [def-weil-pbc-henselian-terminology] and let
$Y\to\operatorname{Spec}A$ be proper
[def-weil-pbc-scheme-conventions]. For every etale abelian sheaf $F$ on $Y$,

$$
  \Gamma(Y,F)\xrightarrow{\sim}\Gamma(Y_0,F|_{Y_0}).
$$

The isomorphism is natural in $F$, in finite pullback, and in morphisms of
henselian pairs.
