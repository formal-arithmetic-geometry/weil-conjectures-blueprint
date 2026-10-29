+++
id = "sk-prop-normal-form"
kind = "proposition"
title = "Étale-local normal form and slicing"
order = 2192
uses = ["sk-def-smooth"]
lean = ["AlgebraicGeometry.Smooth.exists_etale_to_affineSpace", "AlgebraicGeometry.exists_etaleCover_factorization"]
tags = ["sketch"]
+++
Let $g:X\to Y$ be smooth of relative dimension $d$ and let $x\in X$.
Then, after replacing $X$ and $Y$ by affine open neighbourhoods of $x$
and $g(x)$,
$g$ factors as

$$
X\ \xrightarrow{\ e\ }\ \Aaf^d_Y\ \xrightarrow{\ p_d\ }\ Y
$$

with $e$ étale and $p_d$ the projection. Moreover, for any
$f:X\to S$ that is flat, locally of finite presentation and with
geometrically reduced fibres (for instance $f$ smooth) there is an étale covering $\{U_i\to X\}_{i\in I}$ such
that each $U_i\to S$ factors as

$$
U_i\longrightarrow V_i\longrightarrow S
$$

with $V_i\to S$ étale and $U_i\to V_i$ flat, locally of finite
presentation and affine, with geometrically connected fibres and a
section.
