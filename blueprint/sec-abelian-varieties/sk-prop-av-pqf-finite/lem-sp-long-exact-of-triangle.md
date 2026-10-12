+++
id = "lem-sp-long-exact-of-triangle"
kind = "lemma"
title = "Long exact sequences of distinguished triangles"
order = 511
uses = ["def-sp-abelian", "def-sp-homological-functor"]
+++
Let $\Phi:\mathcal C\to\mathcal D$ be a homological functor
[def-sp-homological-functor] with $\mathcal D$ abelian
[def-sp-abelian]. For every distinguished triangle $K_1\to K_2\to K_3\to
K_1[1]$ there is a long exact sequence

$$
 \cdots\to\Phi(K_1)\to\Phi(K_2)\to\Phi(K_3)
 \xrightarrow{\ \delta\ }\Phi(K_1[1])\to\cdots
$$

whose connecting map $\delta$ is natural in the triangle.
