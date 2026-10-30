+++
kind = "proof"
of = "sk-cor-tf-sp-fixed-constant"
uses = ["sk-lem-tf-sp-constant-family", "sk-lem-tf-nearby-mate-coherences"]
+++
First suppose that $Y$ is proper and $F=Y\times S$. By
Lemma [sk-lem-tf-sp-constant-family], the unit
$\sigma_Y(\omega_Y):\omega_Y\to \Psi_Y\omega_{Y_\eta}$ is an isomorphism.
For the proper structure map $a$ of $Y$, the base change isomorphism for proper maps
and its compatibility with $\sigma$ show that

$$
\nu_a\,Ra_!\sigma_Y(\omega_Y)
=\sigma_{\operatorname{Spec}k}(Ra_!\omega_Y)
=\operatorname{id}_{Ra_!\omega_Y}.
$$

By the defining adjunction (E.6),
$\theta_Y\sigma_Y(\omega_Y)$ is therefore the adjoint of the
counit $Ra_!\omega_Y\to A$, and hence it is
$\operatorname{id}_{\omega_Y}$. By naturality of $\sigma$, it follows
that $\theta_Y\Psi_Y(z)\sigma_Y(A)=z$ for every section $z$ of the
dualizing complex.

For general $Y$, choose a proper compactification
$j:Y\hookrightarrow\overline Y$. Then
$\omega_Y=j^*\omega_{\overline Y}$, and by base change along the open
immersion, the units for the constant families correspond under
restriction. By the composition rule (E.9),
together with $\beta_j=\alpha_j^{-1}$ for the open immersion,
$\theta_Y$ corresponds to $j^*\theta_{\overline Y}$ under the same
identification. Therefore, restricting the identity
$\theta_{\overline Y}\sigma_{\overline Y}(\omega_{\overline Y})=1$,
we get $\theta_Y\sigma_Y(\omega_Y)=1$, and by naturality the
assertion follows again for all sections of the dualizing complex.
Finally, if only $F_{\mathrm{red}}=Y\times S$, we replace $F$ by its
reduction. This does not change $\operatorname{sp}_F$, because by
invariance under nilpotent thickenings of the total family
and of its fibres, the six operations, their units and counits, and
nearby cycles agree with those of the reduction.
