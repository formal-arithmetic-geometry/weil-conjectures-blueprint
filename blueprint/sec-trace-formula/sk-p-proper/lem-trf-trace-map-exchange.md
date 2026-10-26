+++
id = "lem-trf-trace-map-exchange"
kind = "lemma"
title = "Exchange of the trace maps: evaluation and support"
order = 3473
uses = ["def-exchange-projection", "def-sf-kv-maps", "def-trf-coefficient-pushforward", "def-trf-kernel-pushforward-maps", "fix-lem-exchanges", "fix-prop-adjunctions", "fix-prop-projection-formula", "lem-sf-kunneth-coherence", "lem-sf-mate", "lem-trf-fixed-map-proper", "prop-trf-fixed-square-cartesian", "thm-sf-comp-composition", "thm-sf-kunneth-relative", "thm-trf-dualizing-complex-composition", "thm-trf-fixed-point-base-change"]
+++
Let $(f,g):(C,c)\to(D,b)$ be a proper pushforward diagram of
[def-trf-coefficient-pushforward] (no Cartesian leg square, no properness
over $s$), with the notation and admissibility of
[def-trf-kernel-pushforward-maps]. Then:

1. *(evaluation)* as maps $Rq_*P_X\to R\Delta_{Y*}\omega_Y$,
$$
\delta_{K'}\circ\rho_f=R\Delta_{Y*}\tau_f\circ Rq_*\delta_K ;
$$
1. *(support)* as maps
$Rg_*Ri_{c*}\omega_{F_c}=Ri_{b*}Rh_*\omega_{F_c}\to Rb^!R\Delta_{Y*}\omega_Y$,
$$
Rb^!\bigl(R\Delta_{Y*}\tau_f\bigr)\circ\mathsf E\circ Rg_*\zeta_c
=\zeta_b\circ Ri_{b*}\tau_h ,
$$
where the source identification is $gi_c=i_bh$.

Moreover, for a Cartesian square $(\beta',\alpha',\beta,\alpha)$
($\beta:V\to W$, $\alpha:U\to W$ proper, $V'=V\times_WU$) the exceptional
adjoint of the right-adjoint base-change isomorphism
$R\alpha'_*R\beta'^!\cong R\beta^!R\alpha_*$ (the mate of
$\operatorname{Ex}_!$) is
$R\beta_!R\alpha'_*R\beta'^!\cong R\alpha_!R\beta'_!R\beta'^!
\xrightarrow{\varepsilon}R\alpha_*$, the composition law followed by the
counit of $\beta'$.
