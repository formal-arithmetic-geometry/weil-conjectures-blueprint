+++
kind = "proof"
of = "proposition-weights-under-usual-operations--1"
order = 1070002
uses = ["lemma-filtrations-spectra"]
+++
At each closed point, the stalk map of $i$ is injective and commutes
with Frobenius. Every eigenvalue on $\mathcal G_{\bar x}$ is therefore
an eigenvalue on $\mathcal F_{\bar x}$, with the same absolute value.
Lean uses `AlgebraicGeometry.WeilSheaf.stalkAt_isPureOfWeight_of_mono`,
which applies `FrobeniusModule.IsPureOfWeight.of_injective` to the stalk map.
