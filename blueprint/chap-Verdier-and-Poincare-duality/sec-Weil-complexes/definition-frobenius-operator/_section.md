+++
id = "definition-frobenius-operator"
kind = "definition"
title = "Frobenius operator"
order = 878
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.WeilBoundedConstructible.compactFrobenius", "AlgebraicGeometry.ProEtale.compactFrobenius"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "proposition-w-local-components", "example-locally-constant-functions-w-local", "theorem-pro-etale-refinements-weakly-etale", "lemma-inverse-image-coefficient-sheaves", "lemma-constructible-sheaves", "lemma-integral-models", "definition-pro-etale-base-change-map", "lemma-inverse-image-tensor-product", "proposition-construction-independence-rf-shriek", "proposition-composition-base-change-rf-shriek", "proposition-six-operations-dctf", "proposition-sp-unique-adjoint", "definition-weil-structure", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
For a Weil complex $(K,\phi_K)$ on $T$, the *geometric Frobenius
operator* on compactly supported cohomology is the endomorphism

$$
\begin{gathered}
\operatorname{Frob}_{T,K}:R\Gamma_c(T_{\mathrm{pro}\acute{e}t},K)
\xrightarrow{\ \operatorname{pb}_{\operatorname{Fr}_T}\ }
R\Gamma_c(T_{\mathrm{pro}\acute{e}t},\operatorname{Fr}_T^*K)\\
\xrightarrow{\ R\Gamma_c(T_{\mathrm{pro}\acute{e}t},\phi_K)\ }
R\Gamma_c(T_{\mathrm{pro}\acute{e}t},K).
\end{gathered}
$$

Here $\operatorname{pb}_{\operatorname{Fr}_T}$ is the pullback along $\operatorname{Fr}_T$
constructed above.
