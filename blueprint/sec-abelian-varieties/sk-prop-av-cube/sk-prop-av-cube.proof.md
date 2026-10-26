+++
kind  = "proof"
of    = "sk-prop-av-cube"
+++
Let $Z_0\subset Z$ be the set of points over which $\mathcal L$ is
trivial on the fibre of $p:X\times Y\times Z\to Z$. It contains $z$, it
is closed by [sk-lem-abelian-seesaw] (2) applied to $X\times Y$,
which is proper and geometrically integral (Stacks [05P3](https://stacks.math.columbia.edu/tag/05P3)), and it is open by
[sk-lem-abelian-cube-open]. Since $Z$ is connected, $Z_0=Z$, and
[sk-lem-abelian-cube-open] gives an open cover of $Z$ over whose
members $\mathcal L$ is trivial. By [sk-lem-abelian-seesaw] (3),
$\mathcal L\simeq p^*\mathcal M$ for an invertible sheaf $\mathcal M$ on
$Z$. Pulling back along $(x,y,\operatorname{id}):Z\to X\times Y\times Z$,
which factors through $x\times Y\times Z$, we find that $\mathcal M$ is
trivial, and hence so is $\mathcal L$.
