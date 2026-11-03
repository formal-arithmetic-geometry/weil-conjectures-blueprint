+++
kind  = "proof"
of    = "lem-sfb-extend-scalars-bounded-constructible"
uses = ["det-def-sfb-condensed-ring", "sk-def-sfb-constructible", "det-prop-sfb-module-category"]
+++
*$E_X$ is $\cO_{E,X}$ with $\ell$ inverted.* Let $S$ be a profinite set. A continuous map
$S\to E$ has compact, hence bounded, image, so
$C(S,E)=\bigcup_n\ell^{-n}C(S,\cO_E)$. Hence $\underline E$ is the colimit of
$\underline{\cO}_E\xrightarrow{\ell}\underline{\cO}_E\xrightarrow{\ell}\cdots$ as a
$\underline{\cO}_E$-module [det-def-sfb-condensed-ring]. This colimit may be computed
sectionwise: profinite sets are quasi-compact and quasi-separated for the coherent
topology, so the sheaf condition involves only finite limits, which commute with filtered
colimits. Since $p_X^*$ is a left adjoint, it follows that
$E_X=\colim(\cO_{E,X}\xrightarrow{\ell}\cO_{E,X}\xrightarrow{\ell}\cdots)$ as
$\cO_{E,X}$-modules.

*Flatness.* $E_X$ is therefore a filtered colimit of free $\cO_{E,X}$-modules of rank one.
Since $\otimes_{\cO_{E,X}}$ commutes with colimits and filtered colimits are exact in the
Grothendieck abelian category of modules [det-prop-sfb-module-category],
$E_X\otimes_{\cO_{E,X}}-$ is exact. So $L(\operatorname{Ext}_\varphi)=D(\operatorname{Ext}_\varphi)$,
and $H^n(E\otimes^{\mathrm L}_{\cO_E}K)=E_X\otimes_{\cO_{E,X}}H^n(K)$. In particular
boundedness is preserved.

*Constructibility.* Let $M$ be a constructible $\cO_{E,X}$-module
[sk-def-sfb-constructible]. Extension of scalars commutes with restriction along a
morphism $g$, since $g^*$ is strong monoidal. It is right exact and sends free modules to
free modules of the same rank. So it sends a presentation
$(\cO_{E,X}|_U)^m\to(\cO_{E,X}|_U)^n\to M|_U\to0$ on a stratum and a member of a cover to
a presentation of $(E_X\otimes M)|_U$ over $E_X|_U$. Hence $E_X\otimes_{\cO_{E,X}}M$ is
constructible, with the same stratification and covers.
