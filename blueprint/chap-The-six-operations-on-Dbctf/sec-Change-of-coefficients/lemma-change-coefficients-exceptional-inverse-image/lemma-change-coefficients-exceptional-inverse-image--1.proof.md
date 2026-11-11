+++
kind = "proof"
of = "lemma-change-coefficients-exceptional-inverse-image--1"
order = 641003
uses = ["definition-derived-base-change-map", "proposition-exceptional-inverse-image-smooth-morphism", "theorem-f-shriek-finite-coefficients", "definition-small-pro-etale-site--1", "definition-constructible-sheaves--5", "lemma-flat-models-generators--1", "definition-underived-base-change-map--1", "definition-derived-base-change-map--1", "lemma-identity-pasting--2", "theorem-comparison-over-henselian-pair-degree--1", "definition-torsion-sheaves--1", "definition-torsion-sheaves--3", "lemma-acyclic-resolutions--1", "theorem-cohomology-curves--1", "theorem-cohomology-curves--2", "lemma-finiteness-small-etale-topoi--2", "proposition-proper-base-change-projective-line--1", "theorem-proper-base-change-classical-pro--1", "theorem-proper-base-change-classical-pro--2", "proposition-construction-independence-rf-shriek--7", "proposition-forgetting-supports-composition--1", "proposition-forgetting-supports-composition--3", "proposition-composition-open-restriction-compactifications-f--1", "proposition-exceptional-inverse-image-smooth-morphism--4", "lemma-smooth-morphisms-locally-constant-sheaves--2", "proposition-sp-unique-adjoint--1", "definition-categorical-trace--1", "definition-compactification-refinement--3", "lemma-schematic-closure-uniqueness--1", "lemma-schematic-closure-uniqueness--2", "proposition-compactifying-union-two-opens--1", "lemma-affine-covers-dense-intersection--1", "lemma-affine-covers-dense-intersection--2", "definition-relative-picard-functor--2", "lemma-finite-direct-images--1", "lemma-finite-direct-images--2", "lemma-finite-morphisms-cohomology--2"]
+++
Assume $\Lambda=A$, $\Lambda'=B$ for a homomorphism of finite admissible rings.

For closed immersions, use localization and the finite-coefficient clause of Lemma [lemma-change-coefficients-direct-image]. On the projective line, the Kummer classes and trace commute with derived extension of scalars. The local factorization in the original proof gives general $f$.

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

*The projective line.* Let $q:\mathbf P^1_Y\to Y$. The adjunction
$Rq_*\dashv q^*(1)[2]$ between $D^b_{\mathrm{ctf}}(\mathbf P^1_Y,\Lambda)$ and
$D^b_{\mathrm{ctf}}(Y,\Lambda)$ is defined by the diagonal class and the trace. Through
these two maps, $q^!$ is identified with $q^*(1)[2]$. It therefore
suffices to know that the two maps commute with all the maps of
coefficient rings listed above.
This holds by construction
(Propositions [proposition-adjunction-projective-line]
and [proposition-ell-adic-cycle-class-diagonal]). The classes with
finite coefficients are constructed from the Kummer sequence and derived
extension of scalars. The integral classes are their compatible limits, and
the classes over fields are obtained from these by extension of scalars.
Only one map in the list needs a further remark. For $\mathcal O_E\to A$,
the proof of Lemma [lemma-change-coefficients-direct-image] shows that
$A_X$ is perfect. Hence the derived tensor product with $A_X$ commutes with
the inverse limits defining the integral classes. The resulting classes
are exactly the classes with finite coefficients. Hence the identification $q^!\simeq q^*(1)[2]$ is
compatible with extension of scalars. Under this identification
$\beta_{q,K}$ becomes the isomorphism of
Definition [definition-change-of-coefficients-maps](1) for $q^*$,
twisted by $(1)[2]$.

*General $f$.* The open immersion
$\mathbf A^1_Y\hookrightarrow\mathbf P^1_Y$ is a case of restriction to
opens, and so $\beta$ is an isomorphism for $\mathbf A^1_Y\to Y$. The
projection $\mathbf A^d_Y\to Y$ is a composite of $d$ projections of this
kind. The compatibility of $\beta$ with composition gives the case of
affine space. In general, whether $\beta_{f,K}$ is an isomorphism may be
checked locally on $X$. Using a finite affine cover, we may therefore
assume that $f$ factors as a closed immersion into an affine space over
$Y$ followed by the projection. Then the two cases already treated and
compatibility with composition give the claim.

*Source:* the proof of Lemma [lemma-change-coefficients-exceptional-inverse-image].
