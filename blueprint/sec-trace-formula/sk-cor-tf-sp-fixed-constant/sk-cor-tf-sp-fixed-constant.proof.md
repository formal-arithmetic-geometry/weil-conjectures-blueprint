+++
kind = "proof"
of = "sk-cor-tf-sp-fixed-constant"
uses = ["sk-lem-tf-sp-constant-family", "sk-lem-tf-nearby-mate-coherences"]
+++
First suppose $B$ proper and $F=B\times S$. By
Lemma [sk-lem-tf-sp-constant-family],
$\sigma_B(\omega_B):\omega_B\xrightarrow{\sim} S_B\omega_{B_\eta}$.
For the proper structure map $a$ of $B$, proper exchange and
compatibility with $\sigma$ give

$$
 \nu_a\,Ra_!\sigma_B(\omega_B)
       =\sigma_{\operatorname{Spec}k}(Ra_!\omega_B)
       =\operatorname{id}_{Ra_!\omega_B}.
$$

By the defining adjunction of $\beta_a$, under which $\beta_a$ is the exceptional adjoint
of $S(\varepsilon_{a_\eta})\circ\nu_a$,
$\theta_B\sigma_B(\omega_B)$ is therefore the adjoint of the
counit $Ra_!\omega_B\to A$, hence is
$\operatorname{id}_{\omega_B}$. Naturality of $\sigma$ now
gives $\theta_BS_B(z)\sigma_B(A)=z$ for every dualizing
section $z$.

For general $B$, choose a proper compactification
$j:B\hookrightarrow\overline B$. Then
$\omega_B=j^*\omega_{\overline B}$, and open base change
identifies the constant-family units by restriction. The composition law
$\theta_V=f_s^!\theta_W\,\beta_f(\omega_{W_\eta})$ of
[sk-lem-tf-nearby-mate-coherences], together with
$\beta_j=\alpha_j^{-1}$ for the open immersion, identifies
$\theta_B$ with $j^*\theta_{\overline B}$ under the same
identification. Restricting the identity
$\theta_{\overline B}\sigma_{\overline B}(\omega_{\overline B})=1$
therefore gives $\theta_B\sigma_B(\omega_B)=1$, and naturality
again gives the assertion for all dualizing sections.
Finally, nilpotent invariance of the total family and of its
fibres identifies the six operations, their units and counits,
and nearby cycles with those of the reduction.
