+++
kind = "proof"
of = "theorem-global-verdier-duality"
order = 852
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "definition-torsion-sheaves", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "proposition-sp-unique-adjoint", "theorem-nagata-s-compactification-theorem", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
Both isomorphisms are the first two Verdier exchange formulas of
Corollary [corollary-verdier-exchange-formulas] for $f=a_X$, so we only have to recognize the Verdier dual on the point as the linear dual. On $s$ the dualizing complex is
$\Lambda_s$, so $\mathbb D_s=\cHom_s(-,\Lambda_s)$. Since $k$ is
algebraically closed, Lemma [lemma-perfect-complexes-geometric-point] identifies
$D^b_{\mathrm{ctf}}(s,\Lambda)$ with $\operatorname{Perf}(\Lambda)$. Under this identification, then, $\mathbb D_s$ becomes $R\!\operatorname{Hom}_\Lambda(-,\Lambda)$, and the two exchange
formulas read (10.5) and
(10.6). As for the pairing,
Lemma [lemma-internal-adjunction-two-exchange-formulas]
constructs the exchange formula (10.3) from
evaluation and the counit of $Rf_!\dashv f^!$. For $f=a_X$ it is therefore
the adjoint of the displayed pairing.
