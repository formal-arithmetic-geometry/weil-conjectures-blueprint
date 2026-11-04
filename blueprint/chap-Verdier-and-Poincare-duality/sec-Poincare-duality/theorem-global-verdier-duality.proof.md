+++
kind = "proof"
of = "theorem-global-verdier-duality"
order = 846
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-underived-base-change-map", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "definition-torsion-sheaves", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "proposition-pullback-multiplication-n", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "corollary-serre-duality-field-extension", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic"]
+++
Both isomorphisms are the first two Verdier exchange formulas of
Corollary [corollary-verdier-exchange-formulas] for $f=a_X$. We
only have to recognize the Verdier dual on the point as the
linear dual. On $s$ the dualizing complex is
$\Lambda_s$, so $\mathbb D_s=\cHom_s(-,\Lambda_s)$. Since $k$ is
algebraically closed, Lemma [lemma-perfect-complexes-geometric-point] identifies
$D^b_{\mathrm{ctf}}(s,\Lambda)$ with $\operatorname{Perf}(\Lambda)$. Under this identification
$\mathbb D_s$ becomes $R\!\operatorname{Hom}_\Lambda(-,\Lambda)$, and the two exchange
formulas read (10.5) and
(10.6). As for the pairing,
Lemma [lemma-internal-adjunction-two-exchange-formulas]
constructs the exchange formula (10.3) from
evaluation and the counit of $Rf_!\dashv f^!$. For $f=a_X$ it is therefore
the adjoint of the displayed pairing.
