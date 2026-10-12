+++
kind  = "proof"
of    = "prop-weil-pbc-inverse-image-exact"
+++
By [def-weil-pbc-inverse-image] the functor $u^{-1}$ is the left adjoint of
the direct image $u_*$ of [def-weil-pbc-direct-image] and is obtained by
sheafifying the presheaf inverse image along the functor $U_{\Et}\to V_{\Et}$
of [def-weil-pbc-etale-site]. The presheaf inverse image is computed
sectionwise by a filtered colimit of sections of the given presheaf; it has a
left adjoint (extension by zero of presheaves) and a right adjoint (presheaf
direct image), so it preserves kernels and cokernels and is exact.
Sheafification of presheaves of abelian groups is exact (Stacks Project,
Lemma 7.10.15, Tag [00WJ](https://stacks.math.columbia.edu/tag/00WJ)), and a
composite of exact functors is exact, so $u^{-1}$ is exact. This is the
exactness of pullback of abelian sheaves on small etale sites (Stacks
Project, Lemma 59.36.2, Tag
[03Q1](https://stacks.math.columbia.edu/tag/03Q1)); the source category is
the category of sheaves of [def-weil-pbc-etale-sheaves].
