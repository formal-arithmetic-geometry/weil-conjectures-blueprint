+++
kind = "proof"
of = "proposition-twisting-weight-zero-adding-dual--8"
order = 1194015
uses = ["proposition-twisting-weight-zero-adding-dual--4"]
+++
Let $y$ be the closed point under $x$, of degree $d$. The trace at $x$
is the trace of the $(n/d)$th power of local Frobenius at $y$.
The stalk of $\mathcal G^\vee$ is the Frobenius-module dual of the stalk
of $\mathcal G$. Since the latter is pure of weight zero, the traces
of these powers are complex conjugates. Lean obtains
`AlgebraicGeometry.WeilSheaf.map_traceFunction_dual` from
`FrobeniusModule.IsPureOfWeight.map_trace_frobeniusEnd_dual_pow`.

Now take $\mathcal G=\mathcal F^0$, which is pure of weight zero by
[proposition-twisting-weight-zero-adding-dual--4]. Additivity of the trace
on a direct sum gives $z+\overline z=2\operatorname{Re}z$.
Lean makes this last computation using
`AlgebraicGeometry.WeilSheaf.traceFunction_biprod` in the proof of
`AlgebraicGeometry.WeilSheaf.traceEnergy_realEnvelope_le`.
