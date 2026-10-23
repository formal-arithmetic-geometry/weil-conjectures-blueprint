+++
kind  = "proof"
of    = "sk-lem-wrp-normal-geometric-cover"
uses = ["det-wrp-cover-open-immersion"]
+++
Since $Y$ is étale over $X$, it is locally noetherian and normal
([Stacks `033C`](https://stacks.math.columbia.edu/tag/033C)), and hence its
connected components are integral, open and closed
([Stacks `033N`](https://stacks.math.columbia.edu/tag/033N)). Fix a nonempty
component $Y_1$. A valuative lift whose generic point lies in $Y_1$ stays in
$Y_1$, so the hypothesis also holds for $Y_1\to X$.

The image of $Y_1$ is nonempty and open, hence contains the generic
point $\eta$ of $X$. The generic fibre of $Y_1$ is integral and
étale over $k(X)$, so it is $\operatorname{Spec}L$ for a finite
separable extension $L/k(X)$. Let $N$ be the normalization of $X$ in
$L$. By [det-wrp-cover-open-immersion], $Y_1\to X$ factors through an open
immersion $f:Y_1\to N$.

Finally, let $n\in N$ and choose a valuation ring $V\subseteq L$
dominating $\mathcal O_{N,n}$
([Stacks `00IA`](https://stacks.math.columbia.edu/tag/00IA)). By hypothesis, the
generic map $\operatorname{Spec}L\to Y_1$ extends to a map
$\operatorname{Spec}V\to Y_1$. Its composite with $f$ agrees with the
canonical map $\operatorname{Spec}V\to N$ generically and over $X$,
so the two maps agree by separatedness of $N\to X$. Consequently $n$
lies in the open image of $Y_1$. We conclude that $Y_1=N$ is finite
étale over $X$, and its image, being nonempty, open and closed, is
all of $X$.
