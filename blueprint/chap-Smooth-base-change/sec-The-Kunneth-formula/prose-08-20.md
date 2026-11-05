+++
id = "prose-08-20"
kind = "hidden"
title = "The Künneth formula (3)"
order = 711
+++
The case we prove first is the one in which one factor is an identity. For
$f:X\to Y$, $T$ as in Lemma [lemma-base-change-along-product-projection],
$M\in D^b_{\mathrm{ctf}}(X,A)$ and $Q\in D^b_{\mathrm{ctf}}(T,A)$, with $f_1=f$ and
$f_2=\operatorname{id}_T$, put $h=f\times\operatorname{id}_T$. The
Künneth map is then

$$
\kappa_{M,Q}:Rf_*M\boxtimes Q
\longrightarrow Rh_*(M\boxtimes Q),
\tag{8.4}
$$

the adjoint transpose of
$h^*(Rf_*M\boxtimes Q)=p_X^*f^*Rf_*M\otimes^{\mathbf L} p_T^*Q
\xrightarrow{\varepsilon_f\otimes^{\mathbf L}1}M\boxtimes Q$. For constant $Q$
it is the base change map of
Lemma [lemma-base-change-along-product-projection], and every constructible
$Q$ is built from finite direct images of constant sheaves, which the next
lemma treats.
