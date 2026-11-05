+++
id = "proposition-p-torsion-smooth-proper-curve--2"
kind = "proposition"
title = "$p$-torsion on a smooth proper curve in characteristic $p$ (2)"
name_showing = false
order = 1584002
aliases = ["bp-r494-2"]
lean = ["AlgebraicGeometry.IsCurve.exists_constantZMod_one_frobenius_baseChange_model"]
uses = []
+++
Let $k\subset k'$ be algebraically closed fields of characteristic
$p>0$, and let $C$ be smooth, proper and connected over $k$, of finite
type and dimension at most one. Let $C'$ be a base change of $C$ to
$k'$, with projection $\iota:C'\to C$. Write $A$ for the constant
sheaf $\mathbf F_p$ on $C_{\acute{e}t}$.

There are a finite-dimensional $k$-vector space $V$, Frobenius-linear
maps $\varphi:V\to V$ and
$\varphi':k'\otimes_k V\to k'\otimes_k V$, and additive isomorphisms

$$
e:H^1(C,A)\xrightarrow{\ \sim\ }\ker(\varphi-1),\qquad
e':H^1(C',\iota^*A)\xrightarrow{\ \sim\ }\ker(\varphi'-1),
$$

such that, for $v\in V$ and $x\in H^1(C,A)$,

$$
\varphi'(1\otimes v)=1\otimes\varphi(v),\qquad
e'(\iota^*x)=1\otimes e(x).
$$

Here the kernels are additive groups. This formulation records the
finite-dimensional Frobenius model and its compatibility with pullback.
