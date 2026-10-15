+++
id = "det-prop-sfb-qlbar-colimit-x-pullback"
kind = "lemma"
title = "The coefficient comparisons commute with inverse image"
uses = ["det-prop-sfb-qlbar-colimit-x-integral-limit", "det-prop-sfb-qlbar-colimit-x-invert-ell", "sk-def-sfb-pullback-from-point-comp", "sk-prop-sfb-cartesian-coefficients"]
+++
Let $f\colon X\to Y$ be a morphism of schemes and let
$\alpha_f\colon f^{-1}\Lambda_Y\xrightarrow{\sim}\Lambda_X$ be the canonical isomorphism
induced by $p_Y\circ f=p_X$ ([sk-def-sfb-pullback-from-point-comp]), for
$\Lambda=\underline{\cO_E},\underline E,\underline{\Qlb}$. Then, under $\alpha_f$ and the
canonical isomorphisms $f^{-1}(T_Y)\cong T_X$ for constant sheaves:

1. $f^{-1}$ of the isomorphism $\cO_{E,Y}\cong\varprojlim_n(\cO_E/\pi_E^n)_Y$ is the
   isomorphism $\cO_{E,X}\cong\varprojlim_n(\cO_E/\pi_E^n)_X$
   ([det-prop-sfb-qlbar-colimit-x-integral-limit]); in particular $f^{-1}$ carries the
   limit $\varprojlim_n(\cO_E/\pi_E^n)_Y$ to $\varprojlim_n(\cO_E/\pi_E^n)_X$;
2. $f^{-1}$ of $E_Y\cong\cO_{E,Y}[1/\ell]$ is $E_X\cong\cO_{E,X}[1/\ell]$
   ([det-prop-sfb-qlbar-colimit-x-invert-ell]);
3. $f^{-1}$ of $\overline{\mathbf Q}_{\ell,Y}\cong\varinjlim_EE_Y$ is
   $\QbarX\cong\varinjlim_EE_X$.
