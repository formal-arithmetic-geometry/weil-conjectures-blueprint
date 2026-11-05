+++
id = "lemma-cohomology-projective-line-trace"
kind = "lemma"
title = "Cohomology of the projective line and the trace"
order = 546
lean = ["AlgebraicGeometry.ProEtale.geoP1Cohomology", "AlgebraicGeometry.ProEtale.geoP1DecompositionMap", "AlgebraicGeometry.ProEtale.geoP1Trace"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "proposition-pro-etale-affines-form-basis", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-pro-etale-base-change-map", "proposition-proper-base-change-degree-zero", "definition-torsion-sheaves", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
Let $\Lambda$ be a finite commutative $\ell$-primary ring, let $S$ be a
Noetherian scheme on which $\ell$ is invertible, and let
$p:\mathbf P^1_S\to S$ be the projection. The unit
$\Lambda_S\to Rp_*\Lambda_{\mathbf P^1_S}$ and the class
$c_1(\mathcal O_{\mathbf P^1_S}(1))$ define an isomorphism

$$
\sigma_S:\Lambda_S\oplus\Lambda_S(-1)[-2]
\ \xrightarrow{\ \sim\ }\ Rp_*\Lambda_{\mathbf P^1_S}
\quad\text{in }D^+(S_{\acute{e}t},\Lambda),
\tag{6.4}
$$

compatible with base change in the sense that for $g:S'\to S$ with $S'$
Noetherian, the base change map $g^*Rp_*\Lambda\to Rp'_*\Lambda$ carries $g^*\sigma_S$ to $\sigma_{S'}$. Let

$$
\operatorname{Tr}_p:Rp_*\Lambda_{\mathbf P^1_S}(1)[2]\longrightarrow\Lambda_S
\tag{6.5}
$$

be the morphism given by the projection
onto the summand $\Lambda_S$ of the twist of $\sigma_S$.
Then $\operatorname{Tr}_p$ is compatible with every Noetherian base
change.
