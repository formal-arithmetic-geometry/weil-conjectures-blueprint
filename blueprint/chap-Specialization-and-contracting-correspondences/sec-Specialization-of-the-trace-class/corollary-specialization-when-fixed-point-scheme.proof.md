+++
kind = "proof"
of = "corollary-specialization-when-fixed-point-scheme"
order = 1699
uses = ["lemma-comparison-completed-coefficients", "lemma-naturality-pasting-comparison", "theorem-nagata-s-compactification-theorem", "lemma-nearby-cycles-constant-family", "lemma-composition-exceptional-base-change-maps"]
+++
By naturality it suffices to show that
$\theta_Y\sigma_Y(\omega_Y)$ is the identity of $\omega_Y$. For proper
$Y$ this follows from the adjunction defining $\theta_Y$. We deduce the
case of general $Y$ by a compactification, and the case of nonreduced
$F$ by invariance under nilpotent thickenings.

*Proper $Y$ and $F=Y\times S$.* Here
$\theta_Y\sigma_Y(\omega_Y)=\operatorname{id}_{\omega_Y}$. The unit
$\sigma_Y(\omega_Y):\omega_Y\to \Psi_Y\omega_{Y_\eta}$ is an isomorphism by
Lemma [lemma-nearby-cycles-constant-family]. For the proper
structure map $a$ of $Y$, the base change isomorphism for proper maps and
its compatibility with $\sigma$ give

$$
\nu_a\,Ra_!\sigma_Y(\omega_Y)
=\sigma_{\operatorname{Spec}k}(Ra_!\omega_Y)
=\operatorname{id}_{Ra_!\omega_Y}.
$$

By the defining adjunction (E.6),
$\theta_Y\sigma_Y(\omega_Y)$ is therefore the adjoint of the counit
$Ra_!\omega_Y\to A$, which is $\operatorname{id}_{\omega_Y}$. Naturality of $\sigma$ then gives
$\theta_Y\Psi_Y(z)\sigma_Y(A)=z$ for every section $z$ of the
dualizing complex.

*General $Y$.* Choose a proper compactification
$j:Y\hookrightarrow\overline Y$, so that
$\omega_Y=j^*\omega_{\overline Y}$. We compare the two sides of the identity under
restriction along $j$. The units for the
constant families correspond by base change along the open immersion, and the map $\theta_Y$ corresponds to $j^*\theta_{\overline Y}$ by the composition
rule (E.9) together with
$\beta_j=\alpha_j^{-1}$ for the open immersion. Restricting the identity
$\theta_{\overline Y}\sigma_{\overline Y}(\omega_{\overline Y})=1$
therefore gives $\theta_Y\sigma_Y(\omega_Y)=1$, and by naturality the
assertion follows again for all sections of the dualizing complex.

*Nonreduced $F$.* If only $F_{\mathrm{red}}=Y\times S$, we replace $F$
by its reduction. This does not change $\operatorname{sp}_F$, because
invariance under nilpotent thickenings of the total family
and of its fibres shows that the six operations, their units and counits,
and nearby cycles agree with those of the reduction.
