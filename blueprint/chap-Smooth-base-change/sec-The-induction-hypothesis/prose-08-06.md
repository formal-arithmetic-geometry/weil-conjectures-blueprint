+++
id = "prose-08-06"
kind = "hidden"
title = "The induction hypothesis"
order = 669
+++
In positive degrees we argue by induction on the degree. This induction
hypothesis has to survive the reductions outlined above: composition of
base changes, étale localization, and replacement of the source and of
the base of the direct image by other schemes. But a statement about the single
square (8.1) does not survive them, so instead we fix an
integer $n$ invertible on $Y$ and use a property of a morphism $g:Y'\to Y$
which concerns all direct images over all $Y$-schemes at once, as in
[Stacks, [0F02](https://stacks.math.columbia.edu/tag/0F02)]. For $r\geq0$, we say that $\mathrm{BC}(g,n,r)$ holds if,
for every scheme $T$ over $Y$, every qcqs morphism
$Z\to T$, every sheaf of $\mathbf Z/n$-modules $M$ on $Z_{\acute{e}t}$, and
every $0\leq i\leq r$, the base change map in degree $i$ for the square with
base change $Y'\times_YT\to T$ and direct image along $Z\to T$ is an
isomorphism. We allow arbitrary schemes $T$ because the reductions below
lead to base schemes, such as the spectrum of a normal domain with
algebraically closed fraction field, that are in general not Noetherian.

The property $\mathrm{BC}(g,n,r)$ may be checked étale locally on $Y$ and
on $Y'$. Moreover, for composable morphisms $g_1$ and $g_2$,
$\mathrm{BC}(g_1,n,r)$ and $\mathrm{BC}(g_2,n,r)$ imply
$\mathrm{BC}(g_2\circ g_1,n,r)$. Both statements rest on two properties of
the base change map in a fixed degree. First, the map is local for
étale coverings of $Y'$ and of $Y$, since restriction to an étale
object is localization of the site. Second, base change maps compose when
two base changes are composed [Stacks, [0EZR](https://stacks.math.columbia.edu/tag/0EZR), [0EZS](https://stacks.math.columbia.edu/tag/0EZS)].

For smooth $g$, étale coordinates [Stacks, [054L](https://stacks.math.columbia.edu/tag/054L)] give, locally on
$Y'$ and $Y$ and with all schemes affine, an étale $Y$-morphism
$Y'\to\mathbf A^d_Y$, where $d$ is the relative dimension of $g$. Composing
it with the projections $\mathbf A^{j}_Y\to\mathbf A^{j-1}_Y$ that forget
the last coordinate, we obtain a factorization

$$
Y'\longrightarrow\mathbf A^{d-1}_Y
\longrightarrow\cdots\longrightarrow\mathbf A^1_Y
\longrightarrow Y
$$

of $g$ in which every displayed arrow is smooth of relative dimension one.
Indeed, the first is an étale map followed by a projection, and the others
are projections. The case $d=0$ is étale localization. Hence, in the
induction on the degree, it suffices to treat affine $Y$ and $Y'$ with $g$
smooth of relative dimension one.

The coefficients reduce to $\mathbf Z/n$-modules. Indeed, a sheaf $F$ as in
Theorem [theorem-smooth-base-change-classical-torsion] is
the filtered union of the subsheaves $F[n]$, ordered by divisibility of
integers invertible on $Y$, and inverse image commutes with this colimit, and
so do higher direct images along qcqs morphisms [Stacks, [09Z1](https://stacks.math.columbia.edu/tag/09Z1)]. It therefore
suffices to treat $\mathbf Z/n$-modules for each such $n$.
