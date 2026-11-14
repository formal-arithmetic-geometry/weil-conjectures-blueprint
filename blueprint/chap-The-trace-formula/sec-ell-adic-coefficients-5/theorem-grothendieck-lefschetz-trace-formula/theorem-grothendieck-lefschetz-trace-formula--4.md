+++
id = "theorem-grothendieck-lefschetz-trace-formula--4"
kind = "theorem"
title = "Trace formula: algebraically closed coefficients"
order = 1018008
aliases = ["bp-r311-4"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.weilTraceFormula"]
uses = ["definition-trace-function", "definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "lemma-stability--3", "lemma-stability--5", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "corollary-finite-quotients-their-transition-maps--3", "lemma-inverse-image-coefficient-sheaves--1", "lemma-constructible-sheaves--8", "lemma-integral-models--3", "lemma-inverse-image-tensor-product--3", "proposition-composition-base-change-rf-shriek--8", "proposition-six-operations-dctf--5", "proposition-six-operations-dctf--16", "proposition-sp-unique-adjoint--1", "definition-weil-structure--2", "definition-correspondence--3", "definition-compactification-refinement--1", "definition-compactification-refinement--3", "lemma-schematic-closure-uniqueness--1", "lemma-schematic-closure-uniqueness--2", "lemma-passing-schematic-closure--1", "lemma-passing-schematic-closure--2", "proposition-compactifying-union-two-opens--1", "lemma-affine-covers-dense-intersection--1", "lemma-affine-covers-dense-intersection--2"]
+++
For $K\in D^b_{\mathrm{ctf}}(X_{\mathrm{pro}\acute{e}t},\overline{\mathbf Q}_\ell)$ with the stated Weil structure and every $m\geq1$, one has in $\overline{\mathbf Q}_\ell$:

$$
\operatorname{tr}_{\overline{\mathbf Q}_\ell}
\bigl(\operatorname{Frob}_{X,K}^m\mid R\Gamma_c(X_{\mathrm{pro}\acute{e}t},K)\bigr)
=\sum_{y\in X_0(\mathbf F_{q^m})}
\operatorname{tr}_{\overline{\mathbf Q}_\ell}
\bigl(\operatorname{Frob}_{y,m}\mid K_{\bar y}\bigr).
$$
