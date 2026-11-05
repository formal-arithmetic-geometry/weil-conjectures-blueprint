+++
id = "lemma-largest-punctual-subsheaf--1"
kind = "lemma"
title = "A direct image of a lisse sheaf has no punctual subsheaf"
order = 1245002
aliases = ["bp-r384-1"]
lean = ["AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.eq_zero_of_support_finite"]
uses = ["definition-weil-structure", "definition-lisse-sheaves", "definition-punctual-sheaf", "proposition-topos-functoriality"]
+++
Let $k_0=\Fq$, let $\ell$ be a prime with $\ell\nmid q$, and let
$j:U_0\hookrightarrow\Aone_{k_0}$ be a dense open immersion. Let $M$ be a
lisse Weil $\overline{\mathbf Q}_\ell$-sheaf on $U_0$, and let $G$ be a
punctual Weil $\overline{\mathbf Q}_\ell$-sheaf on $\Aone_{k_0}$. Then
every morphism $G\to j_*M$ is zero. In particular, $j_*M$ has no nonzero
punctual subsheaf; taking $j$ to be the identity gives the assertion for
a lisse Weil sheaf on the whole affine line.
