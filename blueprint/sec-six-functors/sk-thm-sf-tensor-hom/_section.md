+++
id = "sk-thm-sf-tensor-hom"
kind = "section"
title = "Tensor–Hom form of the exchange"
order = 2281
uses = ["sk-def-sf-exchanges", "sk-def-sf-operations", "sk-lem-sf-mate"]
+++
*Theorem (sketch).*

Let $f:X\to Y$ carry the ambient datum, $M\in\Dctf(X,\Lambda)$ and
$N\in\Dctf(Y,\Lambda)$. Then there is a canonical isomorphism

$$
Rf_*\RHom_X(M,f^!N)\xrightarrow{\ \sim\ }\RHom_Y(Rf_!M,N),
$$

in the ambient category $D^+(Y,\Lambda)$, natural in $M$ and $N$ and
compatible with finite reduction, scalar extension and shifts.

## Proof

For every $L$ the adjunctions and the tensor–internal-Hom adjunction give a
chain

$$
\begin{aligned}
\operatorname{Hom}_Y\bigl(L,\RHom_Y(Rf_!M,N)\bigr)
&\cong\operatorname{Hom}_Y(Rf_!M\otimes^LL,N)\\
&\cong\operatorname{Hom}_Y\bigl(Rf_!(M\otimes^LLf^*L),N\bigr)\\
&\cong\operatorname{Hom}_X\bigl(M\otimes^LLf^*L,f^!N\bigr)\\
&\cong\operatorname{Hom}_X\bigl(Lf^*L,\RHom_X(M,f^!N)\bigr)\\
&\cong\operatorname{Hom}_Y\bigl(L,Rf_*\RHom_X(M,f^!N)\bigr),
\end{aligned}
$$

in which the second isomorphism is the *inverse* of the projection
formula ([sk-thm-sf-pf-finite] below) and the third is the adjunction
$Rf_!\dashv Rf^!$. The chain is natural in $L$, so the two objects represent
the same functor and Yoneda gives the isomorphism.

Uses: `\Cref{def:sf-exchanges}`, `\Cref{def:sf-operations}`, `\Cref{lem:sf-mate}`, `def:weil-derived-pullback-tensor-hom`
