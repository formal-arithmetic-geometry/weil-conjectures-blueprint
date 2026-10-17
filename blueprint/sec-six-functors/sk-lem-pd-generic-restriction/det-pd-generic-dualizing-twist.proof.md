+++
kind = "proof"
of = "det-pd-generic-dualizing-twist"
uses = ["det-pd-generic-closed-hom", "thm-amb-etale-exceptional-adjoint", "cor-amb-affine-space-adjunction", "lem-weil-verdier-preservation-strata", "lem-weil-duality-pairing"]
+++
*The twist.* On an affine open of $X$ choose a closed immersion
$i\colon X\hookrightarrow\mathbf A^r_{\mathbf A^1_k}$ over $\mathbf A^1_k$.
Composition of the exceptional adjoints ([thm-amb-etale-exceptional-adjoint])
and smooth purity for affine space ([cor-amb-affine-space-adjunction]) compute

$$
\omega_X=Ri^!A(r+1)[2r+2],\qquad
\omega_{X_{\bar\eta}}=Ri_{\bar\eta}^!A(r)[2r],
$$

since $\mathbf A^r_{\mathbf A^1_k}=\mathbf A^{r+1}_k$ while
$\mathbf A^r_{\mathbf A^1_k}\times_{\mathbf A^1_k}\bar\eta=\mathbf A^r_{\bar\eta}$.
The closed-support comparison of [det-pd-generic-closed-hom](1), together with
the fact that an invertible constant twist and shift commute with $Ri^!$ by
tensor adjunction, gives $g_X^*\omega_X\simeq\omega_{X_{\bar\eta}}(1)[2]$.
This identification is built from composition and adjunction counits, so it
is compatible with the evaluations defining duality.

*The double dual.* Both $K$ and $D_XK=\cHom_X(K,\omega_X)$ lie in
$D^b_{ctf}(X_{\mathrm{\acute et}},A)$ ([lem-weil-verdier-preservation-strata]),
so the internal-Hom comparison of [det-pd-generic-closed-hom](2) applies to
both. Put $N=A(1)[2]$. The first application gives
$g_X^*D_XK\simeq D_{X_{\bar\eta}}(g_X^*K)\otimes N$. Since
$\cHom(Q\otimes N,\omega\otimes N)\simeq\cHom(Q,\omega)$ for the invertible
object $N$, the second application gives

$$
g_X^*D_XD_XK\simeq D_{X_{\bar\eta}}D_{X_{\bar\eta}}(g_X^*K):
$$

the twist and shift cancel. Both comparisons preserve evaluation, and $\delta$
is the transpose of evaluation ([lem-weil-duality-pairing]); hence this
isomorphism carries $g_X^*\delta_K$ to $\delta_{g_X^*K}$.
