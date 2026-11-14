+++
kind = "proof"
of = "dag-det-pe-classical-derived-equivalence"
tags = ["sheaf-dag"]
uses = ["dag-lem-pe-classical-derived-image", "dag-lem-pe-classical-derived-counit"]
+++
1. The exact comparison inverse image has classical cohomology, including the comparison between small and standard derived-category homology models. (uses [dag-lem-pe-classical-derived-image])
2. The derived counit is invertible on classical bounded-below objects by truncation induction and the upper-tail comparison. (uses [dag-lem-pe-classical-derived-counit])
3. Lift inverse image to the full classical subcategory and restrict the given adjunction along its fully faithful inclusion. Reflect invertibility of its unit and counit through the inclusions, and apply Adjunction.toEquivalence. The forward and inverse comparison isomorphisms are the lift factorization and identity.
