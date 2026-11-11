+++
id = "theorem-trace-formula-frobenius-correspondence"
kind = "theorem"
title = "Trace formula for a Frobenius correspondence"
order = 1007
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.traceFormulaHolds_of_isModelFrobenius", "AlgebraicGeometry.ProEtale.CondensedRing.trace_frobeniusCompactOperator_eq_sum"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "lemma-inverse-image-coefficient-sheaves", "lemma-constructible-sheaves", "lemma-integral-models", "lemma-inverse-image-tensor-product", "proposition-six-operations-dctf", "definition-categorical-trace", "definition-frobenius-correspondences-their-operators", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
Let $X_0/\mathbf F_q$ be separated and of finite type, put
$X=X_0\times_{\mathbf F_q}k$, let $A$ be any finite commutative
$\ell$-primary ring and $K\in D^b_{\mathrm{ctf}}(X,A)$, and let
$\psi:\Phi_X^*K\to K$ be any Frobenius correspondence on $K$. For every
$m\geq1$, in $A$,

$$
\operatorname{tr}_A(T_{c_m}(\psi_m)\mid R\Gamma_c(X_{\mathrm{pro}\acute{e}t},K))
=\sum_{x\in X_0(\mathbf F_{q^m})}
\operatorname{tr}_A(\psi_{m,\bar x}\mid K_{\bar x}).
$$
