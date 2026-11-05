+++
kind = "proof"
of = "theorem-verdier-biduality--3"
order = 844007
uses = ["theorem-verdier-biduality--2", "proposition-isomorphisms-reduce-finite-coefficients--3", "proposition-six-operations-change-coefficients"]
+++
This intermediate argument is bypassed by the Lean proof. In the coefficient-by-coefficient argument, [proposition-isomorphisms-reduce-finite-coefficients--3] applies to the double-dual transformation: [proposition-six-operations-change-coefficients] supplies the scalar comparisons and [theorem-verdier-biduality--2] supplies integral biduality. The mainline instead uses `AlgebraicGeometry.ProEtale.CondensedRing.isIso_verdierBiduality_integersToPadicAlgCl_obj` for the composite extension of scalars, as in [theorem-verdier-biduality--4].
