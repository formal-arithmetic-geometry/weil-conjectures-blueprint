+++
kind = "proof"
of = "lemma-restriction-geometric-generic-fibre--1"
order = 839002
+++
*Direct image.* The geometric generic point is a limit of étale
$B$-schemes. Indeed, a separable closure of $k(B)$ is the inverse limit of
nonempty affine opens in the normalizations of $B$ in its finite separable
extensions, with the branch loci removed, and each stage is étale over
an open of $B$. The functor $Rh_*$ commutes with pullback to each stage,
because pullback to an étale $B$-scheme is restriction to an object of
the small site. It remains to pass to the limit.

Every affine object étale over the limit descends to a stage. Continuity
of cohomology (Corollary [corollary-continuity-cohomology]) therefore shows
that, degree by degree, the derived sections with finite coefficients
commute with this filtered limit along affine transition maps, provided the
complexes vanish below one fixed degree. They do, because $L$ is bounded.
Moreover, all the direct images lie in one fixed range of degrees. The base
changes of $h$ to the stages are of finite type of bounded dimension, and
[Stacks, [0F10](https://stacks.math.columbia.edu/tag/0F10)] bounds their $\ell$-cohomological dimensions
(Definition [definition-cohomological-dimension]) independently of the
stage. This proves the first comparison over the separable closure. It
also holds over the algebraic closure, since a purely inseparable extension
induces the same classical étale topos.

*Source:* the proof of Lemma [lemma-restriction-geometric-generic-fibre].
