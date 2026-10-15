+++
id = "sk-lem-proper-heart-bound"
kind = "lemma"
title = "A uniform bound for proper direct image"
order = 1530
uses = ["sk-prop-ind-heart", "sk-lem-proper-heart-continuity"]
tags = ["sketch"]
+++
Let $\Lambda=E$ or $\Qlb$. Let $p\colon X\to Y$ be proper, and let $d$ be an integer bounding the dimensions
of all geometric fibres of $p$ (for instance $d=\dim X$). For $M\in\IndCons(X,\Lambda)$
([sk-prop-ind-heart]),

$$
R^qp_*M=0\quad(q>2d+1),\qquad R^qp_*M\in\IndCons(Y,\Lambda)\quad(q\geq0),
$$

and $R^qp_*\colon\IndCons(X,\Lambda)\to\IndCons(Y,\Lambda)$ preserves arbitrary direct sums.

The proof computes with an integral lattice. Its reductions modulo $\pi_E^n$ satisfy the classical
torsion bound $2d$, and the derived inverse limit over $n$ costs one more degree, whence $2d+1$.
