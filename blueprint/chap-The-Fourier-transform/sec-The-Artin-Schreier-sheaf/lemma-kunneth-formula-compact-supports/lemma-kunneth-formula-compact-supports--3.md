+++
id = "lemma-kunneth-formula-compact-supports--3"
kind = "lemma"
title = "Projection formula for compact supports"
order = 1225005
aliases = ["bp-r377-3"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleExceptionalProjectionMorphism"]
uses = ["definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--2", "definition-ind-etale-pro-etale-weakly--3", "proposition-etale-implications--1", "lemma-stability--4", "lemma-stability--6", "lemma-stability--7", "definition-small-pro-etale-site--1", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--1", "proposition-topos-functoriality--2", "definition-w-local-w-strictly-local--2", "definition-w-local-w-strictly-local--3", "definition-w-local-w-strictly-local--4", "proposition-w-local-components--1", "example-locally-constant-functions-w-local--1", "proposition-splitting-ind-etale-covers--1", "theorem-existence-contractible-covers--1", "proposition-pro-etale-affines-form-basis--2", "lemma-w-contractible-affines-projective--1", "definition-weak-contractibility--1", "corollary-evaluation-weakly-contractible-objects--1", "proposition-comparison-morphism-inverse-image--2", "theorem-classical-sheaves-essential-image--1", "lemma-acyclicity-pulled-back-injectives--1", "theorem-bounded-below-cohomology-comparison--1", "theorem-bounded-below-cohomology-comparison--2", "theorem-comparison-direct-images--1", "proposition-comparison-immersions--1", "proposition-locally-constant-sheaves-finite-presentation--3", "proposition-pro-etale-site-separably-closed--3", "corollary-finite-quotients-their-transition-maps--3", "lemma-inverse-image-coefficient-sheaves--1", "definition-derived-adic-completeness--1", "definition-constructible-sheaves--1", "definition-constructible-sheaves--2", "definition-constructible-sheaves--4", "definition-constructible-sheaves--5", "definition-constructible-sheaves--6", "definition-lisse-sheaves--1", "proposition-integral-constructibility-criterion--1", "lemma-constructible-sheaves--8", "lemma-lattices-after-finite-stratification--1", "definition-underived-base-change-map--1", "definition-derived-base-change-map--1", "definition-torsion-sheaves--1", "definition-torsion-sheaves--3", "definition-torsion-pbc-property--1", "theorem-cohomology-curves--1", "theorem-cohomology-curves--2", "proposition-proper-base-change-projective-line--1", "lemma-finite-morphisms--1", "lemma-finite-cover-projective-space--1", "proposition-proper-base-change-etale-site--1", "corollary-cohomology-geometric-fibres--2", "proposition-proper-base-change-complete-integral--1", "proposition-comparison-etale-derived-category--5", "proposition-comparison-etale-derived-category--6", "lemma-inverse-image-tensor-product--1", "lemma-inverse-image-tensor-product--3", "lemma-inverse-image-tensor-product--4", "lemma-inverse-image-tensor-product--6", "corollary-open-direct-image-over-field--1", "definition-change-of-coefficients-maps--6", "proposition-six-operations-change-coefficients--1", "proposition-six-operations-change-coefficients--23", "proposition-dctf-x-qbar-2-colimit--2", "proposition-sp-unique-adjoint--1", "definition-compactification-refinement--1", "lemma-schematic-closure-uniqueness--1", "lemma-uniqueness-maps-dense-open--1", "definition-admissible-blow-up--1", "theorem-extension-partial-section--1", "theorem-elimination-indeterminacy--1", "lemma-extending-graph-from-compactification--1", "lemma-separation-closures--1", "lemma-extending-isomorphism-over-closure-closed--1", "lemma-gluing-after-admissible-blow-ups--1", "lemma-affine-covers-dense-intersection--1", "theorem-chow-s-lemma-projective-form--2", "theorem-riemann-roch-coherent-serre-duality--6", "lemma-coherent-base-change-invertible-sheaves--1", "corollary-degree-jacobian--1", "corollary-torsion-jacobian-field-extension--5", "lemma-finite-direct-images--1", "lemma-finite-direct-images--2", "lemma-cohomology-multiplicative-group--5", "lemma-cohomology-multiplicative-group--6", "proposition-p-torsion-smooth-proper-curve--1", "lemma-finite-morphisms-cohomology--2"]
+++
Let $k$ be a field of characteristic $p>0$, let $\ell\ne p$ be a prime,
and let $E$ be a field that is an admissible coefficient ring, for instance $\overline{\mathbf Q}_\ell$. Let $a:U\to V$ be a morphism of
separated schemes of finite type over $k$. For bounded constructible
$E$-complexes $A$ on $U$ and $B$ on $V$, the exceptional projection map

$$
Ra_!A\otimes B\longrightarrow Ra_!(A\otimes a^*B)
$$

is an isomorphism. Taking $a=f$, $A=K$ and $B=Rg_!L$, its inverse gives

$$
Rf_!(K\otimes f^*Rg_!L)\simeq Rf_!K\otimes Rg_!L.
$$

Taking $a=p_1$, $A=p_2^*L$ and $B=K$ instead, and using the symmetry
of the tensor product, gives

$$
Rp_{1!}(p_1^*K\otimes p_2^*L)\simeq K\otimes Rp_{1!}p_2^*L.
$$

The composite

$$
Rh_!(p_1^*K\otimes p_2^*L)
\simeq Rf_!(K\otimes Rp_{1!}p_2^*L)
\simeq Rf_!(K\otimes f^*Rg_!L)
\simeq Rf_!K\otimes Rg_!L
$$

of the projection formula for $p_1$, the base change isomorphism of
[lemma-kunneth-formula-compact-supports--2] and the projection formula
for $f$ is called the *Künneth isomorphism*
$Rh_!(K\boxtimes_SL)\simeq Rf_!K\otimes Rg_!L$.
