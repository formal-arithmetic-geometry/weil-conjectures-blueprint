+++
kind = "proof"
of = "det-tf-sp-kernel-pullback"
uses = ["det-tf-sp-universal-kernel", "thm-trf-verdier-duality"]
+++
Take tensor–Hom adjoints of both sides. Factor the ordinary comparison through
$c_2=p_2c$, using the composition law $\alpha_{p_2c}=\alpha_c(p_{2\eta}^*)c_s^*\alpha_{p_2}$,
and the exceptional comparison through $c_1=p_1c$, using
$\beta_{p_1c}=c_s^!\beta_{p_1}\,\beta_c(p_{1\eta}^!)$. The external-duality isomorphism
$\lambda_{c,K}$ is $c^!\lambda_K$ followed by the projection-formula map
$t_c:c^!M\dt c^*N\to c^!(M\dt N)$, and the identity

$$
 \beta_cS_C(t_{c_\eta})\mu_C(1\otimes\alpha_c)=c_s^!\mu\,t_{c_s}(\beta_c\otimes1)
$$

moves $\beta_c$ past it. What remains is the first equality of
[det-tf-sp-universal-kernel] pulled back by $c_s^!$, which proves the displayed identity.

For the section: by definition of $\mathfrak h_c$, the morphism $u_s$ is obtained from
$S_C(u)$ through the mate of $S(\operatorname{ev})\mu$, followed by $\alpha_{c_2}$ and
$\beta_{c_1}$. The identity $\mu(\sigma\otimes1)=1$ identifies the section
$S_C(k_u)\sigma_C$ of $S_Cc_\eta^!P_X$ with the morphism it induces under this mate.
Applying the displayed identity therefore gives
$k_{u_s}=c_s^!\rho\,\beta_c\,S_C(k_u)\,\sigma_C$.
