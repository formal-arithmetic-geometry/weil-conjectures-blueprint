+++
id = "cor-pc-dense-points-curves-sections"
kind = "theorem"
title = "Consequences of the density of rational points"
order = 753
tags = ["latex:corollary"]
uses = ["def-pc-curve", "def-pc-separably-closed", "def-pc-smooth-projective-curve", "def-sc-invertible-module", "lem-pc-rational-points-dense"]
lean = ["AlgebraicGeometry.Scheme.Hom.denseRange_baseChangeFieldPoint", "AlgebraicGeometry.Scheme.Hom.exists_baseChangeFieldPoint_notMem_support_zeroLocus", "AlgebraicGeometry.Scheme.Hom.exists_fieldPoints_notMem_support_zeroLocus", "AlgebraicGeometry.Scheme.Hom.infinite_fieldPoints"]
+++
Let $k$ be a separably closed field and let $X$ be a scheme over $k$
which is smooth over $k$.

1. For every field extension $K/k$ put $X_K=X\times_{\operatorname{Spec}k}\operatorname{Spec}K$, and for
$x\in X(k)$ let $x_K=\operatorname{Spec}(K)\times_kx$ be the induced $K$-rational point of
$X_K$. Then the set $\{x_K : x\in X(k)\}$ is Zariski dense in $X_K$ (for $K=k$
this is the density of $X(k)$ in $X$).
1. Let $\mathcal{L}$ be an invertible $\mathcal{O}_{X_K}$-module and
$s\in H^0(X_K,\mathcal{L})$ a section which does not vanish identically, i.e.
$s(y)\neq0$ in $\mathcal{L}(y)=\mathcal{L}_y\otimes\kappa(y)$ for some $y\in X_K$.
Then there is an $x\in X(k)$ such that $s$ does not vanish at $x_K$. More
generally, for a morphism $\varphi:\mathcal M\to\mathcal N$ of invertible
$\mathcal O_{X_K}$-modules whose zero scheme $Z(\varphi)$ (cut out locally by the
coefficient $b$ of $\varphi$ in trivializations, $\varphi(e_{\mathcal M})=b\,e_{\mathcal N}$)
is not all of $X_K$, there is an $x\in X(k)$ with $x_K\notin Z(\varphi)$; a section
$s$ is the case $\varphi=s:\mathcal O_{X_K}\to\mathcal L$.
1. If $X$ is smooth of relative dimension $1$, proper and geometrically integral
over $k$ (for instance a geometrically integral smooth projective curve), then
$X(k)$ is infinite. If $X$ is reduced, then every non-zero morphism
$\varphi:\mathcal M\to\mathcal N$ of invertible $\mathcal{O}_X$-modules, for
instance a non-zero $s\in H^0(X,\mathcal{L})$ for $\mathcal{L}$ invertible, does
not vanish identically, so (2) applies with $K=k$: $\varphi$ does not vanish at
some $x\in X(k)$.

## Proof

(1) Let $p:X_K\to X$ be the projection. It is the base change of
$\operatorname{Spec}K\to\operatorname{Spec}k$ along $X\to\operatorname{Spec}k$, and the structure morphism of any
scheme over a field is universally open (Morphisms of Schemes,
Lemma 29.23.4, Tag [0383](https://stacks.math.columbia.edu/tag/0383));
hence $p$ is open. Let $Z\subseteq X_K$ be a closed subset containing every
$x_K$, and suppose $U:=X_K\setminus Z\neq\emptyset$. Then $p(U)\subseteq X$ is a
nonempty open subset, so by [lem-pc-rational-points-dense] it contains a
point $x\in X(k)$. The fibre of $p$ over $x$ is
$\operatorname{Spec}(\kappa(x)\otimes_kK)=\operatorname{Spec}(k\otimes_kK)=\operatorname{Spec}K$, a single point, namely
$x_K$. Since $x\in p(U)$, some point of $U$ lies over $x$, so $x_K\in U$,
contradicting $x_K\in Z$. Hence $Z=X_K$, which is the asserted density.

(2) The set $W:=\{y\in X_K : s(y)\neq0\}$ is open: on an open
$V=\operatorname{Spec}A\subseteq X_K$ on which $\mathcal{L}$ is free on a generator $e$
([def-sc-invertible-module]) write $s|_V=a\cdot e$ with $a\in A$; then
$s(y)\neq0$ if and only if $a\notin\mathfrak p_y$, so $W\cap V=D(a)$. By
hypothesis $W\neq\emptyset$, so its complement is a closed subset not
containing all of $X_K$; by (1) it misses some $x_K$, i.e. $x_K\in W$. For a
morphism $\varphi:\mathcal M\to\mathcal N$ of invertible modules the same
argument applies to the open complement $W$ of $Z(\varphi)$, which on a
common trivializing open $V=\operatorname{Spec}A$ is $D(b)$.

(3) Since $X$ is geometrically integral over $k$, it is integral, and being
smooth of relative dimension $1$ over $k$ and nonempty it has dimension
one; in particular its generic point $\eta$ is not closed. Every
$x\in X(k)$ is a closed point (its residue field is $k$). If $X(k)$ were
finite, it would be a finite union of closed points, hence a closed subset
of $X$ not containing $\eta$; but $X(k)$ is dense in $X$ by
[lem-pc-rational-points-dense], so its closure is $X\ni\eta$, a
contradiction. Hence $X(k)$ is infinite.
For the last assertion let $X$ be reduced and $\varphi:\mathcal M\to\mathcal N$
a non-zero morphism of invertible modules. If $Z(\varphi)$ were all of $X$
as a set, then on every affine open $V=\operatorname{Spec}A$ trivializing
$\mathcal M$ and $\mathcal N$ the coefficient $b$ of $\varphi$ would lie in
every prime of $A$, hence be nilpotent, hence $0$ as $A$ is reduced; so
$\varphi$ would vanish on a cover, i.e. $\varphi=0$. Thus $Z(\varphi)\neq X$,
and (2) (with $K=k$) gives $x\in X(k)$ with $x\notin Z(\varphi)$. A non-zero
$s\in H^0(X,\mathcal L)$ is the case $\varphi=s:\mathcal O_X\to\mathcal L$.

*Remark on base change.* For a general extension $K/k$ the hypothesis
of (2) holds for every non-zero $s$ as soon as $X_K$ is integral (by the
generic-point argument of (3) applied on $X_K$); for a smooth projective
curve with a rational point this integrality is established later in
the twist-lemma block.
