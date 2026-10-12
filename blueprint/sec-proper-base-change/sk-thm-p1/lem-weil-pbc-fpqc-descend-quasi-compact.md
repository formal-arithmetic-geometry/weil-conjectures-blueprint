+++
id = "lem-weil-pbc-fpqc-descend-quasi-compact"
kind = "lemma"
title = "Quasi-compactness descends along flat surjective quasi-compact morphisms (Stacks 02KQ)"
uses = ["def-pc-scheme", "def-weil-finite-type-morphism"]
lean = ["AlgebraicGeometry.quasiCompact_of_fpqc_baseChange"]
source = "literature/stacks-project/descent.tex, Descent, Lemma Tag 02KQ (lemma-descending-property-quasi-compact, line 5471: 'The property P(f) = \"f is quasi-compact\" is fpqc local on the base'), the direction 'the base change has P => f has P' of Definition Tag 02KO (definition-property-morphisms-local, line 5310) for the one-member fpqc covering $\\{g:S'\\to S\\}$. The one-member family $\\{g\\}$ is then an fpqc covering of $S$ (Topologies, Lemma Tag 03L7, lemma-recognize-fpqc-covering, topologies.tex line 2904, (2): for an affine open $U\\subseteq S$ the open $g^{-1}(U)$ is quasi-compact and $g(g^{-1}(U))=U$)"
+++
Let $g:S'\to S$ be a morphism of schemes [def-pc-scheme] which is flat `AlgebraicGeometry.Flat` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/Flat.lean)), surjective `AlgebraicGeometry.Surjective` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/UnderlyingMap.lean)) and quasi-compact [def-weil-finite-type-morphism] (the preimage of every affine open of $S$ is quasi-compact). Let $f:X\to S$ be a morphism of schemes and let $f':X\times_SS'\to S'$ be the second projection of the fibre product `CategoryTheory.Limits.pullback` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Limits/Shapes/Pullback/HasPullback.lean)). If $f'$ is quasi-compact, then $f$ is quasi-compact.
