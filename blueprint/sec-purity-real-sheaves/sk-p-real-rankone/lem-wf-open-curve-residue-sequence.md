+++
id = "lem-wf-open-curve-residue-sequence"
kind = "lemma"
title = "Finite-level residue sequences on an open curve"
order = 2964
uses = ["def-coefficient-twists-detailed", "def-tw-frobenius-action", "def-weil-frobenius-coefficient-twists", "lem-pur-support-localization-triangle", "lem-sc-point-cartier", "prop-pur-regular-immersion-purity-compatibilities", "thm-pur-regular-immersion-purity"]
+++
Let $C_0/\mathbf F_q$ be a smooth projective geometrically connected
curve, let $D_0\subset C_0$ be a finite reduced closed subscheme, and put
$U_0=C_0-D_0$. After base change to
$\overline{\mathbf F}_q$, write $j:U\hookrightarrow C$ and
$i:D\hookrightarrow C$. Put $A_n=\mathbf Z/\ell^n\mathbf Z$, with
$\ell\ne\operatorname{char}\mathbf F_q$. For every $n\geq1$, there is
a Frobenius-equivariant exact sequence

$$
0\longrightarrow H^1(C,A_n)\xrightarrow{j^*}H^1(U,A_n)
\xrightarrow{\operatorname{res}_n}H^0(D,A_n(-1))
\longrightarrow H^2(C,A_n).
\tag{5.1}
$$

The sequences and their transition maps in $n$ are compatible. There
is $m\geq1$ such that, for $Q=q^m$, $\Phi_Q$ fixes every geometric
point of $D$; on the inverse-limit boundary module

$$
\varprojlim_n H^0(D,A_n(-1))
$$

it acts as multiplication by $Q$, and this module has no
$\Phi_Q$-fixed element. Frobenius and twists are those of
[def-tw-frobenius-action], [def-coefficient-twists-detailed].
