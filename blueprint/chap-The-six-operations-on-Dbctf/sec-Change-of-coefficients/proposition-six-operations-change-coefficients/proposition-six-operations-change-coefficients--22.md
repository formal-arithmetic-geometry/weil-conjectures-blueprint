+++
id = "proposition-six-operations-change-coefficients--22"
kind = "proposition"
title = "Transport of tensor–Hom coevaluation"
order = 645044
aliases = ["bp-r197-22"]
lean = ["CategoryTheory.Functor.LaxMonoidal.coev_ihomComparison"]
uses = []
+++
This clause is bypassed by the main theorem's Lean route: the following general coevaluation identity exists in the source, but is absent from the supplied declaration index.

Let $T:\mathcal C\to\mathcal D$ be a lax monoidal functor between monoidal closed categories, with tensorator $\mu_{A,B}:TA\otimes TB\to T(A\otimes B)$ and internal-Hom comparison $v$. Then
$$
v_{A,A\otimes B}\circ T(\operatorname{coev}_{A,B})=
\cHom(TA,\mu_{A,B})\circ\operatorname{coev}_{TA,TB}.
$$
For derived scalar extension, this is transport of the unit of tensor–Hom adjunction. The formula uses $A\otimes-$; the symmetry identifies it with the right-tensor convention in the human statement.
