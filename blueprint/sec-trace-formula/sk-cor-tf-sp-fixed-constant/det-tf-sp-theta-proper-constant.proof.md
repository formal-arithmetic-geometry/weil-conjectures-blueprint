+++
kind = "proof"
of = "det-tf-sp-theta-proper-constant"
uses = ["det-sp-constant-family-vanishing"]
+++
For the constant family, $\sigma_B(\omega_B):\omega_B\to S_B\omega_{B_\eta}$ is an
isomorphism by [det-sp-constant-family-vanishing]. Proper exchange $\nu_a$ is compatible
with the specialization units (same lemma), and on the point $\operatorname{Spec}k$ the unit is the
identity, so

$$
 \nu_a\,Ra_!\sigma_B(\omega_B)
       =\sigma_{\operatorname{Spec}k}(Ra_!\omega_B)
       =\operatorname{id}_{Ra_!\omega_B}.
$$

By the definition of $\theta_B=\beta_a(A)$ as an exceptional adjoint, the map
$\theta_B\sigma_B(\omega_B):\omega_B\to\omega_B$ is the exceptional adjoint of
$\varepsilon\circ\nu_a\circ Ra_!\sigma_B(\omega_B)$, which by the display is the counit
$Ra_!\omega_B\to A$. Its exceptional adjoint is $\operatorname{id}_{\omega_B}$.

For a dualizing section $z$, naturality of $\sigma_B$ gives
$S_B(z)\sigma_B(A)=\sigma_B(\omega_B)z$, and therefore
$\theta_BS_B(z)\sigma_B(A)=\theta_B\sigma_B(\omega_B)z=z$.
