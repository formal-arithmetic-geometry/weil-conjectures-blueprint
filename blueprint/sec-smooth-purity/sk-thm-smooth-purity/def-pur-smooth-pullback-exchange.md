+++
id = "def-pur-smooth-pullback-exchange"
kind = "definition"
title = "Smooth pullback exchange for exceptional inverse image"
order = 2361
uses = ["def-coefficient-twists-detailed", "def-pur-conventions", "def-sbc-smooth-morphisms", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties"]
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
$K\in D^b_{ctf}(Y,\Lambda)$. The *smooth pullback exchange* for the
exceptional inverse image is the isomorphism

$$
\operatorname{Ex}^{!,\mathrm{sm}}_{f,v,K}:
Lu^*Rf^!K\longrightarrow Rf'^!Lv^*K
$$

defined as the typed composite

$$
Lu^*Rf^!K
\xrightarrow{(Lu^*\gamma_{f,K})^{-1}}
Lu^*Lf^*K(d)[2d]
\xrightarrow{\ \sim\ }
Lf'^*Lv^*K(d)[2d]
\xrightarrow{\ \gamma_{f',Lv^*K}\ }
Rf'^!Lv^*K.
$$
