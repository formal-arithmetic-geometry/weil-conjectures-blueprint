+++
id = "proposition-six-operations-change-coefficients--23"
kind = "proposition"
title = "Transport of tensor–Hom evaluation"
order = 646046
aliases = ["bp-r197-23"]
lean = ["CategoryTheory.Functor.LaxMonoidal.ihomComparison_ev"]
uses = ["definition-change-of-coefficients-maps--6"]
+++
Let $T:\mathcal C\to\mathcal D$ be a lax monoidal functor between monoidal closed categories. With tensorator $\mu$ and internal-Hom comparison $v$, evaluation satisfies

$$
\operatorname{ev}_{TA,TB}\circ(1_{TA}\otimes v_{A,B})=
T(\operatorname{ev}_{A,B})\circ\mu_{A,\cHom(A,B)}.
$$

For derived scalar extension along $\Lambda\to\Lambda'$, with $v$ the comparison of Definition [definition-change-of-coefficients-maps](6), this says that scalar extension of the counit (evaluation) of the tensor–Hom adjunction is the counit over $\Lambda'$. The symmetry of the tensor product identifies this left-tensor convention with the right-tensor convention $-\otimes^{\mathbf L}K\dashv\cHom(K,-)$ of the proposition.
