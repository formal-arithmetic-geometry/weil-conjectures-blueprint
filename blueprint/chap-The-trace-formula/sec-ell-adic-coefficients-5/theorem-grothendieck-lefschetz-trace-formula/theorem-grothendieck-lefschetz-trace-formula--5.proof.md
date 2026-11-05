+++
kind = "proof"
of = "theorem-grothendieck-lefschetz-trace-formula--5"
order = 1017011
uses = ["lemma-perfect-complexes-geometric-point--4", "proposition-six-operations-dctf"]
+++
For finite $\Lambda$, compactly supported cohomology is bounded, has finite cohomology modules and has finite Tor amplitude. Since $\Lambda$ is Noetherian, `DerivedCategory.isPerfect_of_finiteTorAmplitude` gives perfectness, as in [lemma-perfect-complexes-geometric-point--4].

For $\Qlb$, the direct image $Ra_!K$ is a bounded Weil complex on $\operatorname{Spec}\Fq$. Choose lower and upper cohomological bounds. Outside them the cohomology sheaf is zero, and hence its global sections over $\operatorname{Spec}\overline{\Fq}$ vanish. This is `AlgebraicGeometry.WeilComplex.exists_subsingleton_cohomologyFrobeniusModule` applied to $Ra_!K$. The finite-dimensionality is part of the Frobenius module returned by `AlgebraicGeometry.WeilComplex.compactlySupportedCohomology`.
