+++
kind = "proof"
of = "sk-lem-wrp-point-count"
uses = ["det-i-real-normalization"]
+++
By Noether normalization [Stacks, Tag 00OY](https://stacks.math.columbia.edu/tag/00OY) there is a finite map
$U_0\to\mathbf A^1_{k_0}$. The coordinate ring of $U_0$ is a finite
torsion-free module over $k_0[t]$. To see this, let $f\ne0$ in
$k_0[t]$ and $fa=0$. On each irreducible component of $U_0$ the image
of $f$ is nonzero, since otherwise the component would be finite over
$k_0[t]/(f)$ and hence of dimension zero. Since the coordinate ring of
each component is a domain, $fa=0$ forces $a$ to vanish on every
component, and $a=0$ because $U_0$ is reduced. Hence the
coordinate ring of $U_0$ is free of some rank $D$. After any
extension of the base field, every fibre has a coordinate ring of
dimension $D$, and therefore at most $D$ rational points by the Chinese
remainder theorem. Summing over $\mathbf A^1(k_n)$, we obtain the
first bound. The second holds because the number of rational points
of a finite scheme is at most its number of geometric points.
