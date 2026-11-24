+++
kind = "proof"
of = "lemma-bounding-weights-mixed-sheaf"
order = 1064
uses = ["lemma-perfect-complexes-geometric-point", "lemma-filtrations-spectra", "lemma-subobjects-quotients-weil-sheaves"]
+++
At every closed point $x$ the eigenvalues of
[$\operatorname{Frob}_x$](@theorem-trace-formula-euler-product) on the stalk of a [mixed](@definition-weights) sheaf are those on the
stalks of the quotients of its filtration. If the quotients have [weights
at most](@definition-weights) $w$, the sheaf is therefore [punctually of weights](@definition-weights) $\le w$.
Conversely, each nonzero
quotient has a nonzero stalk at some closed point $x$, and the
eigenvalues of [$\operatorname{Frob}_x$](@theorem-trace-formula-euler-product) there are eigenvalues on the
stalk of the sheaf. So if the sheaf is [punctually of weights](@definition-weights) $\le w$,
the weight of the quotient is at most $w$.
