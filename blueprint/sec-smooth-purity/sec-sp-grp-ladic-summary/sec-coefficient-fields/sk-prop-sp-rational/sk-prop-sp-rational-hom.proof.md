+++
kind = "proof"
of = "det-sp-rational-localized-hom"
+++
*Essential surjectivity* is the existence of integral models for rational
constructible complexes ([sk-lem-integral-models], (4), with
[sk-thm-sfb-rationalization-comparison]), a consequence of the condensed
definition of $\Dbc(T,E)$.

*Hom groups.* $L_0[1/\ell]$ is the colimit of
$L_0\xrightarrow{\ell}L_0\xrightarrow{\ell}\cdots$, and $\Hom(K_0,-[q])$ commutes
with this sequential colimit (Hom out of an integral constructible complex
commutes with such colimits, by the Ext-continuity lemma for integral
coefficients). The colimit of $\Hom(K_0,L_0[q])\xrightarrow{\ell}\Hom(K_0,L_0[q])\to\cdots$
is $\Hom(K_0,L_0[q])\otimes_{\mathcal O_E}\mathcal O_E[1/\ell]=\Hom(K_0,L_0[q])\otimes_{\mathcal O_E}E$.

*Functors.* Pullback is exact and commutes with colimits, so
$f^*(K_0[1/\ell])=(f^*K_0)[1/\ell]$. For $Rf_!$, with a compactification
$f=\bar f\circ j$: $Rf_{!,\mathcal O_E}M_0=R\bar f_*j_!M_0$ by the
compactification definition of the derived lower shriek
[det-def-sfb-dc-lower-shriek]; $j_!$ commutes with colimits and keeps the
common lower bound of the diagram $M_0\xrightarrow{\ell}M_0\xrightarrow{\ell}\cdots$,
and $R\bar f_*$, for $\bar f$ quasi-compact and quasi-separated, commutes with
filtered colimits of complexes vanishing below one fixed degree
([sk-cor-pe-bounded-continuity]). Hence
$R\bar f_*j_!(M_0[1/\ell])=R\bar f_*j_!(\operatorname{colim}_\ell M_0)\simeq\operatorname{colim}_\ell R\bar f_*j_!M_0=(R\bar f_*j_!M_0)[1/\ell]$
in the ambient derived category; this uses neither constructibility nor a
bound on the cohomological dimension of the base. In the geometric setting of
the last assertion, proper finiteness [sk-thm-sfb-proper-base-change] puts both
sides in $\Dbc(Y,E)$, which gives
$Rf_!(M_0[1/\ell])\simeq(Rf_{!,\mathcal O_E}M_0)[1/\ell]$ there.
