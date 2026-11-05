+++
id = "proposition-six-operations-change-coefficients--13"
kind = "proposition"
title = "Internal Hom: comparison for a composite functor"
order = 645026
aliases = ["bp-r197-13"]
lean = ["CategoryTheory.Functor.LaxMonoidal.ihomComparison_comp_app"]
uses = []
+++
Let $T:\mathcal C\to\mathcal D$ and $U:\mathcal D\to\mathcal E$ be lax monoidal functors between monoidal closed categories. Write $v^T_{A,B}:T\cHom(A,B)\to\cHom(TA,TB)$ for the internal-Hom comparison. Then
$$
v^{UT}_{A,B}=v^U_{TA,TB}\circ U(v^T_{A,B}).
$$
Thus the internal-Hom comparison for a composite of derived scalar-extension functors is the composite of their comparisons. No invertibility hypothesis is needed for this identity.
