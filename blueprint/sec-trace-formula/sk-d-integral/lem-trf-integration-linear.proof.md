+++
kind  = "proof"
of    = "lem-trf-integration-linear"
+++
The integration is the composite
$A\xrightarrow{\eta^*}R\Gamma(\beta,A_\beta) \xrightarrow{R\Gamma(\tau)}R\Gamma(\beta,\omega_{\beta,A}) \xrightarrow{\varepsilon_{a_\beta}}A$ of
[def-trf-integration]. The first arrow is built from the unit of
the adjunction $La_\beta^*\dashv Ra_{\beta*}$ of
[def-weil-derived-direct-image] and the identification
$Ra_{\beta*}\cong Ra_{\beta!}$ of
[def-compact-support-direct-image-detailed]: it does not depend on
$\tau$. The last arrow is $R\Gamma(s,-)$ applied to the counit of
the adjunction $Ra_{\beta!}\dashv Ra_\beta^!$ of
[def-trf-admissibility] at $\omega_{\beta,A}=Ra_\beta^!A_s$ of
[def-trf-dualizing-complex], and $R\Gamma(s,-)$ is an
$A$-linear functor, so this arrow is $A$-linear; it also does not
depend on $\tau$. The middle arrow is $R\Gamma(\beta,-)$ applied
to $\tau$, and $A$-linearity of the compact-support cohomology of
[def-trf-coefficient-conventions] gives
$R\Gamma(\beta,\tau+a\tau')=R\Gamma(\beta,\tau)+aR\Gamma(\beta,\tau')$;
the exceptional inverse image enters only through
$\omega_{\beta,A}=Ra_\beta^!A_s$, by the dualizing-complex
construction of [def-weil-exceptional-inverse-image]. Composing
the three $A$-linear arrows gives the displayed identity.
