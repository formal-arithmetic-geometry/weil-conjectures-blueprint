+++
kind  = "proof"
of    = "sk-prop-av-cube"
+++
Let $Z_0\subset Z$ be the set of points over which $\mathcal L$ is
trivial on the fibre of $p:X\times Y\times Z\to Z$. It contains $z$, it
is closed by [sk-lem-abelian-seesaw] (2) applied to $X\times Y$,
which is proper and geometrically integral (Stacks [05P3](https://stacks.math.columbia.edu/tag/05P3)), and it is open by
[sk-lem-abelian-cube-open]. Since $Z$ is connected, $Z_0=Z$, and
[sk-lem-abelian-cube-open] gives an open cover $(U_\alpha)$ of $Z$ such
that $\mathcal L$ is trivial on $X\times Y\times U_\alpha$. Let
$\pi:X\times Y\times Z\to Y\times Z$ be the projection and $\sigma$ the
section $x\times Y\times Z$. Since $X$ is proper and geometrically
integral, $\pi$ induces bijections
$\Gamma(V,\mathcal O)\simeq\Gamma(\pi^{-1}V,\mathcal O)$
(Stacks [0BUG](https://stacks.math.columbia.edu/tag/0BUG)). Rescale the
local generators of $\mathcal L$ over the opens
$\pi^{-1}(Y\times U_\alpha)$ so that their pullbacks along $\sigma$
agree with a fixed generator of $\sigma^*\mathcal L\simeq\mathcal O$.
Two such generators differ by a unit that is $1$ on the section, hence
equal to $1$; so they glue, and $\mathcal L$ is trivial.
