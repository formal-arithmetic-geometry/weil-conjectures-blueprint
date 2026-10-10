+++
kind  = "proof"
of    = "lem-trf-frobenius-operator-compact-description"
+++
By [def-trf-frobenius-operators] the operator $F_{c,K}^{\,m}$ is
the composite of the canonical direct-image identification of
[def-weil-derived-direct-image] with the compact-support global
geometric Frobenius action of
[def-weil-global-geometric-frobenius] applied to
$\varphi^{[m]}$ of [def-trf-iterated-weil-map]. That action
transports the pair $(g_\gamma^m,Lg_\gamma^{m*}\varphi^{[m]})$ along
the compact-support base-change identification for the finite
automorphism $g_\gamma^m$: on the coefficient complex the transport
is $R\Gamma_c(X,\varphi^{[m]})$ by
[def-trf-coefficient-conventions], and on the scheme variable it is
the base-change isomorphism $g_{\gamma,c}^{m,*}$. The comparison
between the scheme Frobenius and the geometric Frobenius that underlies
this transport is [prop-trf-scheme-galois-comparison], whose input
is the invariance of the site under the universal homeomorphism
$\Phi^m$ between them, [thm-weil-pbc-universal-homeomorphism-invariance];
no further choice enters. The composite is therefore the displayed
one.
