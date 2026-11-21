+++
id = "dag-lem-sp-constant-zmod-scalar-tensor"
kind = "dag-lemma"
title = "Absolute tensor agrees with extension from a constant cyclic ring"
name_showing = false
order = 187549
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--2"
dag_id = "lem-sp-constant-zmod-scalar-tensor"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.Scheme.constantZMod_scalarTensor"]
uses = ["dag-def-weil-pbc-proetale-site", "dag-def-weil-pbc-constant-sheaf", "dag-def-pur-sheaf-tensor-product"]
+++
Let X be an arbitrary scheme [dag-def-weil-pbc-proetale-site]. Fix natural numbers ell,n, put N=ell^(n+1), and write R=(ULift(ZMod N))_X for the constant commutative ring sheaf, using the canonical universe lift [dag-def-weil-pbc-constant-sheaf]. Let A be any commutative ring in the coefficient universe, and let a:ZMod N -> A be a unital ring homomorphism. Let M be any sheaf of R-modules `def-weil-sheaf-of-modules-category`. Use the constant-ring scalar map a_X:R -> A_X `def-pur-finite-tate-line-signed-comparison`. Then there is an isomorphism of abelian sheaves A_X tensor_Z U(M) ≅ U(A_X tensor_R M). Here U forgets the module action, the left tensor is the sheafified objectwise integer tensor `det-def-sfb-sheaf-tensor-structure`, and the right tensor is the actual module scalar extension [dag-def-pur-sheaf-tensor-product]. Neither finiteness of A nor invertibility or primality of ell is assumed.

(SHEAF DAG node `lem-sp-constant-zmod-scalar-tensor`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--2]. DAG kind: statement. Placed through `det-prop-sfb-cartesian-coefficients-twists` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-sheaf-of-modules-category`, `def-pur-finite-tate-line-signed-comparison`, `det-def-sfb-sheaf-tensor-structure`.
