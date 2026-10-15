+++
kind  = "proof"
of    = "sk-thm-sfb-rationalization-comparison"
uses = ["det-prop-sfb-qlbar-colimit-x-invert-ell"]
+++
Inverting $\ell$ is exact, so $E_X$ is flat over $\cO_{E,X}$
([det-prop-sfb-qlbar-colimit-x-invert-ell]) and $H^q(E_X\otimes K)=H^q(K)[1/\ell]$.
Restriction of scalars is right adjoint to extension of scalars, and the counit is an
isomorphism because $\ell$ already acts invertibly on an $E_X$-module. So restriction is
fully faithful, and extension of scalars is the localization at its kernel. The details of
this argument are [det-thm-sfb-rationalization-comparison-verdier].

For the bounded constructible complement: the map $\varphi\colon\cO_{E,X}\to E_X$ is
[def-sfb-integers-to-subfield], built from the inclusion on the point
[def-sfb-integers-to-subfield-point]. Extension of scalars preserves bounded constructible
complexes [lem-sfb-extend-scalars-bounded-constructible], and the restricted functor is
[def-sfb-bounded-constructible-extend-scalars]. For topologically Noetherian $X$, the
category $\Dbc(X,\cO_E)$ is triangulated and $\mathbf Z$-linear
[sk-def-sfb-bounded-constructible], so its rationalization at the powers of $\ell$ is
defined [sk-def-sfb-rationalization]. The localization property is
[thm-sfb-extend-scalars-localization], and the equivalence follows from it by the
uniqueness of localizations [def-sfb-rationalization-equivalence].
