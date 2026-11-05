+++
kind = "proof"
of = "lemma-internal-adjunction-two-exchange-formulas--3"
order = 830006
+++
For (10.4), note that both $f^!\mathbb D_YL$ and
$\mathbb D_Xf^*L$ lie in $D^b_{\mathrm{ctf}}(X,\Lambda)$. Since tensoring with
$f^*L$ preserves $\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$, we may test on objects $M$
of this category:

$$
\begin{aligned}
\Hom_X(M,f^!\mathbb D_YL)
&\simeq\Hom_Y(Rf_!M,\cHom_Y(L,\omega_Y))\\
&\simeq\Hom_Y(Rf_!M\otimes^{\mathbf L}L,\omega_Y)\\
&\simeq\Hom_X(M\otimes^{\mathbf L}f^*L,f^!\omega_Y)\\
&\simeq\Hom_X(M,\mathbb D_Xf^*L).
\end{aligned}
$$

Again, the bijection is induced by the map defined before the lemma, and by Yoneda
we get (10.4).

*Source:* the proof of Lemma [lemma-internal-adjunction-two-exchange-formulas].
