+++
kind = "proof"
of = "lemma-weight-bounds-partitions"
order = 1353
uses = ["proposition-etale-implications", "definition-w-local-w-strictly-local", "proposition-w-local-components", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "theorem-enough-affine-weakly-contractible-objects", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "proposition-integral-constructibility-criterion", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-direct-image-constructible-complexes", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "proposition-dctf-x-qbar-2-colimit", "proposition-sp-unique-adjoint", "proposition-weights-under-usual-operations", "lemma-finite-quasi-finite-direct-images", "lemma-weights-exact-sequence", "theorem-nagata-s-compactification-theorem", "remark-base-change-compactification", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
In both cases the restrictions of $K$ are again mixed of weights at
most $w$ (Proposition [proposition-weights-under-usual-operations]),
and we place $R^qf_!K$ in the middle of an exact sequence of Weil
sheaves whose outer terms are bounded.

For (1), applying $Rf_!$ and the composition isomorphism to the
triangle $j_!j^*K\to K\to i_*i^*K\to$ gives an exact sequence

$$
R^q(fj)_!j^*K\longrightarrow R^qf_!K\longrightarrow R^q(fi)_!i^*K,
$$

which is Frobenius-equivariant by naturality, and
Lemma [lemma-weights-exact-sequence] gives the bound for
$R^qf_!K$.

For (2), let $j':V_0\to Y_0$ and $i':W_0\to Y_0$ be the inclusions.
Base change for direct images with compact support
(Proposition [proposition-composition-base-change-rf-shriek])
identifies $j'^*R^qf_!K$ with $R^qf_{V!}(K|_{f^{-1}V_0})$ and
$i'^*R^qf_!K$ with $R^qf_{W!}(K|_{f^{-1}W_0})$. By
Lemma [lemma-finite-quasi-finite-direct-images], the outer terms of

$$
0\longrightarrow j'_!j'^*R^qf_!K\longrightarrow R^qf_!K
\longrightarrow i'_*i'^*R^qf_!K\longrightarrow0
$$

are mixed of weights at most $w+q$, and
Lemma [lemma-weights-exact-sequence] gives the bound for the
middle term.
