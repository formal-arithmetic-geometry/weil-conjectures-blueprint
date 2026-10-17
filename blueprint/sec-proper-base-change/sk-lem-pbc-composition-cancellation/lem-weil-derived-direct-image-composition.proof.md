+++
kind  = "proof"
of    = "lem-weil-derived-direct-image-composition"
+++
*Condensed coefficients.* Let $\Lambda$ be a commutative condensed ring. The
pushforward of module objects $f_*:\Mod_{\Lambda_X}\to\Mod_{\Lambda_Y}$ has
the module pullback $f^*$ as left adjoint
([sk-def-sfb-module-pushforward-pullback]), and $f^*$ is exact
([sk-prop-sfb-module-pullback-exact]). Hence $f_*$ carries K-injective
complexes [def-weil-pbc-kinjective-resolutions] to K-injective complexes: for
an acyclic $B$ one has $\operatorname{Hom}(B,f_*I)=\operatorname{Hom}(f^*B,I)$,
and $f^*B$ is acyclic. This is the argument of
[lem-weil-pbc-direct-image-preserves-injectives], applied to complexes of
$\Lambda$-modules on the pro-étale site. If $K\to I$ is a K-injective
resolution, then $f_*I$ is a K-injective complex computing $Rf_*K$, so

$$
 Rg_*Rf_*K=g_*f_*I\cong(gf)_*I=R(gf)_*K,
$$

the middle isomorphism being the composition isomorphism of module
pushforwards ([def-sfb-module-lower-star-comp]). By the well-definedness and
functoriality of K-injective resolutions ([lem-sp-kinjective-computes],
part (1)), the resulting isomorphism does not depend on $I$ and is natural in
$K$. Identity and associativity hold because the composition isomorphisms of
the module pushforwards satisfy them on the same representative $I$. The
argument is the same for every $\Lambda$, which gives items (1)–(4); for $\Lambda=A_{E,n}$ the module
pullback is the classical $f^{-1}$ of
[def-weil-derived-pullback-tensor-hom]. No completeness, reduction or
extension of scalars is involved: for $\mathcal O_E$, $E$ and $\Qlb$ the
categories $D(-_{\mathrm{proét}},\Lambda)$ and the functors $Rf_*$ are defined
directly over the condensed ring.

*Étale site.* The same argument applies verbatim on the small étale site with
any coefficient ring (item (5)) and to sheaves of abelian groups.

Finally, for an automorphism $\sigma$ the direct image $R\sigma_*$ is
inverse to $R(\sigma^{-1})_*$ by the identity and associativity properties.
An automorphism of the diagram $X\to Y\to Z$ therefore transports $c_{g,f}$
to itself by associativity, which is the asserted compatibility with
transport of structure.
