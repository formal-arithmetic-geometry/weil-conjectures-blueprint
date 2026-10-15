+++
kind  = "proof"
of    = "sk-thm-sf-tensor-hom"
+++
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
formula at the coefficient stage of $\Lambda$ — [sk-thm-sf-pf-finite] at
$\Lambda=A_{E,n}$, and [sk-thm-sf-pf-adic], [sk-thm-sf-pf-field],
[sk-thm-sf-pf-proetale] at the remaining stages, all stated in the ambient
$D^+$ and collected in [sk-rem-sf-pf-done] — and the third is the adjunction
$Rf_!\dashv Rf^!$ of [thm-sf-ambient-adjoint-class], valid because
$M\otimes^LLf^*L$ is bounded below of étale origin when $L$ is. The chain
is natural in $L$ ranging over the bounded-below complexes of étale origin,
a full subcategory containing both sides (each is the comparison image of the
corresponding complex on the étale site, [sk-prop-sf-comparison]), so
the two objects represent the same functor there and Yoneda gives the
isomorphism.
