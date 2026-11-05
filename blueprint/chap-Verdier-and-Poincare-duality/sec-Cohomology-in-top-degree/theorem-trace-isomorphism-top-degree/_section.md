+++
id = "theorem-trace-isomorphism-top-degree"
kind = "theorem"
title = "The trace isomorphism in top degree"
order = 866
lean = ["AlgebraicGeometry.Etale.TateOrientation.bijective_untwistedTraceMap", "AlgebraicGeometry.Etale.traceIsomorphism", "AlgebraicGeometry.WeilSheaf.traceIsomorphism_adicConstant"]
uses = ["lemma-stability", "proposition-comparison-morphism-inverse-image", "lemma-inverse-image-coefficient-sheaves", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "definition-exceptional-base-change-finite", "proposition-adjunction-projective-line", "proposition-exceptional-inverse-image-smooth-morphism", "proposition-six-operations-change-coefficients", "lemma-degree-zero-calculation", "lemma-reduction-field", "lemma-reduction-curve-over-normal-base", "proposition-base-change-larger-algebraically-closed", "lemma-kunneth-field-coefficients", "definition-relative-dualizing-complex", "lemma-schematic-closure-uniqueness", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
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
