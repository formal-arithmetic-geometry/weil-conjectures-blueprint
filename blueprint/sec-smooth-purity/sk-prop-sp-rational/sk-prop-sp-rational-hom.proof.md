+++
kind = "proof"
of = "det-sp-rational-localized-hom"
+++
*Essential surjectivity* is the existence of integral models for rational
constructible complexes (Lemma on integral models, item (4), in the
construction of the rational categories).

*Hom groups.* $L_0[1/\ell]$ is the colimit of
$L_0\xrightarrow{\ell}L_0\xrightarrow{\ell}\cdots$, and $\Hom(K_0,-[q])$ commutes
with this sequential colimit (Hom out of an integral constructible complex
commutes with such colimits, by the Ext-continuity lemma for integral
coefficients). The colimit of $\Hom(K_0,L_0[q])\xrightarrow{\ell}\Hom(K_0,L_0[q])\to\cdots$
is $\Hom(K_0,L_0[q])\otimes_{\mathcal O_E}\mathcal O_E[1/\ell]=\Hom(K_0,L_0[q])\otimes_{\mathcal O_E}E$.

*Functors.* Pullback is exact and commutes with colimits, so
$f^*(K_0[1/\ell])=(f^*K_0)[1/\ell]$. For $Rf_!$, with a compactification
$f=\bar f\circ j$: $Rf_{!,\mathcal O_E}M_0=R\bar f_*j_!M_0$ by
[det-sp-integral-direct-image-tower]; $j_!$ commutes with colimits, and $R\bar f_*$
commutes with the colimit along $\ell$ on bounded constructible objects (bounded
continuity of the direct image). Hence
$Rf_!(M_0[1/\ell])=R\bar f_*j_!(\operatorname{colim}_\ell M_0)\simeq\operatorname{colim}_\ell R\bar f_*j_!M_0=(Rf_{!,\mathcal O_E}M_0)[1/\ell]$.
