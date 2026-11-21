+++
kind = "proof"
of = "dag-sk-thm-pe-constructible-comparison"
tags = ["sheaf-dag"]
uses = ["dag-lem-pe-coefficient-constructible-locality", "dag-lem-pe-coefficient-comparison-derived-functor"]
+++
1. Prove the local clause by refining point neighborhoods to affine opens, pulling back their strata, taking a finite subcover on each affine, and applying stratification gluing. Convert finite type and finite presentation over the Noetherian coefficient ring. (uses [dag-lem-pe-coefficient-constructible-locality])
2. For a qcqs scheme globalize the affine constructibility partitions using a finite affine cover and the factorization gluing lemma, then apply single-stratification continuity. This is the classicality clause. (uses `lem-pe-coefficient-constructible-classical`)
3. Lift canonical module inverse image to the constructible full subcategories. Full faithfulness, classical descent and reflection of the finite-local-system property give the constructible module equivalence, with forward functor identified by the reflexive isomorphism. (uses `lem-pe-coefficient-constructible-module-equivalence`)
4. The exact canonical module inverse image produces a functor D on the standard derived categories, with the actual complex localization factorization and cohomology comparison. Restrict to bounded constructible objects: preserve constructibility and finite cohomological bounds; for essential surjectivity use classical descent, reflect constructibility, and use full faithfulness to reflect zero cohomology in the same interval. (uses [dag-lem-pe-coefficient-comparison-derived-functor], `lem-pe-coefficient-bounded-constructible-restriction`)

Proof dependencies not drawn: `lem-pe-coefficient-constructible-classical`, `lem-pe-coefficient-constructible-module-equivalence`, `lem-pe-coefficient-bounded-constructible-restriction`.
