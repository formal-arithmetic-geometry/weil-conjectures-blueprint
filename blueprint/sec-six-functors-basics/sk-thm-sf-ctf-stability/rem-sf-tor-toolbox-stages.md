+++
id = "rem-sf-tor-toolbox-stages"
kind = "remark"
title = "The four kinds of admissible coefficients"
order = 2465
uses = ["def-weil-derived-pullback-tensor-hom", "def-weil-finite-tor-amplitude", "def-weil-finite-torsion-constructibility", "lem-sf-flat-model", "lem-sf-pullback-tor-amplitude", "lem-sf-tensor-ctf", "lem-sf-tor-sheaf-constructible", "lem-weil-pbc-pullback-preserves-bounded-constructible", "thm-dg-finite-type-constructibility", "sk-thm-existence", "sk-def-pe-derived-completion", "sk-prop-integral-criterion", "det-prop-integral-criterion-reductions", "sk-lem-integral-models", "sk-prop-scalar-six", "lem-integral-ctf-equals-bc"]
+++
The statements [lem-sf-flat-model], [lem-sf-tor-sheaf-constructible], [lem-sf-tensor-ctf], [lem-sf-pullback-tor-amplitude]
are formulated at the finite stages $A=A_{E,n}$. At the coefficient rings
$\mathcal O_E$, $E$, $\Qlb$, regarded as condensed rings, with the condensed
categories $D^b_c(-,\Lambda)$, they read as follows.
*Field coefficients:* $D^b_{ctf}(-,\Lambda)=D^b_c(-,\Lambda)$ for
$\Lambda\in\{E,\Qlb\}$, a theorem ([sk-thm-existence],
[lem-integral-ctf-equals-bc]), so the finite-Tor cells there are the
bounded-constructible cells of [lem-sf-tensor-ctf],
[thm-dg-finite-type-constructibility] and
[lem-weil-pbc-pullback-preserves-bounded-constructible].
*Integral coefficients:* also $D^b_{ctf}(-,\mathcal O_E)=D^b_c(-,\mathcal O_E)$
([sk-thm-existence]). An object $K\in D^b_c(Y,\mathcal O_E)$ is derived
$\pi_E$-complete ([sk-def-pe-derived-completion], [sk-prop-integral-criterion]),
and all its reductions $K\otimes^L_{\mathcal O_{E,Y}}(A_{E,j})_Y$ are bounded
constructible with cohomology in one interval independent of $j$
([det-prop-integral-criterion-reductions]). Pullback preserves
$D^b_c(-,\mathcal O_E)$ ([sk-lem-integral-models] (3)) and commutes with these
reductions, $(Lf^*K)\otimes^L_{\mathcal O_{E,X}}(A_{E,j})_X\cong
Lf^*(K\otimes^L_{\mathcal O_{E,Y}}(A_{E,j})_Y)$, because $Lf^*$ is monoidal and
$f^*\mathcal O_{E,Y}\cong\mathcal O_{E,X}$ ([def-weil-derived-pullback-tensor-hom],
[sk-prop-scalar-six]). Hence [lem-sf-pullback-tor-amplitude], applied to the
reductions, gives the integral form of clause (i), with an interval
independent of $j$.
