+++
kind = "proof"
of = "lem-weil-pbc-lift-to-injective-unique-up-to-homotopy"
uses = ["def-sp-abelian", "def-sp-injective-resolutions", "def-weil-abstract-derived-category"]
+++
Use the bounded-below hypothesis to instantiate `IsStrictlyGE`, then Mathlib proves a complex with injective terms is K-injective via `isKInjective_of_injective`. ([def-sp-injective-resolutions], `CochainComplex.isKInjective_of_injective` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Homology/HomotopyCategory/KInjective.lean))).

Pass the given homotopy through the derived localization using `DerivedCategory.Q_map_eq_of_homotopy`. Since α is a quasi-isomorphism, its localized map is an isomorphism; cancel it to show the localized maps of β₁ and β₂ agree. ([def-sp-abelian], [def-weil-abstract-derived-category]).

The bijectivity theorem `CochainComplex.IsKInjective.Qh_map_bijective` reflects equality of localized maps into the K-injective target back to equality in the homotopy category. `HomotopyCategory.homotopyOfEq` then supplies the required homotopy. ([def-weil-abstract-derived-category]).
