+++
id = "lemma-local-duality-point-c-u--1"
kind = "lemma"
title = "The Frobenius-equivariant duality isomorphism"
name_showing = false
order = 1291001
aliases = ["bp-r399-1"]
lean = ["AlgebraicGeometry.exists_linearEquiv_dual_stalk_higherDirectImage"]
uses = ["definition-lisse-sheaves", "definition-weil-structure", "definition-tate-twists", "proposition-topos-functoriality"]
+++
Let $k_0$ be a finite field and $\ell$ a prime different from its
characteristic. Let $C_0$ be a smooth separated curve of finite type over
$k_0$, let $j_0:U_0\hookrightarrow C_0$ be a quasi-compact dense open
immersion, and let $F$ be a lisse Weil
$\overline{\mathbf Q}_\ell$-sheaf on $U_0$. Write $j:U\hookrightarrow C$
for its base change to $k=\overline{k_0}$. For a closed point
$s\in C_0\setminus U_0$, take the geometric stalks used to define the local
Frobenius at $s$, and put

$$
V=(j_*F^\vee)_{\bar s},\qquad
W=(R^1j_*F)_{\bar s},\qquad q_s=\#\kappa(s).
$$

There exists a $\overline{\mathbf Q}_\ell$-linear isomorphism
$e:V\xrightarrow{\sim}W^\vee$ such that, for every $a\in V$ and $b\in W$,

$$
e(\operatorname{Frob}_s a)(\operatorname{Frob}_s b)=q_s\,e(a)(b).
$$

Equivalently, there exists a perfect pairing
$V\otimes W\longrightarrow\overline{\mathbf Q}_\ell(-1)$ compatible
with local geometric Frobenius. This assertion gives existence, without
asserting that the pairing is canonical.
