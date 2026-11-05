+++
id = "sk-def-trace-cup"
kind = "definition"
title = "Trace and trace–cup pairing"
lean = ["AlgebraicGeometry.Etale.TateOrientation.traceCupPairing"]
order = 3604
uses = ["sk-def-ops", "sk-def-sf-orientation"]
+++
In the setting of [sk-def-set] with $X_0$ in addition *proper*,
so that $R\Gamma_c=R\Gamma$, the trace map is
$\operatorname{tr}^{(-d)}_X:H^{2d}(X,\Lambda)\to\Lambda(-d)$, the
untwisted form of the counit of $Ra_{X!}\dashv Ra_X^!$ read through the
orientation; the *trace–cup pairing* is

$$
\langle x,y\rangle_i=\operatorname{tr}^{(-d)}_X(x\smile y):
H^i(X,\Lambda)\times H^{2d-i}(X,\Lambda)\to\Lambda(-d).
$$
