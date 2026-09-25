+++
id = "thm-pur-thom-class"
kind = "theorem"
title = "Zero-section purity for a vector bundle"
order = 2082
uses = ["cor-pur-vector-bundle-purity", "def-coefficient-twists-detailed", "def-pur-conventions", "def-pur-vector-bundle-thom-class", "def-pur-vector-bundle-zero-section", "def-weil-exceptional-inverse-image", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
$A=A_{E,n}$, and let $p:E\to Z$ be a
vector bundle of constant
rank $c$ with zero section $z:Z\hookrightarrow E$. There is a
canonical, base-change compatible isomorphism

$$
\operatorname{th}_E:\;\Lambda_Z\xrightarrow{\ \sim\ }
Rz^!\Lambda_E(c)[2c],
$$

i.e. $Rz^!\Lambda_E\cong\Lambda_Z(-c)[-2c]$, compatible with
exterior products. Its generator is the *Thom class* of the zero
section.

## Proof

Identify twists and shifts by [def-coefficient-twists-detailed].
The zero section is a section of the projection $\pi$, so
$\pi\circ z=\operatorname{id}_Z$. The composition law for $(-)^!$ of
[def-weil-exceptional-inverse-image] and [cor-pur-vector-bundle-purity]
give

$$
Rz^!\Lambda_E(c)[2c]
=Rz^!\bigl(R\pi^!\Lambda_Z\bigr)
=R(\pi\circ z)^!\Lambda_Z
=\Lambda_Z,
$$

which is the displayed identification; base change, exterior products,
and the generator are those of [cor-pur-vector-bundle-purity]
(the class being the restriction of the localized top Chern class of
the tautological section, i.e. the vector-bundle Thom class of
[def-pur-vector-bundle-thom-class]).
