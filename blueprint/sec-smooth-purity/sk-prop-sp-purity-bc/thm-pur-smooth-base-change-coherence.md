+++
id = "thm-pur-smooth-base-change-coherence"
kind = "theorem"
title = "Smooth base-change coherence"
order = 2362
uses = ["cor-pur-vector-bundle-purity", "def-coefficient-twists-detailed", "def-exchange-projection", "def-pur-conventions", "def-pur-smooth-purity-map", "def-sbc-smooth-morphisms", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "lem-pur-coprojection", "lem-pur-diagonal-base-change", "lem-pur-smb-extraordinary", "thm-pur-cohomological-smoothness", "thm-pur-diagonal-dualizing-object", "thm-pur-dnc-invariance"]
+++
Work in the purity conventions of [def-pur-conventions], let
$A=A_{E,n}$, and let

$$
\begin{array}{ccc}
X'&\xrightarrow{\ u\ }&X\\
f'\downarrow&&\downarrow f\\
Y'&\xrightarrow{\ v\ }&Y
\end{array}
$$

be a Cartesian square with $f$ smooth of relative dimension $d$ and
$K\in D^b_{ctf}(Y,\Lambda)$. The square

$$
\begin{array}{ccc}
Lu^*Lf^*K(d)[2d]
& \xrightarrow{\ Lu^*\gamma_{f,K}\ }
& Lu^*Rf^!K\\
\big\downarrow\ \sim
& & \big\downarrow\ \operatorname{Ex}^{!,\mathrm{sm}}_{f,v,K}\\
Lf'^*Lv^*K(d)[2d]
& \xrightarrow{\ \gamma_{f',Lv^*K}\ }
& Rf'^!Lv^*K
\end{array}
$$

commutes, i.e. the pullback of the purity isomorphism is the purity
isomorphism of the base change.
