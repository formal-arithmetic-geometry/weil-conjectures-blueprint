+++
kind = "proof"
of = "corollary-bounded-below-classical-complexes"
order = 130
uses = ["proposition-topos-functoriality", "theorem-classical-sheaves-essential-image", "theorem-bounded-below-cohomology-comparison"]
+++
We need the first assertion so that “[classical](@definition-classical-pro-etale-sheaves) complex” defines a
triangulated subcategory, and for extensions we use the vanishing of
[$R^1\nu_{X,*}$](@proposition-comparison-morphism-inverse-image) from the theorem. The equivalence then follows by
comparing cohomology sheaves.

For kernels and cokernels the first assertion follows from exactness and
full faithfulness of [$\nu_X^*$](@proposition-comparison-morphism-inverse-image). Indeed, a map between [classical](@definition-classical-pro-etale-sheaves) sheaves is
[$\nu_X^*$](@proposition-comparison-morphism-inverse-image) of a map of étale sheaves, and [$\nu_X^*$](@proposition-comparison-morphism-inverse-image) carries its kernel
and cokernel to the kernel and cokernel. Given an extension
$0\to\href{@proposition-comparison-morphism-inverse-image}{\nu_X^*F}\to G\to\href{@proposition-comparison-morphism-inverse-image}{\nu_X^*F'}\to0$, we apply [$\nu_{X,*}$](@proposition-comparison-morphism-inverse-image). Since
$\href{@proposition-comparison-morphism-inverse-image}{R^1\nu_{X,*}}\href{@proposition-comparison-morphism-inverse-image}{\nu_X^*F}=0$ by Theorem [theorem-bounded-below-cohomology-comparison], the
result $0\to F\to\href{@proposition-comparison-morphism-inverse-image}{\nu_{X,*}G}\to F'\to0$ is exact, and the counit maps
its pullback to the original extension. This map is the identity on the
outer terms, so by the five lemma $G\simeq\href{@proposition-comparison-morphism-inverse-image}{\nu_X^*}\href{@proposition-comparison-morphism-inverse-image}{\nu_{X,*}G}$ is [classical](@definition-classical-pro-etale-sheaves).

The functor [$\nu_X^*$](@proposition-comparison-morphism-inverse-image) lands in [classical](@definition-classical-pro-etale-sheaves) complexes and is fully
faithful on $D^+$ by
Theorem [theorem-bounded-below-cohomology-comparison], so the
equivalence amounts to the counit $\href{@proposition-comparison-morphism-inverse-image}{\nu_X^*}\href{@proposition-comparison-morphism-inverse-image}{R\nu_{X,*}K}\to K$ being an
isomorphism for $K$ in $D^+_{\mathrm{class}}$. By (2.7), every [classical](@definition-classical-pro-etale-sheaves)
sheaf [$\nu_X^*F$](@proposition-comparison-morphism-inverse-image) is [$\nu_{X,*}$](@proposition-comparison-morphism-inverse-image)-acyclic, so the hypercohomology spectral
sequence for [$R\nu_{X,*}K$](@proposition-comparison-morphism-inverse-image) degenerates and
$H^q(\href{@proposition-comparison-morphism-inverse-image}{R\nu_{X,*}K})=\href{@proposition-comparison-morphism-inverse-image}{\nu_{X,*}}H^q(K)$. On $H^q$ the counit is therefore the
counit $\href{@proposition-comparison-morphism-inverse-image}{\nu_X^*}\href{@proposition-comparison-morphism-inverse-image}{\nu_{X,*}}H^q(K)\to H^q(K)$ for a [classical](@definition-classical-pro-etale-sheaves) sheaf, which is
an isomorphism by Theorem [theorem-classical-sheaves-essential-image]; see
[Stacks, [09B1](https://stacks.math.columbia.edu/tag/09B1)].
