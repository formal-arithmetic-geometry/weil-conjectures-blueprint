+++
id = "lem-weil-pbc-etale-near-prime-naive-cotangent-vanishing"
kind = "lemma"
title = "Vanishing of H_1 and of the differentials at a prime gives an etale localization"
lean = ["AlgebraicGeometry.exists_etale_away_of_localized_cotangent_vanishing"]
+++
Let $A\to C$ be a homomorphism of commutative rings making $C$ a finitely presented $A$-algebra, and $\mathfrak q\subset C$ a prime ideal such that the localizations at $\mathfrak q$ of the $C$-modules $H_1(L_{C/A})$ `Algebra.Smooth` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Smooth/Basic.lean)) and $\Omega_{C/A}$ `KaehlerDifferential` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Kaehler/Basic.lean)) vanish: $H_1(L_{C/A})_{\mathfrak q}=0$ and $(\Omega_{C/A})_{\mathfrak q}=0$. Then there is $h\in C\setminus\mathfrak q$ such that $\operatorname{Spec}C_h\to\operatorname{Spec}A$, induced by $A\to C\to C_h$, is etale `AlgebraicGeometry.Etale` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/Etale.lean)).
