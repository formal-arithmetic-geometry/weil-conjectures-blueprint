+++
kind = "proof"
of = "theorem-global-verdier-duality"
order = 853
uses = ["lemma-stability", "proposition-comparison-morphism-inverse-image", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "proposition-composition-open-restriction-compactifications-f", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
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
