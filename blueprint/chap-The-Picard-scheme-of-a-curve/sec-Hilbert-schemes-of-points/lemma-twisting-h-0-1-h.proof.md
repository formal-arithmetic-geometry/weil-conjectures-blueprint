+++
kind = "proof"
of = "lemma-twisting-h-0-1-h"
order = 1535
uses = ["definition-small-pro-etale-site", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "theorem-chow-s-lemma-projective-form", "theorem-riemann-roch-coherent-serre-duality"]
+++
We first twist by a large power of an ample sheaf on $C$, which kills
$H^1$ and leaves many sections. Then we remove $k$-rational points one
at a time, each time lowering $h^0$ by one and keeping $H^1=0$, until
$h^0=1$. The twist is defined over $k$ because the points are.

Choose an ample invertible sheaf $\mathcal M$ on $C$. For $r\gg0$, Serre vanishing
and Riemann–Roch show that $\mathcal L\otimes\mathcal M_{k'}^{\otimes r}$
has vanishing $H^1$ and a positive-dimensional space of sections.
As long as $h^0$ is larger than $1$, we choose a nonzero section and
a point $x\in C(k)$ where that section is nonzero. Such a point
exists. Indeed, the zero divisor of the section is finite, so its image in $C$
is a finite set. Its complement is a nonempty open of $C$. This open
contains a point of $C(k)$, because the $k$-rational points of a smooth
$k$-scheme are dense when $k$ is separably closed [Stacks, [056U](https://stacks.math.columbia.edu/tag/056U)].
For the current sheaf $\mathcal F$, consider the sequence

$$
0\longrightarrow\mathcal F(-x_{k'})
\longrightarrow\mathcal F
\longrightarrow\mathcal F|_{x_{k'}}\longrightarrow0
$$

The chosen section does not vanish at $x_{k'}$, so the map
$H^0(C_{k'},\mathcal F)\to\mathcal F|_{x_{k'}}$ is onto the one-dimensional
fibre. By the long exact sequence, subtracting $x_{k'}$ lowers $h^0$ by
exactly $1$ and preserves $H^1=0$. We continue until $h^0=1$. All
subtracted points come from $k$, so the resulting twist has the form
$\mathcal M_0=\mathcal M^{\otimes r}(-x_1-\cdots-x_s)$ on $C$.
Normalizing along $P$ does not change the dimensions of fibre
cohomology. Hence the rigidified twist satisfies the same conditions
(see [Stacks, [0B9Y](https://stacks.math.columbia.edu/tag/0B9Y)]).
