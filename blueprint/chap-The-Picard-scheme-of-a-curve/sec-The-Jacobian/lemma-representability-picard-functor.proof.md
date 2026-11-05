+++
kind = "proof"
of = "lemma-representability-picard-functor"
order = 1548
+++
The preceding lemmas assume $C$ geometrically integral. To see that this
holds, note that $\bar k/k$ is purely inseparable. Hence $C_{\bar k}\to C$
is a homeomorphism, and $C_{\bar k}$ is connected and smooth, hence
integral. We rigidify using a point $P\in C(k)$. Such a point exists
because $k$ is separably closed and the $k$-points of the smooth curve
$C$ are dense [Stacks, [056U](https://stacks.math.columbia.edu/tag/056U)].

By Proposition [proposition-divisors-degree-g-open-chart] we have a
representable open subfunctor $F\subset\operatorname{Pic}_{C/k}$. For a fixed class
$M\in\operatorname{Pic}_{C/k}(k)$, the translate
$M^{-1}F$, consisting of the classes $\mathcal L$ with
$\mathcal L\otimes M$ in $F$, is another representable open
subfunctor.

We show that these translates cover $\operatorname{Pic}_{C/k}$. Let a
class on a $k$-scheme $T$ and a point $t\in T$ be given. We apply
Lemma [lemma-twisting-h-0-1-h] to its fibre over the residue field
$k'=\kappa(t)$. This gives an invertible sheaf $\mathcal M_0$ on $C$,
defined over $k$, such that the twisted fibre has $h^0=1$ and $H^1=0$.
By Lemma [lemma-coherent-base-change-invertible-sheaves], the twisted class then
lies in $F$ over an open neighbourhood of $t$. Letting $t$ vary, we see
that the open loci where the corresponding translated class lies
in $F$ cover $T$. Note that the translates are indexed by classes over
$k$, while the points of $T$ have arbitrary residue fields. This is why
Lemma [lemma-twisting-h-0-1-h] asks for a twist defined over $k$ for
every extension $k'$.

The intersections of the charts are open in either chart, and their
transition isomorphisms satisfy the cocycle condition by functoriality.
An fppf sheaf covered by representable open subfunctors is
representable [Stacks, [0B9Q](https://stacks.math.columbia.edu/tag/0B9Q), [0B9Z](https://stacks.math.columbia.edu/tag/0B9Z)]. Hence gluing the charts gives a
scheme representing $\operatorname{Pic}_{C/k}$. It is locally of finite
type because each chart is an open of $\operatorname{Hilb}^{g}_{C/k}$.
