+++
kind = "proof"
of = "corollary-bounded-below-classical-complexes"
order = 130
uses = ["theorem-classical-sheaves-essential-image"]
+++
We need the first assertion so that “classical complex” defines a
triangulated subcategory, and for extensions we use the vanishing of
$R^1\nu_{X,*}$ from the theorem. The equivalence then follows by
comparing cohomology sheaves.

For kernels and cokernels the first assertion follows from exactness and
full faithfulness of $\nu_X^*$. Indeed, a map between classical sheaves is
$\nu_X^*$ of a map of étale sheaves, and $\nu_X^*$ carries its kernel
and cokernel to the kernel and cokernel. Given an extension
$0\to\nu_X^*F\to G\to\nu_X^*F'\to0$, we apply $\nu_{X,*}$. Since
$R^1\nu_{X,*}\nu_X^*F=0$ by Theorem [theorem-bounded-below-cohomology-comparison], the
result $0\to F\to\nu_{X,*}G\to F'\to0$ is exact, and the counit maps
its pullback to the original extension. This map is the identity on the
outer terms, so by the five lemma $G\simeq\nu_X^*\nu_{X,*}G$ is classical.

The functor $\nu_X^*$ lands in classical complexes and is fully
faithful on $D^+$ by
Theorem [theorem-bounded-below-cohomology-comparison], so the
equivalence amounts to the counit $\nu_X^*R\nu_{X,*}K\to K$ being an
isomorphism for $K$ in $D^+_{\mathrm{class}}$. By (2.7), every classical
sheaf $\nu_X^*F$ is $\nu_{X,*}$-acyclic, so the hypercohomology spectral
sequence for $R\nu_{X,*}K$ degenerates and
$H^q(R\nu_{X,*}K)=\nu_{X,*}H^q(K)$. On $H^q$ the counit is therefore the
counit $\nu_X^*\nu_{X,*}H^q(K)\to H^q(K)$ for a classical sheaf, which is
an isomorphism by Theorem [theorem-classical-sheaves-essential-image]; see
[Stacks, [09B1](https://stacks.math.columbia.edu/tag/09B1)].
