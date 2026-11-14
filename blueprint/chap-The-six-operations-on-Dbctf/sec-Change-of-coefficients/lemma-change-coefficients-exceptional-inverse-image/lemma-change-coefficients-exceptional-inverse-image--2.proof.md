+++
kind = "proof"
of = "lemma-change-coefficients-exceptional-inverse-image--2"
order = 641005
uses = ["proposition-pro-etale-affines-form-basis", "definition-derived-base-change-map", "lemma-finite-cover-projective-space", "proposition-exceptional-inverse-image-smooth-morphism", "theorem-picard-scheme-jacobian-over-separably", "definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--2", "proposition-etale-implications--1", "lemma-stability--3", "lemma-stability--6", "lemma-stability--7", "lemma-stability--8", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--1", "definition-w-local-w-strictly-local--4", "theorem-existence-contractible-covers--1", "proposition-pro-etale-affines-form-basis--1", "proposition-pro-etale-affines-form-basis--2", "lemma-w-contractible-affines-projective--1", "definition-weak-contractibility--1", "proposition-comparison-morphism-inverse-image--2", "proposition-comparison-morphism-inverse-image--3", "theorem-classical-sheaves-essential-image--1", "theorem-bounded-below-cohomology-comparison--1", "theorem-bounded-below-cohomology-comparison--2", "proposition-comparison-immersions--1", "proposition-comparison-immersions--2", "proposition-locally-constant-sheaves-finite-presentation--3", "corollary-finite-quotients-their-transition-maps--3", "lemma-inverse-image-coefficient-sheaves--1", "definition-constructible-sheaves--5", "definition-constructible-sheaves--6", "lemma-integral-models--3", "definition-underived-base-change-map--1", "definition-derived-base-change-map--1", "lemma-identity-pasting--2", "definition-torsion-sheaves--1", "definition-torsion-sheaves--3", "lemma-acyclic-resolutions--1", "theorem-cohomology-curves--1", "theorem-cohomology-curves--2", "lemma-finiteness-small-etale-topoi--2", "proposition-proper-base-change-projective-line--1", "lemma-finite-morphisms--1", "lemma-finite-cover-projective-space--1", "theorem-proper-base-change-classical-pro--1", "theorem-proper-base-change-classical-pro--2", "corollary-cohomology-geometric-fibres--2", "proposition-comparison-etale-derived-category--5", "lemma-inverse-image-tensor-product--3", "proposition-construction-independence-rf-shriek--7", "proposition-construction-independence-rf-shriek--9", "proposition-composition-base-change-rf-shriek--7", "proposition-forgetting-supports-composition--3", "proposition-composition-open-restriction-compactifications-f--1", "proposition-composition-open-restriction-compactifications-f--4", "proposition-exceptional-inverse-image-smooth-morphism--4", "corollary-open-direct-image-over-field--1", "theorem-f-shriek-ell-adic-coefficients--4", "theorem-f-shriek-ell-adic-coefficients--6", "proposition-six-operations-dctf--3", "proposition-six-operations-dctf--16", "definition-change-of-coefficients-maps--1", "definition-change-of-coefficients-maps--5", "proposition-sp-unique-adjoint--1", "definition-sp-scalar-extension--2", "lemma-schematic-closure-uniqueness--2", "lemma-uniqueness-maps-dense-open--1", "definition-relative-picard-functor--2", "theorem-riemann-roch-coherent-serre-duality--6", "lemma-coherent-base-change-invertible-sheaves--1", "corollary-torsion-jacobian-field-extension--5", "lemma-finite-direct-images--1", "lemma-finite-direct-images--2", "lemma-cohomology-multiplicative-group--3", "lemma-cohomology-multiplicative-group--5", "lemma-cohomology-multiplicative-group--6", "proposition-p-torsion-smooth-proper-curve--1", "lemma-finite-morphisms-cohomology--2"]
+++
Assume $\Lambda=\mathcal O_E$ and $\Lambda'=A$ for a continuous map to a finite admissible ring (in particular $A=\mathcal O_E/\varpi^n$, where $\varpi=\pi_E$).

For closed immersions, use localization and clause [lemma-change-coefficients-direct-image--2]. On the projective line, $A_X$ is perfect over $\mathcal O_{E,X}$, so derived tensor with $A_X$ commutes with the inverse limits defining the integral diagonal class and trace. Their reductions are the finite classes. Apply the same local factorization.

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
