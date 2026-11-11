+++
id = "lemma-internal-adjunction-two-exchange-formulas"
kind = "lemma"
title = "Internal adjunction and two exchange formulas"
order = 830
lean = ["AlgebraicGeometry.Etale.nonempty_iso_verdierDual_leftDerivedUpperStar"]
uses = ["proposition-etale-implications", "lemma-stability", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "proposition-comparison-morphism-inverse-image", "lemma-acyclicity-pulled-back-injectives", "lemma-comparison-direct-images-compatibilities", "proposition-locally-constant-sheaves-finite-presentation", "theorem-comparison-constructible-sheaves", "proposition-pro-etale-site-separably-closed", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "proposition-composition-open-restriction-compactifications-f", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "definition-change-of-coefficients-maps", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "definition-relative-dualizing-complex", "definition-verdier-dual-evaluation", "lemma-schematic-closure-uniqueness", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
Let $f:X\to Y$ be a morphism, $K\in D^b_{\mathrm{ctf}}(X,\Lambda)$ and
$L\in D^b_{\mathrm{ctf}}(Y,\Lambda)$. The map
(10.1) and the two maps derived from it
and defined above are isomorphisms

$$
\begin{align}
\cHom_Y(Rf_!K,L)&\simeq
Rf_*\cHom_X(K,f^!L),\tag{10.2}\\
e_K:\mathbb D_YRf_!K&\xrightarrow{\ \sim\ } Rf_*\mathbb D_XK,
\tag{10.3}\\
f^!\mathbb D_YL&\simeq\mathbb D_Xf^*L.
\tag{10.4}\end{align}
$$

If $f$ is proper, then the composite

$$
Rf_*K\xrightarrow{Rf_*\delta_K}Rf_*\mathbb D_X\mathbb D_XK
\simeq\mathbb D_YRf_*\mathbb D_XK
$$

of $Rf_*\delta_K$ and $e_{\mathbb D_XK}$
equals the composite

$$
Rf_*K\xrightarrow{\delta_{Rf_*K}}\mathbb D_Y\mathbb D_YRf_*K
\simeq\mathbb D_YRf_*\mathbb D_XK
$$

of $\delta_{Rf_*K}$ and $\mathbb D_Y$ applied to
$e_K$.
