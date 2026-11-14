+++
kind = "proof"
of = "dag-lem-pe-coefficient-constructible-module-equivalence"
tags = ["sheaf-dag"]
+++
1. the constructibility test lifts the canonical inverse image to the two full
subcategories. Ambient full faithfulness gives fullness and faithfulness there.
A constructible target is continuous by the finite-cover classicality argument;
classical descent supplies an etale antecedent and an isomorphism of its image
with the target. Constructibility is invariant under that isomorphism and reflected
by inverse image, so this antecedent belongs to the source full subcategory.
This proves essential surjectivity. The resulting equivalence uses this lifted
functor itself, so its forward-functor identification is reflexive. (uses `lem-pe-coefficient-comparison-module-criteria`, `lem-pe-coefficient-constructible-classical`, `lem-pe-coefficient-constructible-iso`)

Proof dependencies not drawn: `lem-pe-coefficient-comparison-module-criteria`, `lem-pe-coefficient-constructible-classical`, `lem-pe-coefficient-constructible-iso`.
