+++
id = "proposition-kummer-duality-integral-tate-module--3"
kind = "proposition"
title = "Transport of the torsor pairing"
name_showing = false
order = 1094003
aliases = ["bp-r335-3"]
lean = ["AlgebraicGeometry.Scheme.EtaleTorsor.picPairing_transport"]
uses = ["proposition-kummer-duality-integral-tate-module--1", "proposition-smooth-proper-curves-torsion-prime"]
+++
The matrix assertion is bypassed by Lean; the Frobenius calculation uses
the following transport identity at finite level.

Let $X$ be a smooth proper curve over an algebraically closed field $k$,
let $f:X\to X$ be an automorphism lying over an automorphism
$\sigma:\operatorname{Spec}k\to\operatorname{Spec}k$, and let $m\geq1$
be invertible in $k$. For a finite étale $\mathbf Z/m$-torsor $t$ put

$$
P_t(y)=\operatorname{Tr}\bigl(t\mathbin{\cup}K_m^{-1}(y)\bigr),
\qquad y\in\operatorname{Pic}(X)[m],
$$

where $K_m$ is the Kummer isomorphism of
[proposition-kummer-duality-integral-tate-module--1] and the trace
$H^2(X,\mu_m)\to\mathbf Z/m$ sends the Kummer class of a line bundle to
its degree modulo $m$.

Suppose that $t$ and $t'$ have structure maps $\pi:P\to X$ and
$\pi':P'\to X$, and that $h:P\to P'$ satisfies
$\pi'\circ h=f\circ\pi$ and commutes with translation by
$1\in\mathbf Z/m$. Then

$$
P_{t'}(y)=P_t(f^*y).
$$

In particular, taking $t'=f_*t$ and $h=\operatorname{id}_P$ gives the
transport formula used for geometric Galois Frobenius.
