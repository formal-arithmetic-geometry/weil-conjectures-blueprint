+++
id = "sk-p-real-operations"
kind = "proposition"
title = "Local Frobenius polynomials"
order = 2930
uses = ["sec-algebraic-groups-lie-algebras", "sec-poincare-duality", "sk-d-real-operations", "sk-d-real-weights", "sk-d-real-weil", "sk-i-real-sheaves"]
lean = ["AlgebraicGeometry.WeilGroup.localPolynomial_eq_charpolyRev_of_isConj"]
tags = ["sketch"]
+++
Keep the notation of [sk-i-real-sheaves], and let $x$ be a closed point of
$C_0$ of degree $e_x$, with local Frobenius $F_x$ acting on the stalk
$\mathcal F_{\bar x}$; by [sk-d-real-weil] it acts through the
conjugacy class in $W(C_0)$ of geometric Frobenius elements at $x$,
which have degree $e_x$. Use the tensor equivalence of
[sk-i-real-sheaves] for the operations of [sk-d-real-operations], and
write $P_x$ for the local characteristic polynomial of
[sk-d-real-weights]. Then

$$
P_x(\mathcal F,T)=\det\bigl(1-T\,\rho(g)\mid V\bigr)
$$

for every closed point $x$ and every $g\in W(C_0)$ conjugate in $W(C_0)$
to the local Frobenius element at $x$; in particular $P_x$ does not depend
on the choice of that element within its conjugacy class.
