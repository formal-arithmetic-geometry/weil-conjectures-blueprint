+++
kind = "proof"
of = "theorem-verdier-biduality--6"
order = 844013
uses = ["theorem-verdier-biduality--4"]
+++
First identify the underlying geometric complex of $\omega_X$ with the condensed dualizing complex, using the adjunction defining $a_X^!$. This is `AlgebraicGeometry.WeilComplex.nonempty_nativeGeometricForget_obj_iso_of_adjunction`.

Construct the natural double-dual map on Weil complexes from evaluation. After forgetting the Weil structure, its invertibility follows from [theorem-verdier-biduality--4], through `AlgebraicGeometry.ProEtaleWeilSheaf.quasiIso_bifunctorHomBidual_ordinary`. Forgetting detects quasi-isomorphisms, so every component is invertible. They assemble to the natural isomorphism of `AlgebraicGeometry.WeilComplex.nonempty_iso_dual_rightOp_comp_dual`, applied to $\omega_X$.

For any contravariant functor $D$ with a natural isomorphism $\mathrm{id}\simeq DD$, the same functor on the opposite category is a quasi-inverse. Applying `CategoryTheory.Functor.rightOpEquivalenceOfIsoRightOpComp` gives the asserted anti-equivalence.
