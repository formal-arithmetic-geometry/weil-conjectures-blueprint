+++
kind = "proof"
of = "dag-lem-route-sp-integral-twist-level-comparison"
tags = ["sheaf-dag"]
uses = ["dag-lem-sp-ell-quotient-finite-discrete", "dag-lem-sp-constant-zmod-scalar-tensor"]
+++
1. The generator ell^(n+1) lies in the ideal defining B=O_E/(ell^(n+1)); therefore its image is zero in B and in ULift B. The usual ZMod cast homomorphism gives the required a:ZMod(ell^(n+1))->ULift B. Equip B with the discrete topology; its finiteness is spEllQuotient_finite_continuous, with no invertibility assumption on X. (uses [dag-lem-sp-ell-quotient-finite-discrete])
2. Apply finiteDiscreteCondensedRing_constant to B, then finiteDiscreteSchemeRing_constant to its ring-object isomorphism. This identifies the underlying pulled-back finite coefficient sheaf with the constant additive sheaf of ULift B on X. Tensor the inverse coefficient identification with the identity of the actual roots-of-unity sheaf. (uses `lem-weil-pbc-finite-discrete-condensed-ring-constant`, `lem-weil-pbc-finite-discrete-scheme-ring-constant`)
3. Apply constantZMod_scalarTensor to the actual root module and a. It identifies the constant ULift B sheaf tensored over the integers with the underlying root sheaf with the underlying ordinary scalar extension along a, which is by definition tateFiniteLine. Compose with the tensor isomorphism of the preceding step. Restriction of scalars in spIntegralTwistLevel changes only the action, so its underlying object is definitionally the source of this composite. This constructs the requested a and isomorphism directly. (uses [dag-lem-sp-constant-zmod-scalar-tensor])

Proof dependencies not drawn: `lem-weil-pbc-finite-discrete-condensed-ring-constant`, `lem-weil-pbc-finite-discrete-scheme-ring-constant`.
