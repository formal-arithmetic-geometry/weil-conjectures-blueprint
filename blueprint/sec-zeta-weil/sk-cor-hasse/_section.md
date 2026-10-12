+++
id = "sk-cor-hasse"
kind = "corollary"
title = "Hasse–Weil bound"
order = 3217
lean = ["AlgebraicGeometry.Scheme.Hom.abs_pointCount_one_sub_le"]
uses = ["sk-thm-rh", "sk-thm-trace-transport"]
tags = ["sketch"]
+++
Let $k_0$ be a finite field with $q$ elements, let $X_0$ be a scheme over
$k_0$, let $d\ge1$, and let $P_0,\dots,P_{2d}\in\Z[T]$ satisfy:

* $P_i(0)=1$ for all $i$, $P_0=1-T$, $P_{2d}=1-q^{d}T$, and
$Z(X_0,T)\prod_{i\ \text{even}}P_i(T)=\prod_{i\ \text{odd}}P_i(T)$ in $\Q[[T]]$;
* every complex root $z$ of $P_i$ satisfies $|z|=q^{-i/2}$, for every
$0\le i\le2d$.

Then, with $N_1(X_0)=\#X_0(k_0)$,

$$
\bigl|N_1(X_0)-(q^{d}+1)\bigr|\;\le\;\sum_{i=1}^{2d-1}b_i\,q^{i/2},
\qquad b_i=\deg P_i .
$$
