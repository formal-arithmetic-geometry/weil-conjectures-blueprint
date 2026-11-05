+++
id = "lemma-weight-bounds-partitions--1"
kind = "lemma"
title = "Weight bounds and partitions (1)"
name_showing = false
order = 1352002
aliases = ["bp-r418-1"]
lean = ["AlgebraicGeometry.HasDirectImageWeightBound.of_openClosed"]
uses = ["definition-weil-structure", "definition-weights", "proposition-construction-independence-rf-shriek"]
+++
Let $f:X_0\to Y_0$ be a separated morphism of finite type over $k_0$,
where $Y_0$ is quasi-separated and of finite type over $k_0$. Let
$j:U_0\to X_0$ be a quasi-compact open immersion with closed
complement $i:Z_0\to X_0$.

Suppose that for every $v\in\mathbf R$ and every constructible Weil
sheaf $G$ on $U_0$, respectively on $Z_0$, mixed of weights at most
$v$, the sheaves $R^q(fj)_!G$, respectively $R^q(fi)_!G$, are mixed
of weights at most $v+q$ for all $q\geq0$. Then, for every
$w\in\mathbf R$ and every constructible Weil sheaf $K$ on $X_0$
mixed of weights at most $w$, the sheaf $R^qf_!K$ is mixed of
weights at most $w+q$ for all $q\geq0$.

This is the formulation used by Lean: the direct-image weight bound
is a property of a morphism, quantified over all sheaves and weights.
