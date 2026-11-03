+++
id = "thm-pur-localized-top-chern"
kind = "theorem"
title = "Localized top Chern class"
order = 3281
uses = ["cor-pur-affine-space-zero-section-purity", "def-coefficient-twists-detailed", "def-pur-conventions", "def-pur-frame-class", "def-pur-support-cohomology", "def-pur-vector-bundle-zero-section", "def-weil-derived-cohomology-sheaves", "def-weil-derived-tensor", "lem-pur-divisor-class", "lem-pur-frame-independence", "lem-pur-kummer-additivity", "lem-pur-kunneth-supported", "lem-pur-support-localization-triangle", "thm-pur-projective-bundle-formula"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
let $F$ be a rank-$r$ vector bundle on $T$, let $s$ be a regular
section, and write $i:Z(s)\hookrightarrow T$. There is a canonical
morphism

$$
c_r(F,s):i_*\Lambda_{Z(s)}\longrightarrow\Lambda_T(r)[2r]
$$

with the following properties:

1. *(L1)* for $r=1$ it is the localized Kummer class of the
Cartier divisor of $s$ (of [lem-pur-divisor-class]);
1. *(L2)* it commutes with base change whenever the
pulled-back section is still regular, in particular with
arbitrary base change for the tautological section on the total
space of a vector bundle;
1. *(L3)* for a transverse direct sum of sections it is the
cup product of the two localized classes;
1. *(L4)* after forgetting support it is
$(-1)^rc_r(F)=c_r(F^\vee)$; for $r=1$ this is the sign of
[lem-pur-divisor-class](b).

On an open where $F$ is trivial and $s=(s_1,\dots,s_r)$, the class is
$\partial\kappa(s_1)\cup\cdots\cup\partial\kappa(s_r)$, the class of
[def-pur-frame-class] of the frame $s_1,\dots,s_r$.
