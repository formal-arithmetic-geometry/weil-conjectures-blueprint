+++
id = "det-thm-restriction-local"
kind = "lemma"
title = "Local factorization of $f^!$ on an affine chart"
order = 2450
uses = ["sk-lem-sf-mate", "sk-cor-affine-space-rational", "sk-prop-closed-adjoint-constructible"]
+++
Let $\Lambda=E$ or $\Qlb$ and let $f:X\to Y$ be separated of finite type. Let
$v:V\hookrightarrow Y$ be an affine open, $u:U\hookrightarrow X$ an affine
open with $f(U)\subset V$, and $i:U\hookrightarrow\mathbf A^d_V$ a closed
immersion over $V$, with $p:\mathbf A^d_V\to V$ the projection (so that
$f\circ u=v\circ p\circ i$). Then there is an isomorphism of functors
$\Loc(\Dbc(Y,\Lambda))\to\Loc(\Dbc(U,\Lambda))$

$$
u^*f^!\simeq i^!p^!v^*,
$$

and for $K\in\Dbc(Y,\Lambda)$ the object $u^*f^!K$ lies in $\Dbc(U,\Lambda)$.
Such data $(V,U,i)$ exist and finitely many of them cover $X$.
