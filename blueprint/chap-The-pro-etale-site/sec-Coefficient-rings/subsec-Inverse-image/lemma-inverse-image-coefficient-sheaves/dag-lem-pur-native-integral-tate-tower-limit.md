+++
id = "dag-lem-pur-native-integral-tate-tower-limit"
kind = "dag-lemma"
title = "Inverse image preserves the native integral Tate tower limit"
name_showing = false
order = 187520
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--2"
dag_id = "lem-pur-native-integral-tate-tower-limit"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.spIntegralTwist_inverseImage_isLimit"]
uses = ["dag-sk-def-sp-tate-twist"]
+++
Let ell be prime and let f : X → Y be a morphism of schemes on which ell is invertible. For every finite subextension E of the fixed p-adic algebraic closure, the inverse image under the sheaf functor of `def-weil-proetale-inverse-image` of the abelian cone underlying the specified O_E-module inverse limit spIntegralTwistSystem Y ell E of [dag-sk-def-sp-tate-twist] is a limiting cone. This concerns only this compatible locally rank-one tower, and does not assert preservation of arbitrary inverse limits.

(SHEAF DAG node `lem-pur-native-integral-tate-tower-limit`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--2]. DAG kind: statement. Placed through `det-prop-sfb-cartesian-coefficients-twists` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-proetale-inverse-image`.
