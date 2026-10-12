+++
id = "def-trf-categorical-trace"
kind = "definition"
title = "Perfect complex and its categorical trace"
order = 2164
uses = ["def-trf-coefficient-conventions", "def-weil-derived-tensor", "def-weil-finite-coefficient-point", "def-weil-finite-field-fiber"]
+++
Fix the global finite-field datum
and the coefficient
conventions, with $A=A_{E,n}$, and define
$D^b_{\mathrm{fin}}(A)$ to be the category of *perfect*
$A$-complexes, realized explicitly as the category of bounded
complexes of finitely generated projective $A$-modules.
For $P\in D^b_{\mathrm{fin}}(A)$ put
$P^\vee=R\operatorname{Hom}_A(P,A)$. The coevaluation and evaluation
are

$$
\operatorname{coev}_P:A\longrightarrow P\otimes_A^LP^\vee,\qquad
\operatorname{ev}_P:P^\vee\otimes_A^LP\longrightarrow A,
$$

where $\otimes^L_A$ is the
derived tensor over $A$. For an
endomorphism $v:P\to P$, the *categorical trace* is

$$
\operatorname{tr}_A(v\mid P):=
\operatorname{ev}_P\circ\operatorname{sym}\circ
\bigl(v\otimes_A^L1\bigr)\circ\operatorname{coev}_P
\in\operatorname{End}_{D(A)}(A)\cong A.
$$

Here $\operatorname{End}_{D(A)}(A)\cong A$ sends an endomorphism of
$A$ to its degree-$0$ scalar.
