+++
kind = "proof"
of = "proposition-function-sheaf-dictionary--4"
order = 1028010
uses = ["proposition-function-sheaf-dictionary--1", "proposition-function-sheaf-dictionary--3", "proposition-properties-trace"]
+++
For triangle additivity, take geometric stalks of the long exact sequence
of cohomology sheaves. The maps commute with Frobenius and the stalks are
finite-dimensional. Boundedness supplies a common finite set of degrees
outside which all three complexes vanish. Apply
`LinearMap.finsum_negOnePow_smul_trace_eq_add_of_exact` to the powers of the
local Frobenius. This is
`AlgebraicGeometry.WeilComplex.finsum_trace_stalk_homologySheaf_eq_add_of_distTriang`;
rewriting each stalk trace as a trace-function value gives the assertion.

For the comparison, take the direct sum of the Weil lower shriek images
of $K'_U$ and $K'_Z$. Its categorical traces are the sums of the traces of
these two images
(`AlgebraicGeometry.ProEtale.CondensedRing.WeilBoundedConstructible.exists_weilStalkTraceAlternatingSum_eq_add`).
By [proposition-function-sheaf-dictionary--3], the trace of either image
vanishes off the image of the corresponding immersion, since its fibre of
rational points is empty. On that image the fibre is a singleton; the
comparison hypothesis and [proposition-function-sheaf-dictionary--1] identify
its trace, after applying $\iota$, with $t_{K,m}$.
Every rational point of $X_0$ lies in exactly one of $U_0$ and $Z_0$.
Additivity of $\iota$ therefore gives the required comparison.
