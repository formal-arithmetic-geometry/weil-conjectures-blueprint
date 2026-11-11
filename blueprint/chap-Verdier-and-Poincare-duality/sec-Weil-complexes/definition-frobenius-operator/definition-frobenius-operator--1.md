+++
id = "definition-frobenius-operator--1"
kind = "definition"
title = "Frobenius operator (1)"
name_showing = false
order = 878001
aliases = ["bp-r264-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.WeilBoundedConstructible.compactFrobenius", "AlgebraicGeometry.ProEtale.compactFrobenius"]
uses = ["definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--3", "proposition-etale-implications--1", "lemma-stability--1", "lemma-stability--2", "lemma-stability--3", "lemma-stability--5", "lemma-stability--6", "lemma-stability--7", "lemma-stability--8", "definition-small-pro-etale-site--1", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--2", "definition-w-local-w-strictly-local--2", "definition-w-local-w-strictly-local--3", "proposition-w-local-components--1", "example-locally-constant-functions-w-local--1", "theorem-pro-etale-refinements-weakly-etale--1", "lemma-inverse-image-coefficient-sheaves--1", "lemma-constructible-sheaves--8", "lemma-integral-models--3", "definition-pro-etale-base-change-map--1", "lemma-inverse-image-tensor-product--3", "proposition-construction-independence-rf-shriek--9", "proposition-composition-base-change-rf-shriek--7", "proposition-composition-base-change-rf-shriek--8", "proposition-six-operations-dctf--5", "proposition-six-operations-dctf--16", "proposition-sp-unique-adjoint--1", "definition-weil-structure--2", "definition-compactification-refinement--1", "definition-compactification-refinement--3", "lemma-schematic-closure-uniqueness--1", "lemma-schematic-closure-uniqueness--2", "lemma-passing-schematic-closure--1", "lemma-passing-schematic-closure--2", "proposition-compactifying-union-two-opens--1", "lemma-affine-covers-dense-intersection--1", "lemma-affine-covers-dense-intersection--2"]
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
