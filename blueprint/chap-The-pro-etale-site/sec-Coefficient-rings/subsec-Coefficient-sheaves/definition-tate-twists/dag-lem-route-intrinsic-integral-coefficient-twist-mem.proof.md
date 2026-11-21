+++
kind = "proof"
of = "dag-lem-route-intrinsic-integral-coefficient-twist-mem"
tags = ["sheaf-dag"]
uses = ["dag-lem-pur-signed-integral-coefficient-twist-constructible"]
+++
1. Apply integralCoefficientTwist_constructible to the identical signed completed line. It supplies legacy derived completeness and integers a <= b with constructibility and cohomological support bounds for every positive reduction. (uses [dag-lem-pur-signed-integral-coefficient-twist-constructible])
2. Convert the completeness clause with the reverse implication of sfDerivedComplete_iff_legacy. The integralDerivedReduction functor is definitionally scalarReductionDerivedExtension, and Set.Icc membership is the pair of lower and upper inequalities. Reuse the same bounds and each finite constructibility and support proof. These data give both conjuncts of sfIntegralConstructible. (uses `lem-sf-derived-complete-legacy-comparison`, `def-weil-integral-derived-reduction`)

Proof dependencies not drawn: `lem-sf-derived-complete-legacy-comparison`, `def-weil-integral-derived-reduction`.
