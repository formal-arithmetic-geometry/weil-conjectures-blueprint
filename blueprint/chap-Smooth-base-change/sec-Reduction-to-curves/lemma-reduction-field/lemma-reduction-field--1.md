+++
id = "lemma-reduction-field--1"
kind = "lemma"
title = "Detection of a fixed-base failure over a field"
name_showing = false
order = 675001
aliases = ["bp-r203-1"]
lean = ["AlgebraicGeometry.Etale.nonempty_fieldFailure"]
uses = ["definition-derived-base-change-map"]
+++
Let $g:Y'\to Y$ be a morphism of schemes, let $\Lambda$ be a commutative
ring, and let $q\in\mathbf Z$ with $q\geq1$. Suppose that, after every base
change of $g$, the base change map is an isomorphism in every degree $i<q$
for every qcqs direct image and every sheaf of $\Lambda$-modules. Suppose
also that there are a qcqs morphism $f:Z\to Y$ and a sheaf $M$ of
$\Lambda$-modules on $Z_{\acute{e}t}$ for which the degree-$q$ base change
map along $g$ is not an isomorphism.

Then there are an affine scheme $T$ over $Y$, a field $\Omega$, a morphism
$h:\operatorname{Spec}\Omega\to T$, and a sheaf $N$ of $\Lambda$-modules on
$(\operatorname{Spec}\Omega)_{\acute{e}t}$ for which

$$
g_T^{-1}R^qh_*N\longrightarrow R^qh'_*g_\Omega^{-1}N
$$

is not an isomorphism. Here $T'=Y'\times_YT$, $g_T:T'\to T$ is the
projection, and $h'$ and $g_\Omega$ are the projections from
$T'\times_T\operatorname{Spec}\Omega$. The degree-$i$ maps are the
degree-$i$ homology of the derived base change map
[definition-derived-base-change-map] applied to sheaves placed in degree
zero.
