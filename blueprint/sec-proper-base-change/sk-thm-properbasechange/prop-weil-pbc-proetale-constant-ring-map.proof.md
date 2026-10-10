+++
kind  = "proof"
of    = "prop-weil-pbc-proetale-constant-ring-map"
+++
By [def-weil-pbc-proetale-modules] the sheaf $\Lambda_{T,\Proet}$ is the
sheafification of $U\mapsto\operatorname{Cont}(\pi_0(|U|),\Lambda)$;
decomposing a pro-etale object into its clopen connected components, which
form a covering in the small pro-etale topology
[def-weil-pbc-proetale-site], identifies $\Lambda_{T,\Proet}$ with the free
$\Lambda$-module sheaf of rank one, so that

$$
 \operatorname{Hom}\bigl(\Lambda_{T,\Proet},G\bigr)=G(T)
$$

for every sheaf $G$ of $\Lambda$-modules on $T_{\Proet}$, naturally in $G$.
By [def-weil-pbc-inverse-image] the inverse image is the sheafification of
the presheaf inverse image, hence left adjoint to the direct image, and
adjunction therefore gives a natural bijection

$$
 \operatorname{Hom}\bigl(u^{-1}\Lambda_{V,\Proet},G\bigr)
 \cong\operatorname{Hom}\bigl(\Lambda_{V,\Proet},u_*G\bigr)
 \cong(u_*G)(V)=G(U)
 \cong\operatorname{Hom}\bigl(\Lambda_{U,\Proet},G\bigr)
$$

for every sheaf $G$ of $\Lambda$-modules on $U_{\Proet}$. The composite is
the map induced by the displayed structure morphism, which is consequently an
isomorphism by the Yoneda lemma.
