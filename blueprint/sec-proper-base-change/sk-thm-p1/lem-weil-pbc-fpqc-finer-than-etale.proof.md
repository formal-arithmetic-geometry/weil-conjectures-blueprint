+++
kind = "proof"
of = "lem-weil-pbc-fpqc-finer-than-etale"
uses = ["def-weil-pbc-etale-site"]
+++
Apply Mathlib Scheme.ofArrows_mem_smallEtaleTopology_iff to the covering hypothesis. For each point x of U.left, membership in the resulting union of ranges gives an index i and membership of x in the range of (f i).left. Thus the underlying family is jointly surjective. ([def-weil-pbc-etale-site]).

Every underlying morphism (f i).left is etale by the Mathlib instances for morphisms in T.Etale. Etale morphisms are flat and locally of finite presentation. Scheme.ofArrows_mem_precoverage_iff combines these properties with joint surjectivity to place the family in fppfPrecoverage. ([def-weil-pbc-etale-site]).

Apply Mathlib Scheme.fppfPrecoverage_le_fpqcPrecoverage. This comparison proves the required quasi-compact covering condition from openness of flat locally finitely presented morphisms; its finite-open-subcover argument is the argument of Stacks Tag 022C. Together with flatness this gives fpqcPrecoverage membership. (`AlgebraicGeometry.Scheme.fpqcPrecoverage` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Sites/Fpqc.lean))).
