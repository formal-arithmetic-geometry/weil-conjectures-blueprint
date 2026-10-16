+++
id = "lem-weil-pbc-normal-constant-generic"
kind = "lemma"
title = "Constant sheaves on a normal scheme and the generic point"
lean = ["AlgebraicGeometry.Etale.isIso_unit_constantSheaf_of_isIntegrallyClosed"]
order = 1184
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-geometric-stalks", "def-weil-pbc-scheme-conventions", "def-weil-pbc-strict-henselization-limit", "lemma-weil-pbc-etale-cohomology-continuity", "lemma-weil-pbc-geometric-stalk-conservative"]
+++
Let $Y$ be an integral normal scheme with function field $K$, let
$g:\operatorname{Spec}K\to Y$ be the inclusion of the generic point, and let
$\underline E$ be the constant etale sheaf with value a finite abelian group
$E$. Then the canonical map $\underline E\to g_*\underline E$ is an
isomorphism. The same holds for the inclusion $j:U\hookrightarrow Y$ of a
nonempty open subscheme.
