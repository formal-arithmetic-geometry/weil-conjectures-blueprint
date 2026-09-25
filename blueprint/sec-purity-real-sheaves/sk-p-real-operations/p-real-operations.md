+++
id = "p-real-operations"
kind = "theorem"
title = "Local Frobenius polynomials"
order = 2748
uses = ["def-tw-eigenvalue", "def-weil-punctual-weights", "def-wf-fundamental-representation", "def-wf-weil-group", "lem-wf-weil-fundamental-representation", "lem-wf-weil-group-constant-extension", "lem-wf-weil-group-exact-sequence", "prop-wf-weil-sheaf-representation-equivalence", "rem-ptr-wf-weil-group-1"]
tags = ["latex:proposition"]
+++
Keep the notation of [def-wf-fundamental-representation], [lem-wf-weil-fundamental-representation], and let $x$ be a closed point of
$C_0$ of degree $e_x$, with local Frobenius $F_x$ acting on the stalk
$\mathcal F_{\bar x}$; by [def-wf-weil-group], [lem-wf-weil-group-constant-extension], [lem-wf-weil-group-exact-sequence], [rem-ptr-wf-weil-group-1] it acts through a conjugacy
class of degree $e_x$ in $W(C_0)$. Use the tensor equivalence [prop-wf-weil-sheaf-representation-equivalence] of
[def-wf-fundamental-representation], [lem-wf-weil-fundamental-representation] for the operations of [sk-d-real-operations], and
write $P_x$ for the local characteristic polynomial of
[def-tw-eigenvalue], [def-weil-punctual-weights]. Then

$$
P_x(\mathcal F,T)=\det\bigl(1-T\,\rho(F_x)\mid V\bigr)
\qquad\text{for every closed }x .
$$

## Proof

Granted [def-wf-fundamental-representation], [lem-wf-weil-fundamental-representation], the operations of [sk-d-real-operations] on
lisse Weil sheaves are *defined* by transport along the equivalence, so
only the local polynomial needs an argument. Iterating the Frobenius
structure map $e_x$ times on the stalk at $\bar x$ realizes $F_x$ as $\rho$ of
any member of the degree-$e_x$ class supplied by $x$. A characteristic
polynomial is invariant under conjugation, so $\det(1-T\rho(F_x)\mid V)$ is
independent of the member chosen and agrees with the stalkwise $P_x$ of
[def-tw-eigenvalue], [def-weil-punctual-weights].

Uses: [sk-d-real-operations], [def-tw-eigenvalue], [def-weil-punctual-weights], [def-wf-weil-group], [lem-wf-weil-group-constant-extension], [lem-wf-weil-group-exact-sequence], [rem-ptr-wf-weil-group-1], [def-wf-fundamental-representation], [lem-wf-weil-fundamental-representation]
