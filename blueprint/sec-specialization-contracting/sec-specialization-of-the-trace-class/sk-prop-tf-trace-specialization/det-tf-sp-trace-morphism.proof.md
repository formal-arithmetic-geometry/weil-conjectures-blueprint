+++
kind = "proof"
of = "det-tf-sp-trace-morphism"
uses = ["det-tf-sp-universal-kernel", "det-tf-sp-kernel-pullback", "def-trf-trace-class", "prop-trf-fixed-square-cartesian"]
+++
Apply $c_s^!$ to the second equality of [det-tf-sp-universal-kernel],
$e_{K'}\rho=R\Delta_{s*}\theta_X\,\chi_\Delta\,S(e_K)$, and compose with $B_s$. The
fixed-square identity

$$
 Rr_{s*}\beta_d\,\chi_r\,S_C(B_\eta)
    =B_s\,c_s^!(\chi_\Delta)\,\beta_c(R\Delta_{\eta*})
$$

moves $\beta_c$ and $\chi_\Delta$ past $B$, and the composition law
$\theta_F=d_s^!\theta_X\,\beta_d(\omega_{X_\eta})$ combines $\beta_d$ with $\theta_X$. This
gives the first identity.

The unit identity has ordinary adjoint $\sigma_F=\alpha_rr_s^*\sigma_C$, the unit
composition law, followed by the ordinary triangle identity.

For the trace classes, apply the first identity to the section
$k_{u_s}=c_s^!\rho\,\beta_c\,S_C(k_u)\,\sigma_C$ of [det-tf-sp-kernel-pullback]. This gives
$t_{c_s,K'}k_{u_s}=Rr_{s*}\theta_F\,\chi_r\,S_C(t_{c_\eta,K}k_u)\,\sigma_C$. Take
$r_s^*\dashv Rr_{s*}$-adjoints: the trace class on the left is the adjoint of
$t_{c_s,K'}k_{u_s}$, and by the unit identity the adjoint of the right side is
$\theta_FS_F(\operatorname{Tr}_{c_\eta}(u))\sigma_F$. Only the closed immersions $\Delta$
and $r$ are used as proper maps, so $F$ may be singular and nonreduced.
