+++
id = "det-nearby-exceptional-tensor"
kind = "lemma"
title = "The exceptional exchange and the projection formula"
uses = ["det-nearby-exchange-maps"]
+++
In the notation of [det-nearby-exchange-maps], let $f\colon V\to W$ be a morphism of separated
finite-type $S$-schemes, and write $t_f\colon f^!M\dt f^*N\to f^!(M\dt N)$ for the
projection-formula mate of the exceptional counit. Then:

1. $\nu_f$ is compatible with the projection formula: under the projection-formula isomorphisms
   $Rf_{s!}(-)\dt S_WN\simeq Rf_{s!}(-\dt f_s^*S_WN)$ and
   $Rf_{\eta!}(-)\dt N\simeq Rf_{\eta!}(-\dt f_\eta^*N)$, the composite
   $\mu_W(\nu_f\otimes1)$ corresponds to $\nu_f\,Rf_{s!}(\mu_V(1\otimes\alpha_f))$.
1. As maps $S_Vf_\eta^!M\dt f_s^*S_WN\to f_s^!S_W(M\dt N)$,

   $$
   \beta_f\,S_V(t_{f_\eta})\,\mu_V(1\otimes\alpha_f)=f_s^!\mu_W\ t_{f_s}(\beta_f\otimes1).
   $$

1. For $g\colon W\to Z$, $\beta_{gf}=f_s^!\beta_g\ \beta_f(g_\eta^!)$ and
   $\theta_V=f_s^!\theta_W\ \beta_f(\omega_{W_\eta})$.
