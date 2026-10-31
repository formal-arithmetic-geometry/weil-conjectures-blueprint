+++
kind = "proof"
of = "sk-prop-av-cube"
+++
Let $Z_0\subset Z$ be the set of points over which $\mathcal L$ is
trivial on the fibre of $p:X\times Y\times Z\to Z$. It contains $z$, it
is closed by Lemma [sk-lem-abelian-seesaw](2) applied to $X\times Y$,
which is proper and geometrically integral [Stacks, Tag 05P3](https://stacks.math.columbia.edu/tag/05P3), and it is open by
Lemma [sk-lem-abelian-cube-open]. Since $Z$ is connected, $Z_0=Z$, and
Lemma [sk-lem-abelian-cube-open] gives an open cover of $Z$ over whose
members $\mathcal L$ is trivial. We glue these trivializations, using
the trivialization on $x\times Y\times Z$ to normalize them. Let
$\pi:X\times Y\times Z\to Y\times Z$ be the projection and $\sigma$ its
section through $x$, and fix a generator $e$ of $\sigma^*\mathcal L$.
Since $H^0(X,\mathcal O_X)=k$, flat base change gives
$\pi_*\mathcal O=\mathcal O_{Y\times Z}$ over every open of
$Y\times Z$. On each member of the cover we multiply a generator of
$\mathcal L$ by the pullback along $\pi$ of a unit, so that its
restriction along $\sigma$ is $e$. On an overlap the ratio of two such
generators is a unit, hence pulled back from $Y\times Z$, and its
restriction along $\sigma$ is $1$; so the ratio is $1$. The generators
therefore glue to a trivialization of $\mathcal L$.
