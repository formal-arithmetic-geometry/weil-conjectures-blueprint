+++
kind = "proof"
of = "lemma-geometric-coverings-normal-scheme"
order = 1078
+++
We compare a component $Y_1$ with the normalization $N$ of $X$
in the function field of $Y_1$. By Zariski's main theorem, $Y_1$ is an open
subscheme of $N$, and by the valuative hypothesis this open
subscheme contains every point of $N$.

Since $Y$ is étale over $X$, it is locally noetherian and normal
[Stacks, [033C](https://stacks.math.columbia.edu/tag/033C)]. Hence its connected components are integral, open
and closed [Stacks, [033N](https://stacks.math.columbia.edu/tag/033N)]. Fix a nonempty component $Y_1$. Since a valuative
lift whose generic point lies in $Y_1$ stays in $Y_1$, the
hypothesis also holds for $Y_1\to X$.

The image of $Y_1$ is nonempty and open, hence contains the generic
point $\eta$ of $X$. The generic fibre of $Y_1$ is integral and
étale over $k(X)$, so it is $\operatorname{Spec}k(Y_1)$. Thus the
function field $k(Y_1)$ is a finite separable extension of $k(X)$, and we let $N$
be the normalization of $X$ in $k(Y_1)$. Since $X$ is Nagata, $N$ is finite over $X$ [Stacks, [035B](https://stacks.math.columbia.edu/tag/035B), [0AVK](https://stacks.math.columbia.edu/tag/0AVK)].
We claim that $Y_1\to X$ factors through a map $f:Y_1\to N$. Indeed,
since $Y_1$ is normal, an element of $k(Y_1)$ that is integral over the
coordinate ring of an affine open of $X$ lies in every local ring of
$Y_1$ over that open. These regular functions agree in $k(Y_1)$, and hence
they glue. The map $f$ is separated, locally of finite type and
locally quasi-finite, because its fibres lie in the zero-dimensional
fibres of $Y_1\to X$.

We show that $f$ is an open immersion. Choose affine opens
$W\subseteq Y_1$ and $N_0\subseteq N$ with $f(W)\subseteq N_0$.
By Zariski's main theorem [Stacks, [05K0](https://stacks.math.columbia.edu/tag/05K0)], $W$ is an open subscheme of
a finite $N_0$-scheme, and the reduced closure of $W$ in it is integral,
finite and birational over $N_0$, with function field $k(Y_1)$. Since
$N_0$ is normal, this closure is $N_0$ [Stacks, [0AB1](https://stacks.math.columbia.edu/tag/0AB1)], and therefore
$W\to N_0$ is an open immersion. These local inverses glue: on the
intersection of two such open images, the inverse sections agree generically, hence everywhere by
separatedness, and so they glue to an inverse on the union of the
images.

Finally, let $n\in N$ and choose a valuation ring $V\subseteq k(Y_1)$
dominating $\mathcal O_{N,n}$ [Stacks, [00IA](https://stacks.math.columbia.edu/tag/00IA)]. By hypothesis, the
generic map $\operatorname{Spec}k(Y_1)\to Y_1$ extends to a map
$\operatorname{Spec}V\to Y_1$, whose composite with $f$ agrees with the
canonical map $\operatorname{Spec}V\to N$ generically and over $X$.
By separatedness of $N\to X$ the two maps agree, so $n$
lies in the open image of $Y_1$. We conclude that $Y_1=N$ is finite
étale over $X$. In particular its image is open and closed, and being
nonempty, it is all of $X$.
