+++
id = "lem-weil-pbc-normal-constant-generic"
kind = "lemma"
title = "Constant sheaves on a normal scheme and the generic point"
lean = ["AlgebraicGeometry.Etale.isIso_unit_constantSheaf_of_isIntegrallyClosed"]
order = 1586
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-geometric-stalks", "def-weil-pbc-scheme-conventions", "def-weil-pbc-strict-henselization-limit", "lemma-weil-pbc-etale-cohomology-continuity", "lemma-weil-pbc-geometric-stalk-conservative"]
+++
Let $Y$ be an integral scheme all of whose local rings are integrally
closed domains, with function field $K$, let
$g:\operatorname{Spec}K\to Y$ be the inclusion of the generic point, let
$\Lambda$ be a commutative ring and let $\underline M$ be the constant etale
sheaf of $\Lambda$-modules with value a $\Lambda$-module $M$. Then the unit
$\underline M\to g_*g^{-1}\underline M=g_*\underline M$ of the adjunction
$g^{-1}\dashv g_*$ is an isomorphism. The same holds for the inclusion $j:U\hookrightarrow Y$ of a
nonempty open subscheme.
