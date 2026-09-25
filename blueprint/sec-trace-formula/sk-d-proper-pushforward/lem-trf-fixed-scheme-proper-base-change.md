+++
id = "lem-trf-fixed-scheme-proper-base-change"
kind = "lemma"
title = "Fixed scheme of a base-changed correspondence"
order = 2450
uses = ["def-trf-coefficient-conventions", "def-trf-correspondence", "def-trf-fixed-scheme", "def-weil-scheme-morphism-properties"]
+++
Fix the coefficient
conventions, $A=A_{E,n}$, let
$c=(c_1,c_2):C\to X\times_sX$ be a
cohomological correspondence with
fixed scheme
$F=\operatorname{Fix}(c)$ of [def-trf-fixed-scheme], and let
$p:C'\to C$ be a proper
morphism with $c'_i=c_i\circ p$ for $i=1,2$. Then there is a canonical
isomorphism

$$
F':=\operatorname{Fix}(c')\xrightarrow{\ \sim\ }p^{-1}F
=F\times_CC',
$$

i.e. the fixed scheme of the base-changed correspondence is the base
change of the fixed scheme along the proper $p$ (with projections
$i_{F'}:F'\to C'$, $d':F'\to X$, and $p_F:F'\to F$ compatible with
$d'=dp_F$).

## Proof

By the fiber-product definition in [def-trf-fixed-scheme],

$$
\begin{aligned}
F'
&=C'\times_{X\times_sX,c\circ p,\Delta_X}X\\
&\cong C'\times_C\bigl(C\times_{X\times_sX,c,\Delta_X}X\bigr)\\
&=C'\times_CF.
\end{aligned}
$$

For a test scheme $T$, both sides parametrize a map $t:T\to C'$
and a map $x:T\to X$ with $cpt=\Delta_Xx$. The displayed
identification and its inverse are induced by this same pair, so they
are natural in $T$. This proves the canonical isomorphism and
$d'=dp_F$. The projection $p_F$ is the base change of the proper
map $p$, hence is proper.
