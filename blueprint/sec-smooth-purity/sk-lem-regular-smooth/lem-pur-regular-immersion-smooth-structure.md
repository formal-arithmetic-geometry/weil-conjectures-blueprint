+++
id = "lem-pur-regular-immersion-smooth-structure"
kind = "lemma"
title = "A regular immersion of smooth schemes over a perfect field"
order = 3269
uses = ["def-pur-conventions", "def-pur-regular-immersion", "def-sbc-smooth-morphisms", "def-weil-scheme-morphism-properties", "lem-sc-smooth-regular"]
lean = ["AlgebraicGeometry.IsRegularImmersion.smooth_comp", "AlgebraicGeometry.IsRegularImmersion.ringKrullDim_stalk_add"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
let $i:Z\hookrightarrow X$ be a
regular closed immersion of pure
codimension $c$, with $X$ smooth over the perfect field $k$ and
$Z$ regular and locally of finite type over $k$. Then both structure morphisms

$$
a_X:X\longrightarrow\operatorname{Spec}k,\qquad
a_Z:Z\longrightarrow\operatorname{Spec}k
$$

are smooth, where $a_Z=a_X\circ i$, and for every point $z\in Z$ the
local rings satisfy

$$
\dim\mathcal O_{X,i(z)}=\dim\mathcal O_{Z,z}+c.
$$
