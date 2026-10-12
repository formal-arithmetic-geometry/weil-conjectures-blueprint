+++
id = "prop-trf-trace-formal-laws"
kind = "theorem"
title = "Formal laws for the categorical trace"
order = 2647
tags = ["latex:proposition"]
uses = ["def-trf-categorical-trace", "def-trf-coefficient-conventions", "def-weil-algebraically-closed-coefficients", "def-weil-derived-tensor", "def-weil-finite-coefficient-point", "def-weil-finite-field-fiber", "def-weil-rationalization-karoubi", "lem-trf-chain-supertrace"]
+++
Fix the global finite-field datum
and the coefficient
conventions. The categorical
trace has the following properties, all with $A=A_{E,n}$ and
$\Lambda\in\{E,\Qlb\}$ when infinite coefficients occur:

1. *Conjugacy invariance.* If $w:P_1\xrightarrow{\sim}P_2$ is
an isomorphism and $v_2\circ w=w\circ v_1$, then
$\operatorname{tr}_A(v_1\mid P_1)=\operatorname{tr}_A(v_2\mid P_2)$.
1. *Filtered (triangle) additivity.* Let $P'\to P\to P''\to P'[1]$ be a
distinguished triangle in $D^b_{\mathrm{fin}}(A)$ and $(v',v,v'')$ an
endomorphism of it *of filtered origin*: the triangle is the cofibre
sequence of a two-step filtered object $P'\subset P$ with graded pieces
$P'$ and $P''$, and $(v',v,v'')$ is induced by an endomorphism of this
filtered object in the filtered derived category $DF(A)$ (for instance by
a chain endomorphism of a short exact sequence $0\to P'\to P\to P''\to0$
of bounded complexes of finite projective modules, strictly compatible
with the maps). Then
$$
\operatorname{tr}_A(v\mid P)=
\operatorname{tr}_A(v'\mid P')+\operatorname{tr}_A(v''\mid P'').
$$
The filtered origin cannot be dropped: for an endomorphism of a
distinguished triangle in the Verdier derived category whose squares
commute only up to unspecified homotopy, additivity fails (Ferrand's
example, cf. [Stacks, Tag 087J](https://stacks.math.columbia.edu/tag/087J):
over $R=\mathbf Z/4$, the sequence $0\to R[-1]\to[R\xrightarrow{2}R]\to R\to0$
with $(v',v,v'')=(0,(0,2),0)$, where $(0,2)$ is $0$ in degree $0$ and
$2$ in degree $1$, has $\operatorname{tr}_A(v\mid P)=-2\neq0$).
1. *Scalar extension.* For a ring homomorphism
$\rho:A\to B$, $\rho\bigl(\operatorname{tr}_A(v\mid P)\bigr) =\operatorname{tr}_B\bigl(v\otimes_A^LB\mid P\otimes_A^LB\bigr)$.
1. *Supertrace over a field.* For
$\Lambda\in\{E,\Qlb\}$ and $P\in D^b_{\mathrm{fin}}(\Lambda)$,
$$
\operatorname{tr}_\Lambda(v\mid P)=
\sum_{i\in\mathbf Z}(-1)^i\operatorname{Tr}
\bigl(H^i(v)\mid H^i(P)\bigr).
$$
