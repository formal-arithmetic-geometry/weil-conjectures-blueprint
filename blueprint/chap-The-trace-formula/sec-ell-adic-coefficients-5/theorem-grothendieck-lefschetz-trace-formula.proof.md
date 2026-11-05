+++
kind = "proof"
of = "theorem-grothendieck-lefschetz-trace-formula"
order = 1019
uses = ["proposition-etale-implications", "lemma-stability", "proposition-pro-etale-coverings", "definition-w-local-w-strictly-local", "proposition-w-local-components", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "theorem-enough-affine-weakly-contractible-objects", "definition-weak-contractibility", "proposition-milnor-sequence", "corollary-continuity-cohomology", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "theorem-comparison-direct-images", "proposition-comparison-immersions", "corollary-finite-quotients-their-transition-maps", "definition-tate-twists", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-flat-models-generators", "lemma-integral-models", "proposition-inverting-ell", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "definition-pro-etale-base-change-map", "lemma-naturality-pasting-comparison", "theorem-comparison-over-henselian-pair-degree", "proposition-proper-base-change-degree-zero", "definition-torsion-sheaves", "definition-torsion-pbc-property", "definition-injective-acyclicity", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "corollary-cohomology-geometric-fibres", "proposition-proper-direct-image-constructible-complexes", "lemma-proper-direct-image-unbounded-complexes", "proposition-composition-base-change-rf-shriek", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "proposition-exceptional-inverse-image-smooth-morphism", "lemma-coordinate-projections", "corollary-open-direct-image-over-field", "definition-change-of-coefficients-maps", "lemma-extension-scalars-preserves-dctf", "lemma-change-coefficients-direct-image", "proposition-dctf-x-qbar-2-colimit", "theorem-smooth-base-change-classical-torsion", "theorem-smooth-base-change-all-admissible", "lemma-base-change-along-product-projection", "lemma-kunneth-one-identity-factor", "definition-exceptional-base-change-map", "definition-relative-dualizing-complex", "proposition-relative-dualizing-complex", "proposition-sp-unique-adjoint", "lemma-perfect-complexes-geometric-point", "definition-verdier-dual-evaluation", "lemma-internal-adjunction-two-exchange-formulas", "lemma-double-dual-geometric-generic-fibre", "corollary-verdier-exchange-formulas", "definition-categorical-trace", "proposition-properties-trace", "definition-pushforward-correspondence", "definition-frobenius-correspondences-their-operators", "lemma-frobenius-fixed-scheme", "lemma-vanishing-restrictions-after-blowing-up", "proposition-integral-trace-formula", "corollary-trace-functions-direct-image-compact", "theorem-nagata-s-compactification-theorem", "lemma-uniqueness-maps-dense-open", "lemma-passing-schematic-closure", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "proposition-pullback-multiplication-n", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "corollary-serre-duality-field-extension", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "lemma-cohomology-multiplicative-group", "proposition-p-torsion-smooth-proper-curve", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
In each case we turn the Weil structure into a Frobenius correspondence
by composing with $\kappa_1$, and we use
Lemma [lemma-scheme-frobenius-geometric-frobenius] to see that this does not change
the operators. We then treat the coefficient rings in the order
finite, integral, rational, algebraic, each case using the
previous one.

For finite $A$, we apply Theorem [theorem-trace-formula-frobenius-correspondence]
to $\psi=\phi\kappa_1$. Then Lemma [lemma-scheme-frobenius-geometric-frobenius] identifies $T_{c_m}(\psi_m)$ with $\operatorname{Frob}_{X,K}^m$ and, at each fixed
point, $\psi_{m,\bar y}$ with $\operatorname{Frob}_{y,m}$. Similarly, for $\mathcal O_E$, composing the Weil structure with
$\kappa_1$ we get a
Frobenius correspondence $\Phi_X^*K\to K$. By the integral form of
Lemma [lemma-scheme-frobenius-geometric-frobenius], the endomorphisms it induces on $R\Gamma_c$ and on the stalks
are those induced by the Weil structure. The identity therefore follows from
Proposition [proposition-integral-trace-formula]. In particular, taking $E=\mathbf Q_\ell$ gives the case of $\mathbf Z_\ell$.

For coefficients $E$, the Weil structure composed with $\kappa_1$ is a
Frobenius correspondence $\psi_E$, and by the rational form of
Lemma [lemma-scheme-frobenius-geometric-frobenius] the endomorphisms it induces on $R\Gamma_c$ and on the stalks
are those induced by the Weil structure. We apply
Lemma [lemma-integral-models-rational-frobenius-correspondences] to $\psi_E$, apply (12.1) to $(K_0,\theta)$,
extend scalars to $E$, and multiply by $\pi_E^{-Nm}$. By linearity of
categorical traces and their compatibility with extension of scalars
(Proposition [proposition-properties-trace]), together with
(12.2), this gives the identity for every $m$.
The case $E=\mathbf Q_\ell$ gives the case of $\mathbf Q_\ell$.

For $\overline{\mathbf Q}_\ell$, complexes and morphisms are colimits of their versions over
finite extensions, so it is enough to find the Weil complex over some
finite $E$ and to check that the answer does not depend on the choice.
By Proposition [proposition-dctf-x-qbar-2-colimit] the complex $K$, its
Weil structure $\phi$ and $\phi^{-1}$ descend to a common finite extension
$E/\mathbf Q_\ell$. After a further finite extension the two identities saying
that these maps are inverse to each other hold as well. Thus we get a
Weil complex at a finite stage, and by extension
of scalars its formula over $E$ gives (12.3). If we
choose another representative, any isomorphism compatible with the Weil structures descends to a common finite extension, so the resulting
operators are conjugate. Since the trace is compatible with extension of scalars and invariant under conjugation, the result does not depend
on the stage or on the representative.

The complexes are perfect by Lemma [lemma-perfect-complexes-geometric-point]. Compatibility
with the change-of-coefficients maps holds because the pullbacks, the
endomorphisms $T_{c_m}$ and the iterated Frobenius correspondences commute with the
comparisons of Proposition [proposition-six-operations-change-coefficients]. Finally, over a field
the categorical trace is the alternating trace on cohomology by
Proposition [proposition-properties-trace], and this proves
(12.4).
