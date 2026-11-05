+++
kind = "proof"
of = "proposition-weights-under-usual-operations--17"
order = 1070018
uses = []
+++
Every eigenvalue of the twisted Frobenius has the form $Q^{-r}\alpha$
for an eigenvalue $\alpha$ of the original Frobenius. Its absolute
value is
$$
|\iota(Q^{-r}\alpha)|=Q^{-r}Q^{w/2}=Q^{(w-2r)/2}.
$$
Lean uses `FrobeniusModule.hasEigenvalue_frobeniusEnd_rescale_iff`
and then this identity. The sheaf-to-module comparison is supplied
separately by `AlgebraicGeometry.WeilSheaf.tateTwistSheafIso` and the
cohomology comparisons in `WeilConjectures.WeilSheaf.TateTwistCohomology`;
these are not general mixed-sheaf weight theorems.
