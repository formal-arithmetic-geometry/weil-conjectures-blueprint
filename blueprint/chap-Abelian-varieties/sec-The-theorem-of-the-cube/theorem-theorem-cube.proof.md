+++
kind = "proof"
of = "theorem-theorem-cube"
order = 1487
uses = ["definition-compactification-refinement", "lemma-triviality-fibres", "corollary-triviality-over-open-cover-base", "lemma-triviality-near-fibre"]
+++
The local trivializations are glued by
Corollary [corollary-triviality-over-open-cover-base], which shows
that $\mathcal L$ is pulled back from $Y\times Z$; the slice
$x\times Y\times Z$ then identifies the sheaf on $Y\times Z$.

Let $Z_0\subset Z$ be the set of points over which $\mathcal L$ is
trivial on the fibre of $p:X\times Y\times Z\to Z$. It contains $z$.
It is closed by Lemma [lemma-triviality-fibres](2) applied to
$X\times Y$, which is proper and geometrically integral [Stacks, [05P3](https://stacks.math.columbia.edu/tag/05P3)].
It is open by Lemma [lemma-triviality-near-fibre]. Since $Z$ is
connected, $Z_0=Z$. Now Lemma [lemma-triviality-near-fibre] gives
an open cover of $Z$ over whose members $\mathcal L$ is trivial.

Let $\pi:X\times Y\times Z\to Y\times Z$ be the projection and $\sigma$
its section through $x$. We apply
Corollary [corollary-triviality-over-open-cover-base] with $P=X$,
$T=Y\times Z$ and the open cover by the products of $Y$ with these
opens. It shows that $\mathcal M=\pi_*\mathcal L$ is invertible and
that $\pi^*\mathcal M\to\mathcal L$ is an isomorphism. Hence
$\mathcal M\simeq\sigma^*\pi^*\mathcal M\simeq\sigma^*\mathcal L$. This
is the restriction of $\mathcal L$ to $x\times Y\times Z$, which is
trivial by hypothesis. We conclude that $\mathcal L\simeq\pi^*\mathcal M$
is trivial.
