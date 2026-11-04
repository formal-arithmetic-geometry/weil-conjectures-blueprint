+++
kind = "proof"
of = "lemma-reduction-field"
order = 670
+++
We shrink the source of the direct image, keeping a fixed
nonzero element of the cokernel, until it becomes the spectrum of a field. A
minimal closed subscheme carrying the failure exists by a limit argument,
and its generic point still carries it. The one nonformal step is the
third property below, which says that a failure on a scheme is seen either
on an open subscheme or on its closed complement. Its proof uses the
injectivity of the base change map.

Choose a square for which base change fails and a nonzero element of the
cokernel of the base change map at a geometric point. For a qcqs scheme $Z'$ over
the source $Z$ of the morphism along which we take direct image, let $P(Z')$
mean that this fixed element is not in the image after pullback to $Z'$. The
verification in [Stacks, [0F07](https://stacks.math.columbia.edu/tag/0F07)] shows that $P$ has three properties.

1. thickenings preserve $P$, by topological invariance;
2. limits with affine transition maps preserve $P$, by continuity;
3. if $P(Z')$ holds and $V\subset Z'$ is a quasi-compact open with
   closed complement $W$, then $P(V)$ or $P(W)$ holds.

To prove the third property, let $j:V\to Z'$ and $i:W\to Z'$ be
the inclusions. We embed the coefficient sheaf $M$ into
$j_*J\oplus i_*i^{-1}M$, with $J$ injective on $V_{\acute{e}t}$. By
Lemma [lemma-injectivity-base-change-map-degree], the cokernel for $M$ embeds into the sum of
the cokernels for $j_*J$ and for $i_*i^{-1}M$. Hence the fixed element
survives in one of them. Since closed direct image is exact, the cokernel
for $i_*i^{-1}M$ is the cokernel for $i^{-1}M$ on $W$. For the
open summand we must compare the direct image of $j_*J$ along the given
morphism with the direct image of $J$ along its composite with $j$. Let
$j'$ and $g_V$ be the base changes of $j$ and $g$. Upstairs,
$R^pj_*J=0$ for $p>0$ because $J$ is injective. Downstairs,
$\mathrm{BC}(g,n,q-1)$ identifies $R^pj'_*g_V^{-1}J$ with the pullback of
$R^pj_*J$, and so $R^pj'_*g_V^{-1}J=0$ for $0<p<q$. Hence the edge map of
the Leray spectral sequence for the composite with $j'$ is injective in
degree $q$, and it embeds the cokernel for $j_*J$ into the cokernel for
$J$ on $V$. Since the fixed element survives in one of the two summands,
we conclude that $P(V)$ or $P(W)$ holds.

The field comes out of the three properties as follows. The intersection
of a decreasing chain of closed subschemes is the limit of the chain, with
affine transition maps. By the second property and Zorn's lemma there is
therefore a minimal closed subscheme with $P$. It is nonempty, since $P$
fails for the empty scheme. By the first property it is reduced. Let $\xi$
be the generic point of an irreducible component. We claim that every
affine open neighbourhood of $\xi$ has $P$. By the third property, either
the neighbourhood or its closed complement has $P$. The complement is a
closed subscheme not containing $\xi$, hence strictly smaller, and by
minimality it does not have $P$. Since the minimal closed subscheme is
reduced, the limit of these neighbourhoods is
$\operatorname{Spec}\kappa(\xi)$. It has $P$ by the second property
(compare [Stacks, [0F06](https://stacks.math.columbia.edu/tag/0F06)]), and so $\kappa(\xi)$ is the field asserted in the
lemma.
