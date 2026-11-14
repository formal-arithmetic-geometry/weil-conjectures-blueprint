+++
kind = "proof"
of = "dag-lem-pe-coefficient-bounded-classical-descent"
tags = ["sheaf-dag"]
uses = ["dag-lem-pe-coefficient-comparison-injective-acyclic", "dag-lem-pe-coefficient-classical-module-origin"]
+++
1. Use the already proved coefficient-sized module exactness. The canonical module adjunction is additive, and the two module categories are Grothendieck abelian, hence have enough injectives. Apply the injective unit/acyclicity lemma and the general derived-unit theorem to obtain invertibility of the unit of the bounded-below derived adjunction. (uses [dag-lem-pe-coefficient-comparison-injective-acyclic], `lem-pe-constructible-comparison-module-exact`, `lem-cbc-derived-unit-injective-acyclicity`)
2. The isomorphic derived unit makes derived inverse image fully faithful on D+. Regard bounded source objects as D+ objects and use the fully faithful inclusion into the unbounded derived category to obtain the actual Hom-set bijection.
3. Each cohomology module with the stated continuity maps has an ordinary antecedent. On single complexes in this essential image, the derived counit is invertible by the fully faithful derived adjunction and compatibility with singleFunctor. The finite truncation devissage theorem propagates this to a bounded object. Its derived direct image is the desired antecedent. (uses [dag-lem-pe-coefficient-classical-module-origin])
4. For any D with the given factorization through Q, uniqueness of localization lifts gives a natural isomorphism from exact derived inverse image to D. Transport the Hom-set bijections and counit isomorphisms through it. These steps are proved in Lean, with two proved private categorical helpers.

Proof dependencies not drawn: `lem-pe-constructible-comparison-module-exact`, `lem-cbc-derived-unit-injective-acyclicity`.
