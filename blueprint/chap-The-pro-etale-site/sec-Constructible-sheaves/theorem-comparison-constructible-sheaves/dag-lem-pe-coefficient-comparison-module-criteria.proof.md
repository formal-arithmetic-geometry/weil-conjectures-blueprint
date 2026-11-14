+++
kind = "proof"
of = "dag-lem-pe-coefficient-comparison-module-criteria"
tags = ["sheaf-dag"]
uses = ["dag-lem-pe-coefficient-bounded-classical-descent", "dag-lem-pe-coefficient-classical-single", "dag-lem-pe-coefficient-comparison-derived-functor", "dag-lem-pe-coefficient-comparison-constructibility-test"]
+++
1. place modules in degree zero. The degree-zero embedding is fully faithful
and its objects are bounded. The bounded derived comparison therefore makes the
composite of this embedding with derived inverse image fully faithful. The exact
inverse image commutes with degree-zero embeddings, so canceling the fully faithful
target embedding proves full faithfulness on modules. For a continuous target
module, its degree-zero complex has continuous cohomology (zero outside degree zero).
Bounded classical descent supplies a derived antecedent. Taking degree-zero
cohomology and using exactness supplies a module antecedent. Finally apply the
separate finite-local-system constructibility test. (uses [dag-lem-pe-coefficient-bounded-classical-descent], [dag-lem-pe-coefficient-classical-single], [dag-lem-pe-coefficient-comparison-derived-functor], [dag-lem-pe-coefficient-comparison-constructibility-test])
