+++
kind = "proof"
of = "lemma-change-coefficients-compact-support--1"
order = 637003
uses = ["definition-change-of-coefficients-maps", "lemma-change-coefficients-direct-image", "proposition-proper-direct-image-extension-zero", "proposition-inverting-ell", "proposition-comparison-etale-derived-category", "proposition-comparison-immersions", "proposition-composition-base-change-rf-shriek"]
+++
Write the chosen compactification as $f=p\circ j$.
Extension by zero preserves bounded constructible complexes, so the
comparison of Definition [definition-change-of-coefficients-maps](2)
restricts to these categories. For $\mathcal O_E\to E$, the
direct-image comparison is the adjoint transpose of the pullback
comparison. Proposition [proposition-inverting-ell] identifies extension
of scalars with rationalization on both sides; the adjunction bijection
on Hom groups remains a bijection after inverting $\ell$, so this
comparison is an isomorphism.

For $E\to\overline{\mathbf Q}_\ell$, restrict the direct-image
comparison of Lemma [lemma-change-coefficients-direct-image] for the
proper morphism $p$ to bounded constructible complexes. Its underlying
comparison is an isomorphism on bounded below complexes, and the
inclusion of the bounded constructible category is fully faithful.
In each case compose these two isomorphisms:
$$
(Rp_*j_!K)_{\Lambda'}\xrightarrow{\ \sim\ }
Rp_*\bigl((j_!K)_{\Lambda'}\bigr)
\xrightarrow{\ \sim\ }Rp_*j_!(K_{\Lambda'}).
$$
The construction is natural in $K$ and works for any specified
compactification; taking the chosen one gives the asserted isomorphism.

For reduction modulo $\ell^n$, first treat a proper morphism $p$.
Identify $Rp_!$ with $Rp_*$, use the invertible direct-image reduction
comparison, and compose with the finite-coefficient comparison between
the pro-étale and étale sites. For an open immersion $j$, take the
adjoint transpose of the reduction comparison for $j^!=j^*$.
It is invertible after restriction to the open subscheme, by full
faithfulness of extension by zero, and after restriction to its closed
complement, where both sides vanish. The localization triangle shows
that it is invertible. Finally compose the open and proper comparisons
for $c$ and transport them along the composition isomorphisms of
Proposition [proposition-composition-base-change-rf-shriek].
