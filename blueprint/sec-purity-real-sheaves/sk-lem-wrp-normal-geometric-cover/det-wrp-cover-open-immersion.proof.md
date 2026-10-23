+++
kind  = "proof"
of    = "det-wrp-cover-open-immersion"
+++
Since $X$ is Nagata, $N$ is finite over $X$
([Stacks `035B`](https://stacks.math.columbia.edu/tag/035B),
[Stacks `0AVK`](https://stacks.math.columbia.edu/tag/0AVK)).
We claim that $Y_1\to X$ factors through a map $f:Y_1\to N$. Indeed,
since $Y_1$ is normal, an element of $L$ that is integral over the
coordinate ring of an affine open of $X$ lies in every local ring of
$Y_1$ over that open. These regular functions agree in $L$, and hence
they glue. The map $f$ is separated, locally of finite type and
locally quasi-finite, because its fibres lie in the zero-dimensional
fibres of $Y_1\to X$.

We show that $f$ is an open immersion. Choose affine opens
$W\subseteq Y_1$ and $N_0\subseteq N$ with $f(W)\subseteq N_0$.
By Zariski's main theorem
([Stacks `05K0`](https://stacks.math.columbia.edu/tag/05K0)), $W$ is an open
subscheme of a finite $N_0$-scheme. The reduced closure of $W$ in it is
integral, finite and birational over $N_0$, with function field $L$. Since
$N_0$ is normal, this closure is $N_0$
([Stacks `0AB1`](https://stacks.math.columbia.edu/tag/0AB1)), and therefore
$W\to N_0$ is an open immersion. On the intersection of two such open
images, the inverse sections agree generically, hence everywhere by
separatedness, and so they glue to an inverse on the union of the
images.
