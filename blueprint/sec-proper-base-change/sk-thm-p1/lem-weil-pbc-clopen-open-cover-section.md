+++
id = "lem-weil-pbc-clopen-open-cover-section"
kind = "lemma"
title = "A finite surjective disjoint union of open immersions has a section"
uses = ["def-pc-scheme"]
lean = ["AlgebraicGeometry.exists_section_of_finite_clopen_open_cover"]
source = "literature/stacks-project/etale-cohomology.tex, Lemma 59.80.6 (Tag 09ZA), proof, final paragraph: the finite cover by open-and-closed images is refined to disjoint clopen strata and the inverse open immersions glue to a section"
+++
Let $Z$ be a scheme [def-pc-scheme] and let $p:V\to Z$ be a finite `AlgebraicGeometry.IsFinite, AlgebraicGeometry.IsIntegralHom` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/Finite.lean), [Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/Integral.lean)) surjective `AlgebraicGeometry.Surjective` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/UnderlyingMap.lean)) morphism. Suppose that $V=\coprod_{i=1}^nV_i$ is a finite disjoint union of open and closed subschemes such that every restriction $p_i:V_i\to Z$ is an open immersion `AlgebraicGeometry.IsOpenImmersion` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/OpenImmersion.lean)). Then $p$ has a section $s:Z\to V$ with $p\circ s=\mathrm{id}_Z$.
