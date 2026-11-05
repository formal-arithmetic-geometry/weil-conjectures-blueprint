+++
kind = "proof"
of = "lemma-cohomological-range-curve"
order = 1193
uses = ["proposition-etale-implications", "definition-w-local-w-strictly-local", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "proposition-integral-constructibility-criterion", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-direct-image-constructible-complexes", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "proposition-dctf-x-qbar-2-colimit", "proposition-sp-unique-adjoint", "lemma-degree-zero-top-cohomology", "lemma-finite-quasi-finite-direct-images", "theorem-nagata-s-compactification-theorem", "remark-base-change-compactification", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
Choose a dense open $j:U\hookrightarrow C$ on which $F$ is lisse,
and let $i$ be the inclusion of the finite complement. The sequence
$0\to j_!j^*F\to F\to i_*i^*F\to0$ gives a long exact sequence in
which $H^r_c(C,i_*i^*F)$ vanishes for $r\ne0$, because the support is
finite. It therefore suffices to show $H^r_c(U,j^*F)=0$ for
$r\notin\{0,1,2\}$. For $r<0$ there is nothing to prove, and for $r>2$,
degreewise Poincaré duality
(Corollary [corollary-degreewise-duality-over-fields], with $d=1$) shows
that $H^r_c(U,j^*F)$ is dual to $H^{2-r}(U,(j^*F)^\vee(1))$, which is
zero because $(j^*F)^\vee$ is a sheaf and $2-r<0$.
