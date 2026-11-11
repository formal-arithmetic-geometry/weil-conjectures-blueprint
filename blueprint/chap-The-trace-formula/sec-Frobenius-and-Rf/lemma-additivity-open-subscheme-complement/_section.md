+++
id = "lemma-additivity-open-subscheme-complement"
kind = "lemma"
title = "Additivity for an open subscheme and its complement"
order = 1003
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.CoefficientMorphism.closedPieceCoefficient", "AlgebraicGeometry.ProEtale.CondensedRing.CoefficientMorphism.openPieceCoefficient", "AlgebraicGeometry.ProEtale.CondensedRing.trace_compactPullback_comp_eq_add"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "lemma-inverse-image-coefficient-sheaves", "lemma-constructible-sheaves", "lemma-integral-models", "lemma-inverse-image-tensor-product", "proposition-six-operations-dctf", "definition-categorical-trace", "definition-frobenius-correspondences-their-operators", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
Let $j_0:U_0\hookrightarrow X_0$ be open with reduced closed
complement $i_0:Z_0\to X_0$, and let $K\in D^b_{\mathrm{ctf}}(X,A)$. A Frobenius
correspondence $\psi$ on $K$ induces Frobenius correspondences on
$j^*K$, $i^*K$, $j_!j^*K$ and $Ri_*i^*K$, whose stalk maps are the
restrictions of $\psi_m$. Writing $T_{c_m}$ also for the endomorphisms
of $R\Gamma_c$ induced by the Frobenius correspondences on $U$ and $Z$, for
every $m\geq1$

$$
\operatorname{tr}_A(T_{c_m}(\psi_m)\mid R\Gamma_c(X,K))
=\operatorname{tr}_A(T_{c_m}\mid R\Gamma_c(U,j^*K))
+\operatorname{tr}_A(T_{c_m}\mid R\Gamma_c(Z,i^*K)).
$$
