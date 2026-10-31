+++
id = "sk-def-wrp-real-definition"
kind = "definition"
title = "Real sheaves"
order = 684
lean = ["AlgebraicGeometry.WeilGroup.IsReal"]
uses = ["sk-d-real-weights"]
tags = ["sketch"]
+++
A Weil sheaf $\mathcal G$ is $\iota$-real if
$\iota\det(1-T\operatorname{Frob}_x\mid\mathcal G_{\bar x})$ has real coefficients for
every closed point; equivalently, the multiset of its complex
eigenvalues at each point is stable under complex conjugation. In
particular, the traces of all positive powers of local Frobenius are
real.

*Complement.* In terms of the local polynomials of [sk-d-real-weights],
$\mathcal G$ is $\iota$-real if and only if
$\iota P_x(\mathcal G,T)\in\mathbf R[T]$ for every closed point $x$
([def-wf-iota-real]).
