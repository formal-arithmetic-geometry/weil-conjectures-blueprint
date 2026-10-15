+++
id = "det-pe-condensed-point-coefficients"
kind = "lemma"
title = "Coefficient sheaves on the geometric point"
uses = ["det-pe-condensed-point-topology", "sk-def-sfb-pullback-from-point", "sk-def-sfb-pulled-back-coefficients", "sk-def-sfb-condensed-ring", "sk-prop-pe-comparison-morphism"]
+++
Let $\Omega$ be separably closed and $X=\Spec\Omega$. For a condensed set or
condensed ring $F$, $(p_X^*F)(\Omega[S])\cong F(S)$ naturally in the profinite set
$S$. In particular:

1. for a topological ring $T$ (for instance profinite or locally profinite),
   $\underline T_X(\Omega[S])=C(S,T)$, the continuous functions;
2. for a discrete ring $A$, $\underline A_X(\Omega[S])=LC(S,A)=\varinjlim_iA^{S_i}$,
   which is $(\nu_X^*A_{X,\Et})(\Omega[S])$; so $\underline A_X$ is the classical
   constant sheaf.
