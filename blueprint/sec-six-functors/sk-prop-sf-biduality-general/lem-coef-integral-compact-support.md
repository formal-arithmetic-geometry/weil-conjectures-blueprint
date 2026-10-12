+++
id = "lem-coef-integral-compact-support"
kind = "lemma"
title = "Integral compact supports have the prescribed reductions"
order = 2439
uses = ["def-weil-integral-rational-qbar-compact-support", "lem-coef-integral-residue-tor", "lem-coef-normalized-dvr-effectivity", "lem-fix-compact-support-coefficient-change", "lem-sf-etale-direct-image-vanishing", "thm-cbc-finite-level-proetale", "thm-sf-direct-image-tor-amplitude"]
+++
Let $f:X\to Y$ be separated of finite type, with
$\dim X\leq d$. For $K\in D^b_c(X,R)$ with reduction
Tor interval $[a,b]$, the functor defined in
[def-weil-integral-rational-qbar-compact-support] satisfies

$$
Rf_!K\in D^b_c(Y,R),\qquad
(Rf_!K)\otimes_R^L A_n\cong Rf_{!,n}K_n.
$$

One uniform reduction Tor interval is $[a,b+2d]$. These are the
canonical compact-support coefficient comparisons.
