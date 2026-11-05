+++
kind = "proof"
of = "lemma-point-count-bound"
order = 1178
uses = ["lemma-point-count-bound--1", "lemma-point-count-bound--2"]
+++
We map $U_0$ finitely and flatly onto the affine line, whose
number of $k_n$-points is $q^n$, and bound the size of the fibres.

By Noether normalization [Stacks, [00OY](https://stacks.math.columbia.edu/tag/00OY)] there is a finite map
$U_0\to\mathbf A^1_{k_0}$, and the coordinate ring of $U_0$ is a finite
torsion-free module over $k_0[t]$. To see this, let $f\ne0$ in
$k_0[t]$ and $fa=0$. On each irreducible component of $U_0$ the image
of $f$ is nonzero, since otherwise the component would be finite over
$k_0[t]/(f)$ and hence of dimension zero. Since the coordinate ring of
each component is a domain, $fa=0$ forces $a$ to vanish on every
component, and then $a=0$ because $U_0$ is reduced.  As $k_0[t]$ is a
principal ideal domain, it follows that the
coordinate ring of $U_0$ is free of some rank $D$.  Hence, after any
extension of the base field, every fibre has a coordinate ring of
dimension $D$, and by the Chinese remainder theorem it has at most $D$ rational
points.  Summing over $\mathbf A^1(k_n)$, we obtain the
first bound.  The second holds because the number of rational points
of a finite scheme is at most its number of geometric points.
