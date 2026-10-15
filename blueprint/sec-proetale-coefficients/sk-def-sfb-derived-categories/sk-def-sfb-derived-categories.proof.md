+++
kind  = "proof"
of    = "sk-def-sfb-derived-categories"
uses = ["sk-prop-sfb-module-category"]
+++
*Right derived functors.* $RF$ is [def-sfb-right-derived-functor]. A Grothendieck abelian
category has K-injective resolutions by [lem-sfb-grothendieck-k-injective].

*Left derived functors.* The hypothesis on $F$ is [def-sfb-preserves-kflat-quasi-iso], and
$LF$ is [def-sfb-left-derived-functor].

*Exact functors.* By [def-sfb-right-derived-exact] and [def-sfb-left-derived-exact].

*Derived adjunctions.* Let $K\in D(\mathcal C)$ and $L\in D(\mathcal D)$. Choose a K-flat
resolution $P\to K$ and a K-injective resolution $L\to I$, so that $Lf(K)=f(P)$ and
$Rg(L)=g(I)$. Since $I$ is K-injective, morphisms into $I$ in the derived category are
homotopy classes of maps. The adjunction $f\dashv g$ extends termwise to complexes and is
compatible with homotopies. Hence
$$
\Hom_{D(\mathcal D)}(Lf(K),L)=\Hom_{K(\mathcal D)}(f(P),I)=\Hom_{K(\mathcal C)}(P,g(I)).
$$
On the other side, by the calculus of fractions
$\Hom_{D(\mathcal C)}(K,Rg(L))=\colim_{s}\Hom_{K(\mathcal C)}(P',g(I))$. The colimit runs over
the quasi-isomorphisms $s\colon P'\to P$, and the K-flat $P'$ are cofinal among them,
since every complex has a K-flat resolution. For such $s$, the map
$\Hom_{K(\mathcal C)}(P,g(I))\to\Hom_{K(\mathcal C)}(P',g(I))$ is identified by the
adjunction with $\Hom_{K(\mathcal D)}(f(P),I)\to\Hom_{K(\mathcal D)}(f(P'),I)$. That map is
bijective, because $f(s)$ is a quasi-isomorphism by the hypothesis on $f$ and $I$ is
K-injective. So the colimit is $\Hom_{K(\mathcal C)}(P,g(I))$. The resulting bijection
$\Hom(Lf(K),L)\cong\Hom(K,Rg(L))$ is natural in $K$ and $L$, so $Lf\dashv Rg$.

*The categories of the table.* $\Sh(X_{\mathrm{proét}},\mathcal A)$ is a Grothendieck
abelian category, because the small pro-étale site [def-weil-pbc-proetale-site] is
essentially small. With the tensor product of [sk-def-sfb-sheaf-tensor] it is closed
symmetric monoidal. It has functorial flat resolutions when $\mathcal A$ does: the
sheafified free objects on representables, tensored with a flat separator of
$\mathcal A$, form a flat separator. Likewise $\Mod_{\Lambda_X}$ is a closed symmetric
monoidal Grothendieck abelian category with functorial flat resolutions
[sk-prop-sfb-module-category]. So in both cases right derived functors exist for every
additive functor, and left derived functors exist for every additive functor that
preserves K-flat quasi-isomorphisms.
