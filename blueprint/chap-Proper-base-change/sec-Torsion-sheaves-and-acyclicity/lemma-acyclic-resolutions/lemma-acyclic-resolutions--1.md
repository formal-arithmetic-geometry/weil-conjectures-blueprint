+++
id = "lemma-acyclic-resolutions--1"
kind = "lemma"
title = "Quasi-isomorphisms between acyclic complexes"
name_showing = false
order = 346001
aliases = ["bp-r106-1"]
lean = ["CategoryTheory.Functor.quasiIso_map_of_rightAcyclic", "CategoryTheory.Functor.quasiIso_map_of_rightAcyclic_nat"]
uses = []
+++
Let $v:\mathcal A\to\mathcal B$ be a left exact additive functor
between abelian categories, and suppose $\mathcal A$ has injective
resolutions. Let $\varphi:K^\bullet\to L^\bullet$ be a
quasi-isomorphism of $\mathbb Z$-indexed cochain complexes. Suppose
that, for some integer $a$, both complexes vanish in degrees below
$a$, and that every $K^m$ and $L^m$ is $v$-acyclic, meaning that
$R^qv(K^m)=R^qv(L^m)=0$ for every $q>0$. Then

$$
v\varphi:vK^\bullet\longrightarrow vL^\bullet
$$

is a quasi-isomorphism. The same conclusion holds for $\N$-indexed
cochain complexes whose terms are $v$-acyclic.
