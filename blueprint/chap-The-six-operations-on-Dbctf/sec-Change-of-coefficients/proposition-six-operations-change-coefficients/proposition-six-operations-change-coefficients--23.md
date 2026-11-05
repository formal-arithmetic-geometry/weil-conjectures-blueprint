+++
id = "proposition-six-operations-change-coefficients--23"
kind = "proposition"
title = "Transport of tensor–Hom evaluation"
order = 645046
aliases = ["bp-r197-23"]
lean = ["CategoryTheory.Functor.LaxMonoidal.ihomComparison_ev"]
uses = []
+++
Let $T:\mathcal C\to\mathcal D$ be a lax monoidal functor between monoidal closed categories. With tensorator $\mu$ and internal-Hom comparison $v$, evaluation satisfies
$$
\operatorname{ev}_{TA,TB}\circ(1_{TA}\otimes v_{A,B})=
T(\operatorname{ev}_{A,B})\circ\mu_{A,\cHom(A,B)}.
$$
For derived scalar extension, this is compatibility with the counit of tensor–Hom adjunction. The symmetry identifies this left-tensor convention with the right-tensor convention of the human statement.
