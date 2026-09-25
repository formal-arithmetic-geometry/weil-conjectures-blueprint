+++
id = "cor-pur-tensor-form-of-purity"
kind = "theorem"
title = "Tensor form of purity"
order = 2114
tags = ["latex:corollary"]
uses = ["def-coefficient-twists-detailed", "def-pur-conventions", "def-sbc-smooth-morphisms", "def-weil-derived-pullback-tensor-hom", "def-weil-derived-tensor", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "thm-pur-cohomological-smoothness", "thm-pur-finite-coefficient-smooth-purity"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
$A=A_{E,n}$, let $f:X\to Y$ be smooth of relative dimension $d$, and
let $K\in D^b_{ctf}(Y,\Lambda)$. There are coherent isomorphisms

$$
Rf^!K\cong Lf^*K\otimes^L_{\Lambda_X}Rf^!\Lambda_Y
\cong Lf^*K(d)[2d],
$$

the second being the purity isomorphism of
[thm-pur-finite-coefficient-smooth-purity] with $K=\Lambda_Y$, and
the first following from it by the tensor-compatibility of the purity
isomorphism.

## Proof

By [thm-pur-finite-coefficient-smooth-purity] applied to $K$
and to $\Lambda_Y$, and by the tensor formula
[thm-pur-cohomological-smoothness], the maps

$$
Rf^!K\cong Lf^*K\otimes^L_{\Lambda_X}\omega_f,\qquad
Rf^!\Lambda_Y\cong\omega_f\cong\Lambda_X(d)[2d]
$$

are canonical; composing them with the twist and associativity
isomorphisms of [def-weil-derived-tensor] (the shift factors are
of even degree, so the Koszul signs are $+1$) gives the displayed
coherent isomorphisms, natural in $K$, and compatible with finite
reduction, scalar extension, shifts and the composition law for $R^!$
by the corresponding properties of
[thm-pur-finite-coefficient-smooth-purity] and of the tensor
coherence of [def-weil-derived-pullback-tensor-hom].
