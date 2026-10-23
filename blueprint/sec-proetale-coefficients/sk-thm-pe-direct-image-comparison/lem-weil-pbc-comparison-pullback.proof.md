+++
kind  = "proof"
of    = "lem-weil-pbc-comparison-pullback"
+++
Pass to right adjoints. By [def-weil-pbc-site-comparison-morphism] the functor
$\nu_{T,*}$ is restriction of a pro-etale sheaf to etale $T$-schemes, and by
[def-weil-pbc-direct-image] the direct image $u_*$ on either site is
$(u_*G)(E)=G(E\times_VU)$. For an etale $V$-scheme $E$ the base change
$E\times_VU$ is etale over $U$, so both composites $\nu_{V,*}u_{\Proet,*}$ and
$u_{\Et,*}\nu_{U,*}$ send a pro-etale sheaf $G$ on $U$ to
$E\mapsto G(E\times_VU)$. This gives a natural isomorphism
$\nu_{V,*}u_{\Proet,*}\simeq u_{\Et,*}\nu_{U,*}$. The composites
$u_{\Proet}^{-1}\nu_V^*$ and $\nu_U^*u_{\Et}^{-1}$ are left adjoint to these two
functors ([def-weil-pbc-inverse-image]), so the conjugate of this isomorphism is
the asserted isomorphism of left adjoints.

The functors $u_{\Et}^{-1}$ and $u_{\Proet}^{-1}$ are exact
([prop-weil-pbc-inverse-image-exact], [lem-sfb-finite-upper-star-exact]),
and so are $\nu_U^*$ and $\nu_V^*$. Applied termwise to complexes, the
isomorphism therefore descends to the derived categories
[def-weil-pbc-derived-categories]. Finally the left derived functor of the exact
functor $u_{\Proet}^*$ is computed termwise, $Lu_{\Proet}^*\simeq u_{\Proet}^{-1}$
on complexes, which gives the last isomorphism on bounded-below objects.
