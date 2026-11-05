+++
kind = "proof"
of = "lemma-finite-morphisms-cohomology--2"
order = 1594005
uses = ["lemma-finite-morphisms"]
+++
It suffices to check the map at geometric points $\bar c'$ of $C'$
with algebraically closed residue field. The base change $h'$ is
finite, so the stalk formula of [lemma-finite-morphisms] applies to
both $h$ and $h'$. The geometric fibres over $a\bar c'$ and $\bar c'$
are in bijection, and pullback identifies each stalk of $b^*G$ with
the corresponding stalk of $G$.

Under these identifications the base change map is the reindexing of
the finite product of stalks. Compatibility with each projection is
`AlgebraicGeometry.Etale.sheafFiber_map_baseChangeMap_app_stalkRestrict`;
the reindexing is supplied by
`AlgebraicGeometry.Scheme.Hom.GeometricFiber.baseChangeEquiv`.
Thus the map is an isomorphism on every such stalk, and these stalks
jointly detect isomorphisms. Applying this to every $G$ proves that
the natural transformation itself is an isomorphism.
