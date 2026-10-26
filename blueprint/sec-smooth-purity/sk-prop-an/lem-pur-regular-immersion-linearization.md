+++
id = "lem-pur-regular-immersion-linearization"
kind = "lemma"
title = "Etale linearization of a regular immersion"
order = 2915
uses = ["def-pur-conventions", "def-pur-regular-immersion", "def-sbc-smooth-morphisms", "def-weil-scheme-morphism-properties", "lem-sc-smooth-regular", "sbc-thm-etale-local-normal-form"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
let $i:Z\hookrightarrow X$ be a regular
closed immersion of pure codimension $c$, with $X$ smooth over the
perfect field $k$ and $Z$ regular. Then:

1. $Z$ is smooth over $k$
(regularity plus finite type over the perfect field
$k$: the complete local
rings are power-series rings, so the local ring of $Z$ at every point is
regular, and finite type over a perfect field, hence smooth).
1. The pair $(X,Z)$ is etale locally the *linear* pair: for
every $z\in Z$, writing $m$ for the dimension of its smooth component,
there are an etale neighborhood $U\to X$ of $z$, an
etale neighborhood $V\to Z$ of $z$, an etale map
$$
u:U\longrightarrow\mathbf A^{c+m}_k
$$
and an identification $V=u^{-1}(\mathbf A^m_k)$ with
$Z\cap U=V$, $u|_V$ etale, and the ideal of $V$ in $U$ generated
by $x_1,\dots,x_c$.
