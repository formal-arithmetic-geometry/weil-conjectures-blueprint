+++
id = "prose-09-06"
kind = "hidden"
title = "Degree zero and reduction to a smooth curve (2)"
order = 401
+++
In positive degrees we argue by induction on the degree, and the
induction hypothesis has to survive the reductions outlined above:
composition of base changes, étale localization, and replacement of
the source and of the base of the direct image by other schemes. A
statement about the single square (9.1) does not survive
them, so we fix an integer $n$ invertible on $Y$ and use the following
property of a morphism $g:Y'\to Y$, as in [Stacks, Tag 0F02](https://stacks.math.columbia.edu/tag/0F02), which concerns
all direct images over all $Y$-schemes at once. For $r\geq0$, we say that $\mathrm{BC}(g,n,r)$ holds if,
for every scheme $T$ over $Y$, every qcqs morphism
$Z\to T$, every sheaf of $\mathbf Z/n$-modules $M$ on $Z_{\acute{e}t}$, and
every $0\leq i\leq r$, the base change map in degree $i$ for the square with
base change $Y'\times_YT\to T$ and direct image along $Z\to T$ is an
isomorphism. We allow arbitrary schemes $T$ because the reductions below
lead to base schemes, such as the spectrum of a normal domain with
algebraically closed fraction field, that are in general not Noetherian.

The base change map is local for étale coverings of $Y'$ and of $Y$,
since restriction to an étale object is localization of the site, and
base change maps compose when two base changes are composed
[Stacks, Tag 0EZR](https://stacks.math.columbia.edu/tag/0EZR), [Stacks, Tag 0EZS](https://stacks.math.columbia.edu/tag/0EZS). Both facts hold in each fixed degree. It follows that
$\mathrm{BC}(g,n,r)$ may be checked étale locally on $Y$ and on $Y'$, and
that for composable morphisms $g_1$ and $g_2$, $\mathrm{BC}(g_1,n,r)$ and $\mathrm{BC}(g_2,n,r)$ imply
$\mathrm{BC}(g_2\circ g_1,n,r)$.

For smooth $g$, étale coordinates [Stacks, Tag 054L](https://stacks.math.columbia.edu/tag/054L) give, locally on
$Y'$ and $Y$ and with all schemes affine, an étale $Y$-morphism
$Y'\to\mathbf A^d_Y$, where $d$ is the relative dimension of $g$. Composing
it with the projections $\mathbf A^{j}_Y\to\mathbf A^{j-1}_Y$ that forget
the last coordinate, we obtain a factorization

$$
Y'\longrightarrow\mathbf A^{d-1}_Y
\longrightarrow\cdots\longrightarrow\mathbf A^1_Y
\longrightarrow Y
$$

of $g$ in which every displayed arrow is smooth of relative dimension one:
the first is an étale map followed by a projection, and the others are
projections. The case $d=0$ is étale localization. Hence, in the
induction on the degree, it suffices to treat affine $Y$ and $Y'$ with $g$
smooth of relative dimension one.

Finally, a sheaf $F$ as in Theorem [sk-thm-smooth-base-change] is
the filtered union of the subsheaves $F[n]$, ordered by divisibility of
integers invertible on $Y$. Inverse image commutes with this colimit,
and so do higher direct images along qcqs morphisms [Stacks, Tag 09Z1](https://stacks.math.columbia.edu/tag/09Z1).
Therefore it suffices to treat $\mathbf Z/n$-modules for each such $n$.
