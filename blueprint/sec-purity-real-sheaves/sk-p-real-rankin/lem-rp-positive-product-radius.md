+++
id = "lem-rp-positive-product-radius"
kind = "lemma"
title = "Positive products and radii of convergence"
order = 3002
uses = ["d-real-series"]
+++
Let $\{f_j(t)\}_{j\in J}$ be a locally finite family of series

$$
f_j(t)=1+\sum_{n\ge1}a_{j,n}t^n\in1+t\mathbf R_{\ge0}[[t]],
$$

meaning that each coefficient of the formal product
$F(t):=\prod_{j\in J}f_j(t)=\sum_{n\ge0}A_nt^n$ receives contributions
from only finitely many factors. If this formal series is the Taylor
series at $0$ of a function holomorphic on $|t|<R$, then every
$f_j$ has radius of convergence at least $R$ (in the sense of [d-real-series]). In particular, if
$f_j=P_j(t)^{-1}$ with $P_j(0)=1$ a polynomial, then $P_j$ has no
zero in $|t|<R$.
