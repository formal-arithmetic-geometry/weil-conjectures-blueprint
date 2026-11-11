+++
kind = "proof"
of = "lemma-restriction-geometric-generic-fibre"
order = 840
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "lemma-flat-models-generators", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-construction-independence-rf-shriek", "proposition-composition-base-change-rf-shriek", "proposition-forgetting-supports-composition", "theorem-generic-constructibility-base-change-rj", "corollary-open-direct-image-over-field", "proposition-sp-unique-adjoint", "definition-categorical-trace", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "definition-relative-picard-functor", "theorem-riemann-roch-coherent-serre-duality", "lemma-coherent-base-change-invertible-sheaves", "theorem-picard-scheme-jacobian-over-separably", "corollary-torsion-jacobian-field-extension", "lemma-finite-direct-images", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-finite-morphisms-cohomology"]
+++
We prove the comparisons in the order stated, each using the
previous ones: the direct image by continuity along a limit of étale
maps, $i^!$ by the localization triangle, and internal Hom by
dévissage to generators $t_!P$. Throughout, with finite coefficients
Proposition [proposition-comparison-etale-derived-category] lets us
compute $D^b_{\mathrm{ctf}}(X,A)$ and the direct images by their classical
étale counterparts.

*Direct image.* The geometric generic point is a limit of étale
$B$-schemes. Indeed, a separable closure of $k(B)$ is the inverse limit of
nonempty affine opens in the normalizations of $B$ in its finite separable
extensions, with the branch loci removed, and each stage is étale over
an open of $B$. The functor $Rh_*$ commutes with pullback to each stage,
because pullback to an étale $B$-scheme is restriction to an object of
the small site. It remains to pass to the limit.

Every affine object étale over the limit descends to a stage. Continuity
of cohomology (Corollary [corollary-continuity-cohomology]) therefore shows
that, degree by degree, the derived sections with finite coefficients
commute with this filtered limit along affine transition maps, provided the
complexes vanish below one fixed degree. They do, because $L$ is bounded.
Moreover, all the direct images lie in one fixed range of degrees. The base
changes of $h$ to the stages are of finite type of bounded dimension, and
[Stacks, [0F10](https://stacks.math.columbia.edu/tag/0F10)] bounds their $\ell$-cohomological dimensions
(Definition [definition-cohomological-dimension]) independently of the
stage. This proves the first comparison over the separable closure. It
also holds over the algebraic closure, since a purely inseparable extension
induces the same classical étale topos.

*Exceptional inverse image.* Let $j$ be the open complement of
$i$ and pull back

$$
i_*i^!M\longrightarrow M\longrightarrow Rj_*j^*M
\longrightarrow.
$$

We compare the pulled-back triangle with the triangle with closed support
on the generic fibre, whose first term is $i_{\bar\eta,*}i_{\bar\eta}^!g_X^*M$. Their second terms agree. The third terms agree too, because the first
comparison identifies the pullback of $Rj_*j^*M$ with
$Rj_{\bar\eta,*}j_{\bar\eta}^*g_X^*M$, and the map between them is the same.
It follows that the first terms are determined functorially. Indeed, there are no nonzero
maps, in any degree, from a complex supported on $Z_{\bar\eta}$ to one of the form
$Rj_{\bar\eta,*}N$, so the first term of each triangle is the fibre of the second map. Now pullback commutes with direct image along a closed immersion, so
the first term of the pulled-back triangle is $i_{\bar\eta,*}g_Z^*i^!M$. By construction, the induced map $i_{\bar\eta,*}g_Z^*i^!M\to i_{\bar\eta,*}i_{\bar\eta}^!g_X^*M$
is adjoint to the pulled-back counit, that is, it is $i_{\bar\eta,*}$ of our
comparison map, and it is an isomorphism. Since $i_{\bar\eta,*}$ is fully
faithful, the comparison map itself is an isomorphism.

*Internal Hom.* The complexes $K$ for which the comparison is an
isomorphism are closed under cones and shifts, because both sides are exact
functors of $K$. The dévissage of
Lemma [lemma-verdier-duality-preserves-constructibility] therefore
reduces us to $K=t_!P$,
where $t$ is the inclusion of a stratum and $P$ is locally perfect
on it. For these generators, internal adjunction and the dualizability of the locally perfect complex $P$ express internal Hom
through operations we have already compared:

$$
\cHom_X(t_!P,M)
\simeq Rt_*(P^\vee\otimes^{\mathbf L}t^!M).
$$

We check that $g^*$ commutes with each operation on the right. For $t^!$ we factor $t$ as a closed immersion followed by an open immersion: for the open immersion $t^!$ is restriction, which commutes with $g^*$, and for the closed immersion
we use the second comparison. Similarly, pullback commutes with $Rt_*$ by the first
comparison, and it commutes with tensor products and with $P^\vee$. The first two comparisons apply here, because by
Lemma [lemma-verdier-duality-preserves-constructibility]
all complexes used remain bounded constructible. Hence the comparison holds
for $K=t_!P$.
