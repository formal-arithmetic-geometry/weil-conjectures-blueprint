+++
id = "det-prop-sfb-qlbar-colimit-x-integral-limit"
kind = "lemma"
title = "$\\mathcal O_{E,X}$ is the limit of its finite levels"
lean = ["AlgebraicGeometry.ProEtale.sfb_integral_coefficient_limit"]
order = 1246
uses = ["det-def-sfb-pullback-from-point", "det-def-sfb-condensed-ring", "det-def-sfb-pulled-back-coefficients"]
+++
Let $E/\mathbf Q_\ell$ be finite with ring of integers $\cO_E$ and uniformizer $\pi_E$, and
let $X$ be a scheme. For $n\ge1$ let $(\cO_E/\pi_E^n)_X$ be the constant sheaf of rings on
$X_{\mathrm{proét}}$ with value the finite ring $\cO_E/\pi_E^n$, and let
$(\cO_E/\pi_E^{n+1})_X\to(\cO_E/\pi_E^n)_X$ be the reduction maps.

1. For a finite set $T$, the constant sheaf $T_X$ is represented by the $X$-scheme
   $\coprod_TX$. For the profinite set $\cO_E=\varprojlim_n\cO_E/\pi_E^n$ the pro-étale
   $X$-scheme
   $$
   X[\cO_E]=\varprojlim_n\coprod_{\cO_E/\pi_E^n}X
   $$
   of [det-def-sfb-pullback-from-point] represents $\varprojlim_n(\cO_E/\pi_E^n)_X$ (limit
   of sheaves of sets).
2. The underlying sheaf of sets of $\cO_{E,X}=p_X^*\underline{\cO_E}$ is represented by
   $X[\cO_E]$.
3. Consequently there is a canonical isomorphism of sheaves of rings
   $\cO_{E,X}\cong\varprojlim_n(\cO_E/\pi_E^n)_X$, the limit being taken in sheaves of rings
   (equivalently, in sheaves of sets, with the induced ring structure).
