+++
kind = "proof"
of = "theorem-grothendieck-lefschetz-trace-formula--6"
order = 1017013
uses = ["definition-constructible-sheaves"]
+++
The pullback of a constructible Weil sheaf to the geometric point is constructible, so its global sections are finite-dimensional. This gives `AlgebraicGeometry.WeilSheaf.finiteDimensional_stalkObj`.

Choose bounds $a,b$ for the underlying bounded complex and take $S=[a,b]\cap\mathbf Z$. The cohomology sheaves vanish below $a$ and above $b$, giving `AlgebraicGeometry.WeilComplex.exists_finset_isZero_homologySheaf`. Taking their stalks gives the asserted finiteness for the local trace.
