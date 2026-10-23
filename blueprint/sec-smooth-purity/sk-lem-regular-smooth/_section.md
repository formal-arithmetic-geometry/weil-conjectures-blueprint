+++
id = "sk-lem-regular-smooth"
kind = "lemma"
title = "A regular immersion of smooth schemes over a perfect field"
order = 3268
uses = ["sk-def-purity-conv"]
lean = ["AlgebraicGeometry.IsRegularImmersion.smooth_comp", "AlgebraicGeometry.IsRegularImmersion.ringKrullDim_stalk_add"]
tags = ["sketch"]
+++
Let $i:Z\hookrightarrow X$ be a regular closed immersion of pure codimension
$c$, with $X$ smooth over the perfect field $k$ and $Z$ regular and locally
of finite type over $k$. Then both structure morphisms $a_X:X\to\Spec k$ and
$a_Z=a_X\circ i:Z\to\Spec k$ are smooth, and for every point $z\in Z$
$$\dim\mathcal O_{X,i(z)}=\dim\mathcal O_{Z,z}+c.$$
