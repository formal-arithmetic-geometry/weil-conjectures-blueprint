+++
kind = "proof"
of = "proposition-weights-under-usual-operations--2"
order = 1070003
uses = ["lemma-filtrations-spectra"]
+++
The stalk map of $p$ is a Frobenius-equivariant surjection. The
eigenvalues of its quotient occur among those of its source, so their
weights remain $w$. Lean uses
`AlgebraicGeometry.WeilSheaf.stalkAt_isPureOfWeight_of_epi` and
`FrobeniusModule.IsPureOfWeight.of_surjective`.
