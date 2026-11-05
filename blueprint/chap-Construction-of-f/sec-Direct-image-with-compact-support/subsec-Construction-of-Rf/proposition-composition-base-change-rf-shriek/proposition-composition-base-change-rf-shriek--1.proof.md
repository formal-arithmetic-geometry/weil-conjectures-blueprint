+++
kind = "proof"
of = "proposition-composition-base-change-rf-shriek--1"
order = 516002
uses = ["proposition-construction-independence-rf-shriek", "proposition-proper-direct-image-constructible-complexes", "proposition-comparison-immersions", "theorem-nagata-s-compactification-theorem", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro"]
+++
For the pro-étale statement, choose compactifications $f=pj$ and $g=qj_Y$.
Compactify $j_Yp$ as $rj'$ with the square formed by $p,j',j_Y,r$ cartesian;
Lean obtains this from `AlgebraicGeometry.Compactification.exists_isPullback_overG_overI`.
Proper base change and base change for extension by zero give
$$
j_{Y!}Rp_*\simeq Rr_*j'_!.
$$
The exchange map is checked on the open and its closed complement: on the
open it is an isomorphism by proper base change, and on the complement both
sides vanish. Compose this exchange with the composition isomorphisms of
proper direct images and extensions by zero. Finally compare the resulting
compactification of $gf$ with the chosen one using
[proposition-construction-independence-rf-shriek]. The same construction
works for $\Oe$, using integral proper base change.

For the finite-coefficient étale statement, Lean uses a graph construction.
Let $V$ and $W$ be the proper parts of compactifications of $gf$ and $g$,
and form $P=V\times_ZW$. Embed $X$ properly in the open $P\times_VX$.
`AlgebraicGeometry.Etale.nonempty_iso_rightDerivedLowerShriekOfCompactification`
computes $R(gf)_!$ through this proper-open-proper factorization. The same
lemma computes $Rf_!$ over the open $P\times_WY$. Exchange extension by zero
with the proper pushforward $P\to W$, then compose the proper direct images
and the extensions by zero. This gives the required isomorphism without
assuming quasi-compactness of $f$ or $g$.
