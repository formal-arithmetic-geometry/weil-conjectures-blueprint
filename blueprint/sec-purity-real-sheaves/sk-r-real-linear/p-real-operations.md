+++
id = "p-real-operations"
kind = "theorem"
title = "Local Frobenius polynomials"
lean = ["AlgebraicGeometry.WeilGroup.localPolynomial_eq_charpolyRev", "AlgebraicGeometry.WeilGroup.exists_equivalence_localPolynomial_stalk", "AlgebraicGeometry.WeilGroup.localPolynomial_eq_charpolyRev_of_isConj"]
order = 3976
uses = ["sk-d-real-weights", "def-real-weil-representation-operations", "def-weil-local-frobenius-trace", "def-wf-fundamental-representation", "def-wf-weil-group", "lem-wf-weil-group-constant-extension", "prop-wf-weil-sheaf-representation-equivalence"]
tags = ["latex:proposition"]
+++
Keep the notation of [prop-wf-weil-sheaf-representation-equivalence], so
that $(V,\rho)$ is the Weil fundamental representation of
[def-wf-fundamental-representation], and let $x$ be a closed point of
$C_0$ of degree $e_x$, with local Frobenius $F_x$ of
[def-weil-local-frobenius-trace] acting on the stalk
$\mathcal F_{\bar x}$; it acts through the conjugacy class of
geometric Frobenius elements at $x$ (images of the geometric Frobenius of
$k(x)$ under a decomposition-group map $\pi_1(x)\to\pi_1(C_0)$), of degree $e_x$, in the Weil group $W(C_0)$ of [def-wf-weil-group],
the geometric Frobenius over $k(x)$ having degree $e_x$ by
[lem-wf-weil-group-constant-extension]. Use the tensor equivalence
[prop-wf-weil-sheaf-representation-equivalence] for the operations of
[def-real-weil-representation-operations] (direct sum, tensor product, dual,
exterior powers, determinant), and
write $P_x(\mathcal F,T)=\det(1-TF_x\mid\mathcal F_{\bar x})$ for the local
characteristic factor of [sk-d-real-weights]. Then

$$
P_x(\mathcal F,T)=\det\bigl(1-T\,\rho(F_x)\mid V\bigr)
\qquad\text{for every closed }x .
$$
