+++
id = "det-tf-sp-kernel-pullback"
kind = "lemma"
title = "The specialized coefficient as a section of the kernel"
order = 3602
uses = ["det-tf-sp-universal-kernel", "thm-trf-verdier-duality"]
+++
In the setting of [det-tf-sp-universal-kernel], let $c=(c_1,c_2):C\to X\times_SX$ be a
correspondence of separated finite-type $S$-schemes, let
$\lambda_{c,K}:c^!P_X\xrightarrow{\sim}\cHom_A(c_2^*K,c_1^!K)$ be the external-duality
isomorphism on $C$, and let $\mathfrak h_c$ be defined as $\mathfrak h$ with
$\alpha_{c_2}$ and $\beta_{c_1}$ in place of $\alpha_{p_2}$ and $\beta_{p_1}$. Then

$$
 \mathfrak h_cS_C(\lambda_{c_\eta,K})
   =\lambda_{c_s,K'}\,c_s^!\rho\,\beta_c(P_X).
$$

Consequently, if $u:c_{2\eta}^*K\to c_{1\eta}^!K$ corresponds to the section
$k_u:A_{C_\eta}\to c_\eta^!P_X$ and
$u_s=\beta_{c_1}\circ S_C(u)\circ\alpha_{c_2}:c_{2s}^*K'\to c_{1s}^!K'$, then the section
corresponding to $u_s$ is

$$
 k_{u_s}=c_s^!\rho\,\beta_c\,S_C(k_u)\,\sigma_C,
$$

where $\sigma_C:A_{C_s}\to S_CA_{C_\eta}$ is the specialization unit.
