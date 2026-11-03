+++
id = "prose-03-04"
kind = "hidden"
title = "Pulling back to a scheme"
order = 132
+++
A profinite set $S$ defines a pro-étale scheme
$\operatorname{Spec}LC(S,\mathbf Z)$ over $\mathbf Z$, where
$LC(S,\mathbf Z)$ is the ring of locally constant functions. The functor
$S\mapsto\operatorname{Spec}LC(S,\mathbf Z)$ is continuous and preserves
finite limits, as one checks on finite quotients of $S$. Hence it induces a
morphism of topoi $\Sh((\operatorname{Spec}\mathbf Z)_{\mathrm{pro}\acute{e}t})\to \Sh(*_{\mathrm{pro}\acute{e}t})$ [Stacks, Tag 00X6](https://stacks.math.columbia.edu/tag/00X6). Composing with the structure morphism of
$X$, we obtain

$$
p_X:\Sh(X_{\mathrm{pro}\acute{e}t})\longrightarrow\Sh(*_{\mathrm{pro}\acute{e}t}),
$$

and for a condensed ring $\Lambda$ we write $\Lambda_X=p_X^*\Lambda$.
For a morphism $f:X\to Y$ we have $p_Y\circ f=p_X$, and hence a canonical
isomorphism $f^{-1}\Lambda_Y\simeq\Lambda_X$, compatible with identities
and composition. Likewise, a morphism $\Lambda\to\Lambda'$ of condensed
rings pulls back to $\Lambda_X\to\Lambda'_X$, which defines extension of
scalars $\Lambda'_X\otimes_{\Lambda_X}-$ from $\Lambda_X$-modules to
$\Lambda'_X$-modules on $X_{\mathrm{pro}\acute{e}t}$. Thus both pullback along morphisms
and change of coefficients are obtained from $p_X^*$.

The next lemma identifies these rings with the completed coefficient
rings of classical $\ell$-adic cohomology.
