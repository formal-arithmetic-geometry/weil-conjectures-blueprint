+++
kind = "proof"
of = "corollary-open-direct-image-over-field--2"
order = 585004
uses = ["theorem-smooth-base-change-classical-torsion", "theorem-proper-base-change-classical-pro", "theorem-comparison-direct-images", "lemma-naturality-pasting-comparison"]
+++
For sheaves, induct on $\dim Y+\dim T$. At a nonclosed point of $Y_T$,
at least one projection has nonclosed image. Pass to the strict
localization at that image and express it as a limit of schemes of
smaller dimension over a separably closed field. Smooth base change
(Theorem [theorem-smooth-base-change-classical-torsion]) and continuity
reduce the stalk calculation to the induction hypothesis. These are the
steps of `AlgebraicGeometry.Etale.openImmersionBaseChangeAtNonClosed_of_below`.

It remains to handle closed points. Work on products of affine opens
and compactify the second factor into a projective scheme of the same
dimension. After extension to a separable closure of $k$, the cone of
the base change map is supported on closed points. The Künneth formula
with one proper factor, obtained from proper base change
(Theorem [theorem-proper-base-change-classical-pro]) and the
projection formula, shows that its derived global sections vanish.
Detection for complexes supported on closed points makes the
cone zero. Restrict back to the affine opens and use étale locality.
This gives `AlgebraicGeometry.Etale.openImmersionBaseChangeAtMost_of_atNonClosed`
and completes the induction.

Choose a finite interval containing the cohomology of $L$. Apply the
sheaf assertion to every $H^q(L)$. The finite-range comparison
`AlgebraicGeometry.Etale.isIso_baseChange_app_of_isGE_of_isLE` then gives
the derived assertion: the base change map is an isomorphism on the
single-sheaf complexes, and truncation triangles give the result for $L$.

Finally, write $K\simeq\nu_X^*L$. Since $Y$ is noetherian, $j$ and $j_T$
are quasi-compact and quasi-separated. The comparison isomorphisms of
Theorem [theorem-comparison-direct-images] identify the source and target
of the pro-étale map with the inverse images of the étale source and
target. Lemma [lemma-naturality-pasting-comparison] identifies the maps
themselves. The étale isomorphism therefore gives the pro-étale
isomorphism, and naturality transports it along $K\simeq\nu_X^*L$.
