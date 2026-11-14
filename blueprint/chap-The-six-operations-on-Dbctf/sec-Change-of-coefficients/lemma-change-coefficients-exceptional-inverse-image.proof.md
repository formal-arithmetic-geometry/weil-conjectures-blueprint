+++
kind = "proof"
of = "lemma-change-coefficients-exceptional-inverse-image"
order = 642
uses = ["proposition-etale-implications", "proposition-pro-etale-coverings", "definition-w-local-w-strictly-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-exact-products", "proposition-milnor-sequence", "theorem-classical-sheaves-essential-image", "theorem-bounded-below-cohomology-comparison", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "lemma-reduction-derived-nakayama", "lemma-flat-models-generators", "lemma-integral-models", "proposition-inverting-ell", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "lemma-naturality-pasting-comparison", "theorem-comparison-over-henselian-pair-degree", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-comparison-etale-derived-category", "proposition-construction-independence-rf-shriek", "proposition-composition-base-change-rf-shriek", "proposition-forgetting-supports-composition", "proposition-exceptional-inverse-image-smooth-morphism", "lemma-smooth-morphisms-locally-constant-sheaves", "corollary-open-direct-image-over-field", "theorem-f-shriek-finite-coefficients", "proposition-dctf-x-qbar-2-colimit", "proposition-sp-unique-adjoint", "definition-sp-scalar-extension", "definition-categorical-trace", "lemma-uniqueness-maps-dense-open", "definition-relative-picard-functor", "theorem-riemann-roch-coherent-serre-duality", "lemma-coherent-base-change-invertible-sheaves", "theorem-picard-scheme-jacobian-over-separably", "corollary-torsion-jacobian-field-extension", "lemma-finite-direct-images", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-finite-morphisms-cohomology"]
+++
Since $f^!$ is only known through its adjunction, there is no formula into
which we could substitute $K_{\Lambda'}$ directly. Instead we show that
$\beta_{f,K}$ is an isomorphism in two cases where $f^!$ has been computed:
closed immersions and the projection $\mathbf P^1_Y\to Y$. We then factor
a general $f$ locally into such maps, using that $\beta$ is compatible
with composition and with restriction to opens.

*Closed immersions.* For a closed immersion $i$ with open complement
$j$, the functor $i^!$ is determined by the localization triangle

$$
i_*i^!K\longrightarrow K\longrightarrow Rj_*j^*K.
$$

It expresses $i_*i^!K$ as the fibre of a map between objects whose
behaviour under extension of scalars we already know. Extension of scalars
commutes with $i_*$, $j^*$ and, by
Lemma [lemma-change-coefficients-direct-image], $Rj_*$. Hence the
extension of scalars of this triangle is the triangle for $K_{\Lambda'}$
over $\Lambda'$. Since the first map is the counit, the comparison on
fibres is $i_*\beta_{i,K}$. The comparisons on the other two terms are
isomorphisms, and therefore $i_*\beta_{i,K}$ is one as well. Since $i_*$
is fully faithful, $\beta_{i,K}$ is an isomorphism.

*The projective line.* Let $q:\mathbf P^1_Y\to Y$. Recall that the adjunction $Rq_*\dashv q^*(1)[2]$ between $D^b_{\mathrm{ctf}}(\mathbf P^1_Y,\Lambda)$ and
$D^b_{\mathrm{ctf}}(Y,\Lambda)$ is defined by the diagonal class and the trace. Through these two maps, $q^!$ is identified with $q^*(1)[2]$. It therefore
suffices to know that the two maps commute with all the maps of
coefficient rings listed above.
This holds by construction
(Propositions [proposition-adjunction-projective-line]
and [proposition-ell-adic-cycle-class-diagonal]). Indeed, the classes with finite coefficients are constructed from the Kummer sequence and derived
extension of scalars, while the integral classes are their compatible limits, and
the classes over fields are obtained from these by extension of scalars.
Only one map in the list needs a further remark. For $\mathcal O_E\to A$,
the proof of Lemma [lemma-change-coefficients-direct-image] shows that
$A_X$ is perfect. Hence the derived tensor product with $A_X$ commutes with
the inverse limits defining the integral classes, and so the resulting classes are exactly the classes with finite coefficients. Consequently the identification $q^!\simeq q^*(1)[2]$ is
compatible with extension of scalars. Under this identification, finally, $\beta_{q,K}$ becomes the isomorphism of
Definition [definition-change-of-coefficients-maps](1) for $q^*$,
twisted by $(1)[2]$.

*General $f$.* The open immersion
$\mathbf A^1_Y\hookrightarrow\mathbf P^1_Y$ is a case of restriction to
opens, and so $\beta$ is an isomorphism for $\mathbf A^1_Y\to Y$. Since the projection $\mathbf A^d_Y\to Y$ is a composite of $d$ projections of this kind, the compatibility of $\beta$ with composition gives the case of affine space. In general, whether $\beta_{f,K}$ is an isomorphism may be
checked locally on $X$. Using a finite affine cover, we may therefore
assume that $f$ factors as a closed immersion into an affine space over
$Y$ followed by the projection. Then the two cases already treated and
compatibility with composition give the claim.
