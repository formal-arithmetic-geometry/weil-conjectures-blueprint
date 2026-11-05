+++
kind = "proof"
of = "lemma-passing-schematic-closure--2"
order = 1412004
uses = ["lemma-passing-schematic-closure--1", "proposition-topos-functoriality", "proposition-proper-direct-image-constructible-complexes", "proposition-extension-zero-restriction-closed-subscheme"]
+++
Apply $Rp_*$ to the assumed isomorphism $\rho$ and compose with the
direct-image composition isomorphism:

$$
Rp_*j_!K\simeq Rp_*Rh_*j'_!K
\simeq R(p\circ h)_*j'_!K=Rq_*j'_!K.
$$

Lean constructs the composition isomorphism as the adjoint of the
pullback composition isomorphism, through
`AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerStarComp`
and its $E$- and $\mathcal O_E$-coefficient versions. This construction
does not require $p$, $q$, or $h$ to be proper once $\rho$ is invertible.

The alternative construction for $\Qbarl$ first inserts
$R(\mathrm{id}_X)_*\simeq\mathrm{id}$, then uses the assumed exchange
isomorphism, and finally the same composition isomorphism. For proper
$h$, the exchange map is invertible by proper base change and detection
on the open and closed complement, as in the proof of
[lemma-passing-schematic-closure--1]; the relevant declaration is
`AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleLowerStarOpenImmersionLowerShriekExchange'_padicAlgCl`.
When both comparisons are invertible, the two constructions agree by
`AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekRefinementIso_eq'`.
