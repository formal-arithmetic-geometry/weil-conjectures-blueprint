+++
kind = "proof"
of = "proposition-multiplication-n"
order = 1498
+++
We use the isomorphism $[n]^*\mathcal N\simeq\mathcal N^{\otimes n^2}$
twice: on curves in the fibres of $[n]$ it shows that $[n]$ is finite,
and in Euler characteristics it computes the degree. In between,
translation invariance shows that all fibres have the same length, which
makes $[n]$ finite locally free. Whether $[n]$ is étale is decided by
its differential.

Since finiteness, flatness and the degree may be checked after base
change to an algebraic closure, we may assume that $k$ is
algebraically closed. Choose a symmetric ample $\mathcal N$
(Lemma [lemma-symmetric-ample-sheaf]); then
$[n]^*\mathcal N\simeq\mathcal N^{\otimes n^2}$ by
Proposition [proposition-pullback-multiplication-n]. If a fibre of $[n]$ had positive
dimension, it would contain a proper integral curve. Since $[n]$ maps
that curve to a point, the restriction of
$[n]^*\mathcal N$ to it is trivial, whereas the restriction of
$\mathcal N^{\otimes n^2}$ has positive degree. Hence every fibre has
dimension zero, and since $[n]$ is proper, it is finite. Its image is a
closed subset of dimension $g$, hence equal to the integral variety $A$
(Lemma [lemma-abelian-variety-commutative]).
After base change to an algebraic closure of its residue field, every
fibre of $[n]$ becomes a translate of $A[n]$. Indeed, if $y=nx_0$, then
translation by $x_0$ carries $A[n]=[n]^{-1}(0)$ isomorphically onto
$[n]^{-1}(y)$, because $[n]$ is a homomorphism. Hence all fibres have the
same degree $r=\dim_k\Gamma(A[n],\mathcal O_{A[n]})$.

To get flatness from the constancy of the fibre degree, we use the
following general fact. A finite morphism $f$ to a reduced Noetherian
scheme whose fibres all have degree $r$ is finite locally free of rank
$r$. Indeed, near any point Nakayama's lemma gives a surjection
$\mathcal O^{\oplus r}\to f_*\mathcal O$, since the fibre at that point
has dimension $r$. This surjection is an isomorphism at each generic
point, where the local ring is a field and both sides are vector
spaces of dimension $r$. Hence on an affine open every coordinate of a
section of its kernel lies in all minimal primes, and is therefore zero
because the ring is reduced. Since $A$ is smooth, hence
reduced, $[n]$ is finite locally free.

Recall that for a locally free sheaf $\mathcal E$ of rank $r$ on $A$,
the function $m\mapsto\chi(A,\mathcal E\otimes\mathcal N^{\otimes m})$
is a polynomial of degree $g$ with leading coefficient
$r\deg_{\mathcal N}(A)/g!$. Here
$\deg_{\mathcal N}(A)=(\mathcal N^g)$ is the degree of $A$ with respect
to $\mathcal N$, a positive integer because $\mathcal N$ is ample. We
compare the coefficients of $m^g$ in two expressions for
$\chi(A,[n]^*\mathcal N^{\otimes m})$. Since $[n]$ is finite, this
Euler characteristic equals
$\chi(A,[n]_*[n]^*\mathcal N^{\otimes m})$, which by the projection
formula is $\chi(A,\mathcal N^{\otimes m}\otimes[n]_*\mathcal O_A)$.
As $[n]_*\mathcal O_A$ is locally free of rank $\deg[n]$, the
coefficient is $\deg[n]\deg_{\mathcal N}(A)/g!$. Since
$[n]^*\mathcal N^{\otimes m}\simeq\mathcal N^{\otimes n^2m}$, it is also
$n^{2g}\deg_{\mathcal N}(A)/g!$. Hence

$$
\deg[n]\,\deg_{\mathcal N}(A)
=n^{2g}\deg_{\mathcal N}(A).
$$

Since $\deg_{\mathcal N}(A)>0$, we conclude that $\deg[n]=n^{2g}$; compare [Stacks, [0BFG](https://stacks.math.columbia.edu/tag/0BFG)].
It remains to treat étaleness. The differential of the group law at
$(0,0)$ is addition of tangent vectors. By induction, the differential
of $[n]$ at the identity is $n\operatorname{id}$. Since $[n]$ commutes
with translations, the same holds at every point. If $n$ is invertible,
$[n]$ is therefore étale. Base change along the identity section
gives the assertion for $A[n]$.
