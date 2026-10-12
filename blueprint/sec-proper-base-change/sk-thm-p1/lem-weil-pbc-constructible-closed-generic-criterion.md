+++
id = "lem-weil-pbc-constructible-closed-generic-criterion"
kind = "lemma"
title = "Constructibility from generic finite local constancy on closed subschemes"
uses = ["def-constructible-constructible", "def-constructible-finite-locally-constant", "def-weil-pbc-etale-site", "def-weil-pbc-scheme-conventions", "prop-constructible-pullback"]
lean = ["AlgebraicGeometry.Scheme.constructible_of_closed_generic"]
source = "Stacks Project, Tag 09BH, Proposition 59.74.1 (3), proof of (3), Noetherian-induction step; Tag 095E, finite stratifications"
+++
Let $X$ be a Noetherian scheme [def-weil-pbc-scheme-conventions], $\Lambda$ a commutative ring, and $F$ a sheaf of $\Lambda$-modules on its small etale site [def-weil-pbc-etale-site]. Assume that for every closed immersion $i:Z\to X$ `AlgebraicGeometry.IsClosedImmersion` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/ClosedImmersion.lean)) with $Z$ Noetherian, there is a dense open $U\subseteq Z$ on which $i^*F$ [prop-constructible-pullback] is finite locally constant [def-constructible-finite-locally-constant]. Then $F$ is constructible [def-constructible-constructible]. No target sheaf or monomorphism is assumed, and no Noetherian condition on $\Lambda$ is needed.
