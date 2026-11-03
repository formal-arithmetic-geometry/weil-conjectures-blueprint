+++
kind = "proof"
of = "sk-lem-failure-field"
uses = ["sk-prop-injectivity", "sk-lem-minimal"]
+++
The idea is to shrink the source of the direct image, keeping a fixed
nonzero element of the cokernel, until it becomes the spectrum of a field: a
minimal closed subscheme carrying the failure exists by a limit argument,
and its generic point still carries it.

Choose a square for which base change fails and a nonzero element of the
cokernel of the base change map at a geometric point. For a qcqs scheme $Z'$ over
the source $Z$ of the morphism along which we take direct image, let $P(Z')$
mean that this fixed element is not in the image after pullback to $Z'$. The
verification in [Stacks, Tag 0F07](https://stacks.math.columbia.edu/tag/0F07) shows that $P$ has three properties.

1. thickenings preserve $P$, by topological invariance;
2. limits with affine transition maps preserve $P$, by continuity;
3. if $P(Z')$ holds and $V\subset Z'$ is a quasi-compact open with
   closed complement $W$, then $P(V)$ or $P(W)$ holds.

To prove the third property, let $j:V\to Z'$ and $i:W\to Z'$ be
the inclusions. We embed the coefficient sheaf $M$ into
$j_*J\oplus i_*i^{-1}M$, with $J$ injective on $V_{\acute{e}t}$. By
Lemma [sk-prop-injectivity], the cokernel for $M$ embeds into the sum of
the cokernels for $j_*J$ and for $i_*i^{-1}M$, so the fixed element survives
in one of them. Closed direct image is exact, so the cokernel for
$i_*i^{-1}M$ is the cokernel for $i^{-1}M$ on $W$. For the
open summand, let $j'$ and $g_V$ be the base changes of $j$ and $g$. Then
$\mathrm{BC}(g,n,q-1)$ shows that $R^pj'_*g_V^{-1}J=0$ for
$0<p<q$. Hence the edge map of the Leray spectral sequence for the
composite with $j'$ is injective in degree $q$, and it embeds the cokernel
for $j_*J$ into the cokernel for $J$ on $V$. Thus $P(V)$ or $P(W)$ holds.

By the second property and Zorn's lemma, there is a minimal closed
subscheme with $P$. It is nonempty, and by the first property it is reduced. Let
$\xi$ be the generic point of an irreducible component. Every affine
open neighbourhood of $\xi$ has $P$, since otherwise its closed
complement, a smaller closed subscheme, would have $P$. The limit of
these neighbourhoods is $\operatorname{Spec}\kappa(\xi)$, which has $P$
by the second property (compare [Stacks, Tag 0F06](https://stacks.math.columbia.edu/tag/0F06)).
