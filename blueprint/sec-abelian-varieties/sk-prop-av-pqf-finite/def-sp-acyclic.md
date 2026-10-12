+++
id = "def-sp-acyclic"
kind = "definition"
title = "Acyclic objects for a left exact functor"
order = 509
uses = ["def-sp-left-exact-additive"]
+++
Let $v:\mathcal A\to\mathcal B$ be a left exact additive
[def-sp-left-exact-additive] functor. An object $X\in\mathcal A$ is
$v$-*acyclic* if $R^nv(X)=0$ for every $n>0$, where $R^nv$ is the right
derived functor [def-sp-left-exact-additive] of $v$.

For example, for the direct image $v=f_*$ of étale sheaves along a morphism
$f$, an object $X$ is $f_*$-acyclic if and only if $R^qf_*(X)=0$ for $q>0$.
