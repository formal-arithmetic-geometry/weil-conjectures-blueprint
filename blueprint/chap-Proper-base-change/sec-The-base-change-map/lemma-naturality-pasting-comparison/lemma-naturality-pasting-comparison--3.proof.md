+++
kind = "proof"
of = "lemma-naturality-pasting-comparison--3"
order = 324005
uses = ["definition-derived-base-change-map", "definition-pro-etale-base-change-map", "theorem-comparison-direct-images", "lemma-comparison-direct-images-compatibilities", "proposition-topos-functoriality", "proposition-comparison-morphism-inverse-image"]
+++
Both base change maps are mates of the corresponding square
isomorphisms of inverse images. The direct image comparisons are
compatible with the counits, as in
[lemma-comparison-direct-images-compatibilities](2), after passing from
bounded below to unbounded derived categories.

The inverse image comparisons also commute with the square
isomorphisms. On sheaves, this follows from the canonical identifications
of iterated fibre products and the pullback universal property. Passing
to complexes and then to derived categories preserves this equality.

Apply the adjunction for $f'$ to the proposed equality of exchange
maps. Precompose with the inverse image comparison for $f'$ at
$g_{\acute{e}t}^*Rf_{\acute{e}t,*}K$, which is an isomorphism.
Naturality and the counit compatibility for $f'$ turn the first mate
into its defining square isomorphism followed by a counit. The
compatibility of the square isomorphisms then identifies the two
inverse image paths, and the counit compatibility for $f$ gives the
remaining equality. Injectivity of the adjunction bijection proves the
claim. The definitions of $\alpha_K$ and $\beta_K$ identify this mate
identity with the displayed formula.
