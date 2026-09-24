+++
id = "prop-trf-external-hom"
kind = "theorem"
title = "External Hom; the $\\beta$ map"
order = 3857
tags = ["latex:proposition"]
uses = ["def-trf-admissibility", "lem-trf-ordinary-kunneth", "prop-trf-exceptional-kunneth"]
+++
For $i=1,2$, let $E_i\in D^b_{ctf}(X_i,A)$ and $L_i\in D^b_{ctf}(X_i,A)$ on separated finite-type $X_i$, with the
admissibility of [def-trf-admissibility] where $!$-pullbacks
occur. The evaluation-defined comparison

$$
\beta:\RHom_A(E_1,L_1)\boxtimes_A^{\mathrm L}\RHom_A(E_2,L_2)
\longrightarrow
\RHom_A\bigl(E_1\boxtimes_A^{\mathrm L}E_2,\,
L_1\boxtimes_A^{\mathrm L}L_2\bigr)
$$

is an isomorphism, natural in all four variables.

## Proof

Devissage in both $E_i$ reduces to $E_i=Rh_{i!}A_{U_i}$, where
$h_i=g_ij_i$ with $g_i$ finite and $j_i$ open. The tensor–Hom
adjunction and exceptional adjunction give

$$
\RHom_A(E_i,L_i)\simeq Rh_{i*}h_i^!L_i .
$$

Writing $h=h_1\times h_2$, the comparison becomes

$$
Rh_{1*}h_1^!L_1\boxtimes_A^{\mathrm L}Rh_{2*}h_2^!L_2
\xrightarrow[\text{twice}]{\mathrm{Ku}_*}
Rh_*\bigl(h_1^!L_1\boxtimes_A^{\mathrm L}h_2^!L_2\bigr)
\xrightarrow{Rh_*\alpha}
Rh_*h^!\bigl(L_1\boxtimes_A^{\mathrm L}L_2\bigr),
$$

the first arrow being [lem-trf-ordinary-kunneth] applied in each
factor, and the second the exceptional Kunneth
[prop-trf-exceptional-kunneth]. To identify this composite with the
specified $\beta$, take ordinary and then exceptional adjoints: both
paths become the tensor product of the two evaluation maps after the
projection formula. Hence $\beta$ itself is an isomorphism.

*Recorded in advance* from chapter *The trace formula* of the source.
