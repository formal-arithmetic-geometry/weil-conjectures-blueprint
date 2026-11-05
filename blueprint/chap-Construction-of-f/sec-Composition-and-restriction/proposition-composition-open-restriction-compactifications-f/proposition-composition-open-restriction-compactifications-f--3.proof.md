+++
kind = "proof"
of = "proposition-composition-open-restriction-compactifications-f--3"
order = 530012
uses = ["proposition-composition-base-change-rf-shriek", "proposition-sp-unique-adjoint"]
+++
Identify the lower shriek of the identity with the identity functor.
For finite coefficients, transport the identity adjunction across
`AlgebraicGeometry.Etale.rightDerivedLowerShriekIdIso` and apply uniqueness
of right adjoints to the exceptional adjunction. For $\Qbarl$-coefficients,
take the conjugate of the inverse of
`AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekId`
under the exceptional adjunction and the identity adjunction.
