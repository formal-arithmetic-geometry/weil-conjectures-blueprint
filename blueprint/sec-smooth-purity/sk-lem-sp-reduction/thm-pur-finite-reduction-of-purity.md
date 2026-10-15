+++
id = "thm-pur-finite-reduction-of-purity"
kind = "theorem"
title = "Finite reduction of purity"
order = 2366
uses = ["cor-pur-affine-space-zero-section-purity", "def-coefficient-twists-detailed", "def-pur-conventions", "def-pur-smooth-purity-map", "def-pur-smooth-trace", "def-sbc-smooth-morphisms", "def-weil-derived-pullback-tensor-hom", "def-weil-derived-tensor", "def-weil-exceptional-inverse-image", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "lem-cbc-proetale-stalk-conservative", "lem-pur-kunneth-supported", "lem-pur-lisse-uniqueness", "lem-sf-flat-model", "lem-sf-reduction-flat-model", "thm-pur-affine-line-orientation", "thm-pur-composition-coherence", "thm-pur-diagonal-dualizing-object", "thm-pur-dnc-invariance", "thm-pur-smooth-base-change-coherence"]
+++
Work in the purity conventions of [def-pur-conventions], let
$m\leq n$, and write $\operatorname{red}_{n,m,T}$ for the finite
reduction functor

$$
K\mapsto K\otimes^L_{A_{E,n}}A_{E,m}:\
D^b_{ctf}(T,A_{E,n})\longrightarrow D^b_{ctf}(T,A_{E,m})
$$

on a $k$-scheme $T$. For a smooth separated $f:X\to Y$ of relative
dimension $d$ and $K\in D^b_{ctf}(Y,A_{E,n})$, the square

$$
\begin{array}{ccc}
\operatorname{red}_{n,m,X}\bigl(Lf^*K(d)[2d]\bigr)
& \xrightarrow{\ \operatorname{red}_{n,m}(\gamma_{f,K})\ }
& \operatorname{red}_{n,m,X}(Rf^!K)\\
\big\downarrow\ \sim
& & \big\downarrow\ \sim\\
Lf^*\operatorname{red}_{n,m,Y}K(d)[2d]
& \xrightarrow{\ \gamma_{f,\operatorname{red}_{n,m}K}\ }
& Rf^!_{A_{E,m}}\operatorname{red}_{n,m,Y}K
\end{array}
$$

commutes, the vertical isomorphisms being the finite-reduction
compatibilities of the six-operations package. The same is true for the
affine orientations of [thm-pur-affine-line-orientation], the smooth
traces of [def-pur-smooth-trace], the composition coherence of
[thm-pur-composition-coherence], and the base-change squares of
[thm-pur-smooth-base-change-coherence].
