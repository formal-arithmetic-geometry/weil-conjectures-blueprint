+++
id = "theorem-trace-formula-frobenius-correspondence"
kind = "theorem"
title = "Trace formula for a Frobenius correspondence"
order = 1007
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.traceFormulaHolds_of_isModelFrobenius", "AlgebraicGeometry.ProEtale.CondensedRing.trace_frobeniusCompactOperator_eq_sum"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "lemma-constructible-sheaves", "lemma-integral-models", "proposition-proper-direct-image-constructible-complexes", "lemma-inverse-image-tensor-product", "proposition-six-operations-dctf", "definition-categorical-trace", "definition-frobenius-correspondences-their-operators", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
Let $X_0/\mathbf F_q$ be separated and of finite type, put
$X=X_0\times_{\mathbf F_q}k$, let $A$ be any finite commutative
$\ell$-primary ring and $K\in \href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(X,A)}$, and let
$\psi:\Phi_X^*K\to K$ be any [Frobenius correspondence](@definition-frobenius-correspondences-their-operators) on $K$. For every
$m\geq1$, in $A$,

$$
\href{@definition-categorical-trace}{\operatorname{tr}_A}(\href{@definition-frobenius-correspondences-their-operators}{T_{c_m}(\psi_m)}\mid R\Gamma_c(\href{@definition-small-pro-etale-site}{X_{\mathrm{pro}\acute{e}t}},K))
=\sum_{x\in X_0(\mathbf F_{q^m})}
\href{@definition-categorical-trace}{\operatorname{tr}_A(\psi_{m,\bar x}\mid K_{\bar x})}.
$$
