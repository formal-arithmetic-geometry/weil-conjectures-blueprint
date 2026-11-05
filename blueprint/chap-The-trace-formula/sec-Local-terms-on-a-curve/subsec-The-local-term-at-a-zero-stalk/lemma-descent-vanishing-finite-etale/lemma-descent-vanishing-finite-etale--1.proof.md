+++
kind = "proof"
of = "lemma-descent-vanishing-finite-etale--1"
order = 986003
uses = ["lemma-finite-morphisms"]
+++
For a finite étale morphism, the functor $f_*$ is both a right adjoint
and a left adjoint of $f^{-1}$, hence is exact. Let $\eta$ be the unit
of $f^{-1}\dashv f_*$ and let $\tau:f_*f^{-1}\to\operatorname{id}$ be
the counit of $f_*\dashv f^{-1}$. The finite-stalk formula of
[lemma-finite-morphisms] identifies $\eta$ with the diagonal map and
$\tau$ with summation over the geometric fibre. Their composite is
therefore multiplication by $n$, as in
`AlgebraicGeometry.Etale.unit_app_comp_lowerStarUpperStarAdjunctionOfIsFinite_counit_app`.

Under $\Gamma(W',f^{-1}\mathcal F)\simeq
\Gamma(W,f_*f^{-1}\mathcal F)$, pullback on sections is the map induced
by $\eta$. Exactness allows $\tau$ to be applied termwise and passed to
the derived category. The trace on derived global sections is the
composite

$$
R\Gamma(W',f^{-1}L)\longrightarrow
R\Gamma(W,f_*f^{-1}L)\xrightarrow{R\Gamma(\tau)}R\Gamma(W,L),
$$

where the first arrow is the derived pullback along the exact functor
$f_*$. The composition rule for derived pullback and
`CategoryTheory.Functor.rightDerivedPullback_app_comp_map_mapDerivedCategoryToId_app`
carry the identity $\tau\circ\eta=n\,\operatorname{id}$ to this
composite. Finally, transport the trace through the natural
isomorphisms between global sections and sections over the terminal
étale objects. Compatibility of these isomorphisms with pullback gives
the assertion for restriction of derived sections.
