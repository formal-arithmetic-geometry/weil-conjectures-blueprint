+++
id = "theorem-trace-isomorphism-top-degree"
kind = "theorem"
title = "The trace isomorphism in top degree"
order = 866
lean = ["AlgebraicGeometry.Etale.TateOrientation.bijective_untwistedTraceMap", "AlgebraicGeometry.Etale.traceIsomorphism", "AlgebraicGeometry.WeilSheaf.subsingleton_cohomology_adicConstant", "AlgebraicGeometry.WeilSheaf.traceIsomorphism_adicConstant", "AlgebraicGeometry.ProEtale.subsingleton_H_continuousSheaf_of_profinite", "AlgebraicGeometry.ProEtale.subsingleton_H_continuousSheaf_of_two_mul_lt"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "proposition-proper-base-change-degree-zero", "definition-torsion-sheaves", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "definition-exceptional-base-change-finite", "theorem-smooth-base-change-classical-torsion", "lemma-kunneth-one-identity-factor", "definition-relative-dualizing-complex", "proposition-relative-dualizing-complex", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
Let $X/k$ be smooth, proper and connected of pure dimension
$d$, with $k$ algebraically closed. For every admissible
coefficient ring,

$$
H^i(X,\Lambda_X)=0\quad(i\notin[0,2d]),\qquad
H^0(X,\Lambda_X)=\Lambda,
$$

and the map

$$
\operatorname{tr}_X:H^{2d}(X,\Lambda_X)
\xrightarrow{\sim}\Lambda(-d),
$$

the twist by $(-d)$ of the map
$\operatorname{tr}_X(d):H^{2d}(X,\Lambda_X(d))\to\Lambda$ induced on
$H^{2d}$ by $\operatorname{Tr}_X$ of Definition [definition-trace-map],
is an isomorphism.
