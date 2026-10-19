+++
id = "lem-coef-integral-compact-support"
kind = "lemma"
title = "Integral compact supports have the prescribed reductions"
order = 2479
uses = ["sk-def-sf-operations", "sk-def-sfb-module-derived-lower-shriek", "sk-thm-existence", "sk-prop-scalar-six", "sk-prop-integral-criterion", "lem-coef-integral-residue-tor", "lem-fix-compact-support-coefficient-change", "lem-sf-etale-direct-image-vanishing", "thm-cbc-finite-level-proetale", "thm-sf-direct-image-tor-amplitude"]
+++
Let $R=\mathcal O_E$, $A_n=A_{E,n}=\mathcal O_E/\pi_E^n$, and write
$K_n=K\otimes^{\mathbf L}_{R}A_n$. Let $f:X\to Y$ be separated of finite type,
with $\dim X\leq d$, and let $Rf_!=R\bar f_*\circ j_!$ be the compact-support
direct image of $R_X$-modules for a compactification $f=\bar f\circ j$
([sk-def-sf-operations], [sk-def-sfb-module-derived-lower-shriek]). For
$K\in D^b_c(X,R)$ with reduction Tor interval $[a,b]$,

$$
Rf_!K\in D^b_c(Y,R),\qquad
(Rf_!K)\otimes_R^L A_n\cong Rf_{!,n}K_n.
$$

One uniform reduction Tor interval is $[a,b+2d]$. These are the
canonical compact-support coefficient comparisons.
