+++
id = "prose-05-31"
kind = "hidden"
title = "Construction of $Rf_!$ (5)"
order = 515
+++
To make $Rf_!$ functorial in $f$, and for the base change
theorems later on, we need composition and base change isomorphisms. The
base change map is defined as follows. Let $f:X\to Y$ be separated of
finite type with compactification $f=p\circ j$, let $v:Y'\to Y$ be a
morphism, and let $f':X'\to Y'$, $u:X'\to X$, $p':\overline X'\to Y'$,
$j':X'\to\overline X'$ and $v':\overline X'\to\overline X$ be the base
changes, so that $f'=p'\circ j'$ is a compactification. For
$K\in D(X_{\mathrm{pro}\acute{e}t},\Lambda)$, the isomorphism
$j'^*v'^*j_!K\simeq u^*j^*j_!K=u^*K$ corresponds under $j'_!\dashv j'^*$ to
a map $j'_!u^*K\to v'^*j_!K$. This map is an isomorphism: it is the identity
on the open $X'$, and both sides vanish on the closed complement
$v'^{-1}(\overline X\setminus X)=\overline X'\setminus X'$ [Stacks, [09AH](https://stacks.math.columbia.edu/tag/09AH)]. The
base change map for $Rf_!$ is the composite

$$
v^*Rp_*j_!K\longrightarrow Rp'_*v'^*j_!K\simeq Rp'_*j'_!u^*K
\tag{5.8}
$$

of the base change map (4.5) for $p$ and $Rp'_*$ of the
inverse of this isomorphism.
