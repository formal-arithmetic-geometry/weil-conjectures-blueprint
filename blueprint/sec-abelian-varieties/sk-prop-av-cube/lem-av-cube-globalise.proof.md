+++
kind  = "proof"
of    = "lem-av-cube-globalise"
+++
We show that $\mathcal L=\mathcal M\otimes\mathcal N^\vee$ is trivial. Let
$\pi:X\times(Y\times Z)\to Y\times Z$ be the projection and $\sigma$ the slice
$x\times Y\times Z$, a section of $\pi$. As $X$ is proper and geometrically integral,
$\pi$ is the base change of $X\to\operatorname{Spec}k$ and induces bijections
$\Gamma(V,\mathcal O)\simeq\Gamma(\pi^{-1}V,\mathcal O)$ on all opens $V$
(Stacks [0BUG](https://stacks.math.columbia.edu/tag/0BUG) and flat base change). Local
generators of $\mathcal L$ over the opens $\pi^{-1}V$, with $V$ lying over a member of
the cover of $Z$, can therefore be rescaled by units of $\Gamma(V,\mathcal O)$ so that
their pullbacks along $\sigma$ agree with a fixed generator of
$\sigma^*\mathcal L\simeq\mathcal O$. Two such generators differ by a unit of
$\Gamma(\pi^{-1}(V\cap V'),\mathcal O)=\Gamma(V\cap V',\mathcal O)$ that is $1$ after
pulling back along $\sigma$, hence equal to $1$; so they agree on overlaps and glue to a
global generator. This is the tex's [sk-lem-abelian-seesaw] (3) followed by the
pullback along the section.
