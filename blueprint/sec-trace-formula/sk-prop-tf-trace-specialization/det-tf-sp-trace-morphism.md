+++
id = "det-tf-sp-trace-morphism"
kind = "lemma"
title = "Nearby cycles of the trace morphism"
order = 3585
uses = ["det-tf-sp-universal-kernel", "det-tf-sp-kernel-pullback", "def-trf-trace-class", "prop-trf-fixed-square-cartesian"]
+++
In the setting of [det-tf-sp-kernel-pullback], let $F=F_c$ be the fixed scheme with
$r:F\hookrightarrow C$ and $d:F\to X$, let $B:c^!R\Delta_*\xrightarrow{\sim} Rr_*d^!$ be
exceptional proper base change for the fixed square ([prop-trf-fixed-square-cartesian]),
and let $t_{c,K}=B\,c^!e_K:c^!P_X\to Rr_*\omega_F$ be the trace morphism. Then

$$
 t_{c_s,K'}\,c_s^!\rho\,\beta_c
   =Rr_{s*}\theta_F\,\chi_r\,S_C(t_{c_\eta,K}),
$$

and the units satisfy
$\chi_rS_C(\eta_{r_\eta})\sigma_C=Rr_{s*}(\sigma_F)\eta_{r_s}$. Consequently the trace
classes ([def-trf-trace-class]) satisfy
$\operatorname{Tr}_{c_s}(u_s)=\theta_FS_F(\operatorname{Tr}_{c_\eta}(u))\sigma_F$.
