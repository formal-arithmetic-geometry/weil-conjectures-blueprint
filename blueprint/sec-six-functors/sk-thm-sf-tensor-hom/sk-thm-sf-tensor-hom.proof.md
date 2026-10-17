+++
kind  = "proof"
of    = "sk-thm-sf-tensor-hom"
uses = ["sk-prop-sf-comparison", "sk-rem-sf-pf-done", "sk-thm-sf-pf-adic", "sk-thm-sf-pf-field", "sk-thm-sf-pf-finite", "sk-thm-sf-pf-proetale"]
+++
The first formula is checked by the Yoneda lemma, localizing the
exceptional adjunction. For $N\in D(Y_{\mathrm{pro\acute et}},\Lambda)$,

$$
 \Hom_Y(N,\cHom_Y(Rf_!K,L))
 =\Hom_Y(N\otimes^{\mathbf L}Rf_!K,L)
 =\Hom_X(f^*N\otimes^{\mathbf L}K,f^!L),
$$

by the projection formula and $Rf_!\dashv f^!$. Tensor–Hom
adjunction and $f^*\dashv Rf_*$ give the first formula. Taking
$L=\omega_Y$ and using composition
$f^!\omega_Y=\omega_X$ gives the second. The same calculation,
with the tensor factor on $X$, gives
$f^!\cHom_Y(L,\omega_Y)\simeq
\cHom_X(f^*L,f^!\omega_Y)$, which is the third formula.

Every map used is an adjunction map. For proper $f$, the pairing
whose adjoint is the exchange is

$$
 Rf_*K\otimes^{\mathbf L}Rf_*\mathbb D_XK
 \longrightarrow Rf_*(K\otimes^{\mathbf L}\mathbb D_XK)
 \longrightarrow Rf_*\omega_X\longrightarrow\omega_Y.
$$

Transposing evaluation twice in this pairing identifies
$Rf_*\delta_K$ with $\delta_{Rf_*K}$. This
proves the last assertion.

*Complement.* For every $N$ the adjunctions and the tensor–internal-Hom
adjunction give a chain

$$
\begin{aligned}
\operatorname{Hom}_Y\bigl(N,\cHom_Y(Rf_!K,L)\bigr)
&\cong\operatorname{Hom}_Y(Rf_!K\otimes^LN,L)\\
&\cong\operatorname{Hom}_Y\bigl(Rf_!(K\otimes^LLf^*N),L\bigr)\\
&\cong\operatorname{Hom}_X\bigl(K\otimes^LLf^*N,f^!L\bigr)\\
&\cong\operatorname{Hom}_X\bigl(Lf^*N,\cHom_X(K,f^!L)\bigr)\\
&\cong\operatorname{Hom}_Y\bigl(N,Rf_*\cHom_X(K,f^!L)\bigr),
\end{aligned}
$$

in which the second isomorphism is the *inverse* of the projection
formula at the coefficient stage of $\Lambda$ — [sk-thm-sf-pf-finite] at
$\Lambda=A_{E,n}$, and [sk-thm-sf-pf-adic], [sk-thm-sf-pf-field],
[sk-thm-sf-pf-proetale] at the remaining stages, all stated in the ambient
$D^+$ and collected in [sk-rem-sf-pf-done] — and the third is the adjunction
$Rf_!\dashv Rf^!$ of [thm-sf-ambient-adjoint-class], valid because
$K\otimes^LLf^*N$ is bounded below of étale origin when $N$ is. The chain
is natural in $N$ ranging over the bounded-below complexes of étale origin,
a full subcategory containing both sides (each is the comparison image of the
corresponding complex on the étale site, [sk-prop-sf-comparison]), so
the two objects represent the same functor there and Yoneda gives the
isomorphism (1), in the ambient category $D^+(Y,\Lambda)$. Its naturality in
$K$ and $L$ and its compatibilities with finite reduction, scalar extension
and shifts are those of the ingredients.
