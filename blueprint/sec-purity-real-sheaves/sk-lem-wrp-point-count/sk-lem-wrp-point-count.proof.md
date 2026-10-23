+++
kind  = "proof"
of    = "sk-lem-wrp-point-count"
uses = ["det-i-real-normalization"]
+++
By Noether normalization
([Stacks `00OY`](https://stacks.math.columbia.edu/tag/00OY),
[det-i-real-normalization]) there is a finite map
$U_0\to\mathbf A^1_{k_0}$. The coordinate ring of $U_0$ is a finite
torsion-free module over $k_0[t]$, because the map from $k_0[t]$ is
injective on each irreducible component, all of which have dimension
one (a nonzero kernel would force dimension zero). Hence it is free of
some rank $D$. After any extension of the base field, every fibre
has a coordinate ring of dimension $D$, and therefore at most $D$
rational points by the Chinese remainder theorem. Summing over
$\mathbf A^1(k_n)$, we obtain the first bound
([lem-wf-point-count-linear-growth]). For a finite scheme, the number of
rational points is at most its number of geometric points.
