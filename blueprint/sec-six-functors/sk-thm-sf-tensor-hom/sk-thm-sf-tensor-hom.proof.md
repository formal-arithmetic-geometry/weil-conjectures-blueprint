+++
kind  = "proof"
of    = "sk-thm-sf-tensor-hom"
uses = ["sk-rem-sf-pf-done", "sk-thm-sf-pf-adic", "sk-thm-sf-pf-field", "sk-thm-sf-pf-finite", "sk-thm-sf-pf-proetale"]
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

The projection formula used here holds for every admissible $\Lambda$ on
$D(Y_{\mathrm{pro\acute et}},\Lambda)$: [sk-thm-sf-pf-finite] and
[sk-thm-sf-pf-proetale] for finite $\Lambda$, [sk-thm-sf-pf-adic] and
[sk-thm-sf-pf-field] for $\mathcal O_E$, $E$ and $\Qlb$ ([sk-rem-sf-pf-done]).
The Yoneda argument therefore applies to every admissible condensed
$\Lambda$ directly, with no transport between coefficient rings.
