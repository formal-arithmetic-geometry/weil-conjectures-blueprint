+++
id = "det-nearby-exchange-maps"
kind = "definition"
title = "Exchange maps between nearby cycles and the operations"
order = 3593
uses = ["det-sp-nearby-cycles-exchanges", "thm-nagata-compactification"]
+++
Let $S$ be a strictly henselian trait with separably closed residue field, generic point $\eta$ and
geometric generic point $\bar\eta$, let $A$ be a finite commutative $\ell$-primary ring with $\ell$
invertible on $S$, and for a separated finite-type $S$-scheme $X$ write $S_X=R\Psi_{X/S}$ for the
nearby cycles of [det-sp-nearby-cycles-exchanges]. Let $f\colon V\to W$ be a morphism of separated
finite-type $S$-schemes.

1. $\alpha_f\colon f_s^*S_W\to S_Vf_\eta^*$ is the pullback exchange of
   [det-sp-nearby-cycles-exchanges].
1. $\chi_f\colon S_WRf_{\eta*}\to Rf_{s*}S_V$ is the adjoint mate of $\alpha_f$ for
   $f_s^*\dashv Rf_{s*}$ and $f_\eta^*\dashv Rf_{\eta*}$.
1. For an open immersion $h\colon V\hookrightarrow\overline V$,
   $\nu_h\colon h_{s!}S_VM\to S_{\overline V}h_{\eta!}M$ is the map whose adjoint for
   $h_{s!}\dashv h_s^*$ is
   $S_VM=S_Vh_\eta^*h_{\eta!}M\xrightarrow{\alpha_h^{-1}}h_s^*S_{\overline V}h_{\eta!}M$
   ($\alpha_h$ is invertible since $h$ is smooth). For general $f$, choose a compactification
   $f=ph$ with $h$ an open immersion and $p$ proper [thm-nagata-compactification], and put
   $\nu_f=\chi_p^{-1}\,Rp_{s*}(\nu_h)\colon Rf_{s!}S_V\to S_WRf_{\eta!}$ under the composition
   identifications; for proper $p$, $\chi_p$ is invertible by the proper exchange.
1. $\beta_f(M)\colon S_Vf_\eta^!M\to f_s^!S_WM$ is the exceptional adjoint of
   $Rf_{s!}S_Vf_\eta^!M\xrightarrow{\nu_f}S_WRf_{\eta!}f_\eta^!M\xrightarrow{S_W\varepsilon_{f_\eta}}S_WM$.
1. $\mu_Y\colon S_YM\dt S_YN\to S_Y(M\dt N)$ is the lax tensor map of $R\bar j_*$, adjoint to the
   tensor product of the two counits $\bar j^*R\bar j_*\to1$, with unit
   $\sigma_Y\colon A_{Y_s}\to S_YA_{Y_\eta}$; and for the structure map $a_Y$,
   $\theta_Y=\beta_{a_Y}(A)\colon S_Y\omega_{Y_\eta}\to\omega_{Y_s}$, using $S_SA=A$.

The map $\nu_f$ does not depend on the chosen compactification, and $\nu_{gf}$ is the composite of
$\nu_g$ and $\nu_f$ under the composition identifications.
