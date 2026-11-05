+++
id = "prose-C-05"
kind = "hidden"
title = "Riemann–Roch and Serre duality (1)"
order = 1527
+++
The chart of the Picard scheme in degree $g$ is cut out by the
condition $h^1=0$. Let $\mathcal L$ be an invertible sheaf of degree $g$ on
a curve of genus $g$. Then Riemann–Roch gives $h^0(\mathcal L)-h^1(\mathcal L)=1$,
so $h^1(\mathcal L)=0$ if and only if $\mathcal L$ has exactly one
section up to scalars. In a family over $T$, coherent base change shows
that the condition “$Rf_{T,*}\mathcal L$ is an invertible sheaf in
degree zero” is open on $T$ and compatible with base change. It
therefore defines an open subfunctor of the Picard functor.

The condition is not closed, because $h^0$ can jump up under
specialization. For example, on a curve of genus two a divisor $D$ of
degree two has $h^0(\mathcal O(D))=1$ unless $\mathcal O(D)\simeq\omega_{C/k}$,
in which case $h^0=2$. The chart therefore misses the line of canonical
divisors in $\operatorname{Hilb}^{2}_{C/k}$, and we need its translates
to cover the Picard scheme in degree two.

Fix a smooth proper geometrically connected curve $C$ over $k$, with
structure morphism $f:C\to\operatorname{Spec}k$, and set
$g=\dim_kH^1(C,\mathcal O_C)$. Such a curve is projective
[Stacks, [0A26](https://stacks.math.columbia.edu/tag/0A26)].
