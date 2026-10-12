+++
id = "lem-weil-pbc-normal-extension-purely-inseparable-then-galois"
kind = "lemma"
title = "A normal extension is Galois over a purely inseparable subextension (Stacks 030M (2))"
lean = ["Normal.fixedField_purelyInseparable_and_galois"]
source = "literature/stacks-project/fields.tex, Fields, Lemma Tag 030M (lemma-normal-case, line 3666), part (2), with $E_{insep}=E^{\\mathrm{Aut}(E/F)}$ as in its proof ('Details omitted'); tag verified in literature/stacks-project/tags/tags (030M,fields-lemma-normal-case)"
+++
Let $F$ be a field and $E/F$ a field extension `Algebra` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Algebra/Defs.lean)) which is algebraic and normal: every $\alpha\in E$ is algebraic over $F$ `IsAlgebraic` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Algebraic/Defs.lean)) and its minimal polynomial over $F$ is a product of polynomials of degree one in $E[T]$. Let $E_{insep}=\{x\in E:\sigma(x)=x$ for every $F$-algebra automorphism $\sigma$ of $E\}$. Then $E_{insep}$ is a subfield of $E$ containing $F$, the extension $E_{insep}/F$ is purely inseparable `IsPurelyInseparable, Module.Finite` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/FieldTheory/PurelyInseparable/Basic.lean)), and the extension $E/E_{insep}$ is separable algebraic `Algebra.IsSeparable` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/FieldTheory/Separable.lean)) and normal (i.e. Galois).
