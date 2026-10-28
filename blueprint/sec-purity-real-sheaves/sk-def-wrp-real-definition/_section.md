+++
id = "sk-def-wrp-real-definition"
kind = "definition"
title = "Real and realizable sheaves"
order = 4082
uses = ["sk-d-real-weights"]
lean = ["AlgebraicGeometry.WeilGroup.IsReal"]
tags = ["sketch"]
+++
A Weil sheaf $\mathcal G$ is $\iota$-real if
$\iota\det(1-TF_x\mid\mathcal G_{\bar x})$ has real coefficients for
every closed point; equivalently, the multiset of its complex
eigenvalues at each point is stable under complex conjugation. In
particular, the traces of all positive powers of local Frobenius are
real. A lisse sheaf is $\iota$-realizable if it is
a direct summand of an $\iota$-real lisse Weil sheaf.

*Complement.* In terms of the local polynomials of [sk-d-real-weights],
$\mathcal G$ is $\iota$-real if and only if
$\iota P_x(\mathcal G,T)\in\mathbf R[T]$ for every closed point $x$
([def-wf-iota-real]).
