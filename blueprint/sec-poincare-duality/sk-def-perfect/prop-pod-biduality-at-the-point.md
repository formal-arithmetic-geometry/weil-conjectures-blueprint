+++
id = "prop-pod-biduality-at-the-point"
kind = "theorem"
title = "Biduality at the point"
lean = ["DerivedCategory.IsPerfect.isDualizable", "DerivedCategory.IsPerfect.isIso_toIhomIhomUnit", "DerivedCategory.IsPerfect.isIso_ihomUnitTensorToIhom"]
order = 3601
tags = ["latex:proposition"]
uses = ["def-pod-conventions", "def-pod-perfect-point-complex", "def-weil-derived-pullback-tensor-hom", "def-weil-finite-coefficient-point", "def-weil-geometric-hypotheses", "lem-pod-finite-projective-tensor-hom"]
+++
In the Poincare duality conventions of this chapter (the fixed setting),
let $C$ be a perfect point complex. The
evaluation and coevaluation give a canonical isomorphism

$$
C\xrightarrow{\ \sim\ }C^{\vee\vee},
$$

and for every object $D$ of the category at the point, the canonical
tensor–internal-Hom comparison

$$
C^\vee\otimes_A^LD\xrightarrow{\ \sim\ }R\operatorname{Hom}_A(C,D)
$$

is an isomorphism.
