+++
kind = "proof"
of = "sk-thm-picard-twist"
uses = ["sk-thm-picard-perfect", "sk-thm-picard-rr"]
+++
Choose an ample invertible sheaf $\mathcal M$ on $C$. For $r\gg0$, Serre vanishing
and Riemann–Roch show that $\mathcal L\otimes\mathcal M_{k'}^{\otimes r}$
has vanishing $H^1$ and a positive-dimensional space of sections.
As long as $h^0$ is larger than $1$, we choose a nonzero section and
a point $x\in C(k)$ where that section is nonzero. Such a point
exists: the zero divisor of the section is finite, so its image in $C$
is a finite set, and its complement is a nonempty open of $C$, which
contains a point of $C(k)$ because the $k$-rational points of a smooth
$k$-scheme are dense when $k$ is separably closed [Stacks, Tag 056U](https://stacks.math.columbia.edu/tag/056U).
For the current sheaf $\mathcal F$, the sequence

$$
0\longrightarrow\mathcal F(-x_{k'})
\longrightarrow\mathcal F
\longrightarrow\mathcal F|_{x_{k'}}\longrightarrow0
$$

shows that subtracting $x_{k'}$ lowers $h^0$ by exactly $1$ and
preserves $H^1=0$: the map
$H^0(C_{k'},\mathcal F)\to\mathcal F|_{x_{k'}}$ is onto the one-dimensional
fibre, because the chosen section does not vanish at $x_{k'}$. We
continue until $h^0=1$. Since all subtracted
points come from $k$, the resulting twist has the form
$\mathcal M_0=\mathcal M^{\otimes r}(-x_1-\cdots-x_s)$ on $C$.
Normalizing along $P$ does not change the dimensions of fibre
cohomology, and hence the rigidified twist satisfies the same conditions
(see [Stacks, Tag 0B9Y](https://stacks.math.columbia.edu/tag/0B9Y)).
