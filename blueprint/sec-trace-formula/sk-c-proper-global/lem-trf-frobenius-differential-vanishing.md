+++
id = "lem-trf-frobenius-differential-vanishing"
kind = "lemma"
title = "The differential of the Frobenius vanishes"
order = 2476
uses = ["def-trf-scheme-frobenius"]
+++
Let $X_0$ be a scheme over $\mathbf F_q$, $q=p^a$, and let
$\Phi_X:X\to X$ be the absolute Frobenius of
[def-trf-scheme-frobenius] on $X=X_0\times_{\mathbf F_q}k$. At
every point $y$ of $X$, the linearization

$$
d\Phi_X^{\,m}:\mathcal O_{X,y}/\mathfrak m_y^2
\longrightarrow\mathcal O_{X,\Phi^m(y)}/\mathfrak m_{\Phi^m(y)}^2
$$

is zero for every $m\ge1$.

## Proof

By [def-trf-scheme-frobenius], the $m$-th iterate of the absolute
Frobenius acts on regular functions by $f\mapsto f^{p^m}$. Its
linearization on the Zariski cotangent space is therefore
$f\bmod\mathfrak m^2\mapsto f^{p^m}\bmod\mathfrak m^2=0$, since
$p^m=0$ in $\mathbf F_q$ and every term of $d(f^{p^m})$ carries the
coefficient $p^m$. Hence $d\Phi^m=0$ at every point.
