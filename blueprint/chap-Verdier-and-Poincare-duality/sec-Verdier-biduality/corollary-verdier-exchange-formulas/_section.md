+++
id = "corollary-verdier-exchange-formulas"
kind = "corollary"
title = "Verdier exchange formulas"
order = 848
lean = ["AlgebraicGeometry.Etale.nonempty_iso_leftDerivedUpperStar_verdierDual", "AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_verdierDual", "AlgebraicGeometry.WeilComplex.nonempty_upperShriek_verdierDual_iso"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "definition-w-local-w-strictly-local", "example-locally-constant-functions-w-local", "lemma-extremally-disconnected-covers", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "definition-weak-contractibility", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "lemma-comparison-direct-images-compatibilities", "proposition-comparison-immersions", "proposition-locally-constant-sheaves-finite-presentation", "proposition-pro-etale-site-separably-closed", "lemma-comparison-completed-coefficients", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "proposition-integral-constructibility-criterion", "lemma-constructible-sheaves", "lemma-descent-finite-coefficient-field", "lemma-lattices-after-finite-stratification", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-base-change-complete-integral", "proposition-comparison-etale-derived-category", "lemma-structure-integral-constructible-complexes", "proposition-composition-open-restriction-compactifications-f", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "proposition-sp-unique-adjoint", "definition-verdier-dual-evaluation", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "definition-relative-picard-functor", "theorem-riemann-roch-coherent-serre-duality", "lemma-coherent-base-change-invertible-sheaves", "theorem-picard-scheme-jacobian-over-separably", "corollary-torsion-jacobian-field-extension", "lemma-finite-direct-images", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-finite-morphisms-cohomology"]
+++
For a morphism $f:X\to Y$ there are natural isomorphisms of functors on
[$D^b_{\mathrm{ctf}}(X,\Lambda)$](@definition-constructible-sheaves), respectively [$D^b_{\mathrm{ctf}}(Y,\Lambda)$](@definition-constructible-sheaves),

$$
\begin{aligned}
\href{@definition-verdier-dual-evaluation}{\mathbb D_Y}\href{@proposition-construction-independence-rf-shriek}{Rf_!}&\simeq Rf_*\href{@definition-verdier-dual-evaluation}{\mathbb D_X},&
\href{@definition-verdier-dual-evaluation}{\mathbb D_Y}Rf_*&\simeq \href{@proposition-construction-independence-rf-shriek}{Rf_!}\href{@definition-verdier-dual-evaluation}{\mathbb D_X},\\
\href{@definition-verdier-dual-evaluation}{\mathbb D_X}f^*&\simeq \href{@theorem-existence-exceptional-inverse-image}{f^!}\href{@definition-verdier-dual-evaluation}{\mathbb D_Y},&
\href{@definition-verdier-dual-evaluation}{\mathbb D_X}\href{@theorem-existence-exceptional-inverse-image}{f^!}&\simeq f^*\href{@definition-verdier-dual-evaluation}{\mathbb D_Y}.
\end{aligned}
$$

In particular, for an open $j:U\hookrightarrow X$ and a closed
$i:Z\hookrightarrow X$,

$$
\href{@definition-verdier-dual-evaluation}{\mathbb D_X}j_!\simeq Rj_*\href{@definition-verdier-dual-evaluation}{\mathbb D_U},\qquad
\href{@definition-verdier-dual-evaluation}{\mathbb D_X}Rj_*\simeq j_!\href{@definition-verdier-dual-evaluation}{\mathbb D_U},\qquad
i^*\href{@definition-verdier-dual-evaluation}{\mathbb D_X}\simeq\href{@definition-verdier-dual-evaluation}{\mathbb D_Z}\href{@theorem-existence-exceptional-inverse-image}{i^!}.
$$

The isomorphisms in the left column are (10.3)
and (10.4); those in the right column are
obtained from them by [biduality](@theorem-verdier-biduality), as displayed in the proof.
