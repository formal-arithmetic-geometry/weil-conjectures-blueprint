+++
id = "corollary-cup-product-pairing--1"
kind = "corollary"
title = "The cup product pairing (1)"
name_showing = false
order = 871001
aliases = ["bp-r262-1"]
lean = ["AlgebraicGeometry.WeilSheaf.exists_traceCup_isPerfect"]
uses = ["definition-perfect-pairing", "definition-frobenius-operator"]
+++
Let $k_0=\Fq$, let $\ell$ be a prime different from the characteristic
of $k_0$, and let $X_0/k_0$ be smooth, proper and geometrically connected
of pure dimension $d$. Put $X=X_0\times_{k_0}\overline{k}_0$ and
$H^i=H^i(X,\Qbarl)$, with geometric Frobenius $F$.

There is a trace–cup structure $T$ on $H^\bullet$: bilinear products
$H^i\times H^j\to H^{i+j}$, for $i,j\in\Z$, satisfying

$$
Fa\cup Fb=F(a\cup b),\qquad
b\cup a=(-1)^{ij}a\cup b,
$$

and a linear trace $\operatorname{tr}:H^{2d}\to\Qbarl$ satisfying
$\operatorname{tr}(Fz)=q^d\operatorname{tr}(z)$, such that the trace is
an isomorphism and, for every $i+j=2d$, the pairing

$$
\langle a,b\rangle=\operatorname{tr}(a\cup b),\qquad
H^i\times H^j\longrightarrow\Qbarl(-d),
$$

is perfect. Here $\Qbarl(-d)$ denotes the value line on which
geometric Frobenius acts by $q^d$.
