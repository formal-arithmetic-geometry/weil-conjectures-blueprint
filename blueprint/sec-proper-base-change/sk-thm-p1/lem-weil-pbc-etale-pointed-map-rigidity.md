+++
id = "lem-weil-pbc-etale-pointed-map-rigidity"
kind = "lemma"
title = "Rigidity of maps from a local spectrum to an etale scheme"
uses = ["def-pc-scheme"]
lean = ["AlgebraicGeometry.etalePointedMapRigidity"]
source = "literature/stacks-project/morphisms.tex, Tag 02GE, open diagonal; algebra.tex Tag 08HQ, uniqueness; direct diagonal argument written in Lean by Y2"
+++
Let $B$ be a commutative local ring, $\Omega$ a field, and $\beta:B\to\Omega$ a local ring map `AlgebraicGeometry.LocallyRingedSpace.Hom` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Geometry/RingedSpace/LocallyRingedSpace.lean)). Let $f:X\to S$ be an etale morphism `AlgebraicGeometry.Etale` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/Etale.lean)) of schemes [def-pc-scheme]. If $u,v:\operatorname{Spec}B\to X$ `AlgebraicGeometry.Spec` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Scheme.lean)) satisfy $f\circ u=f\circ v$ and $u\circ\operatorname{Spec}\beta=v\circ\operatorname{Spec}\beta$, then $u=v$. Henselianity of $B$, algebraic closure of $\Omega$, and locality of $u$ and $v$ are not assumed.
