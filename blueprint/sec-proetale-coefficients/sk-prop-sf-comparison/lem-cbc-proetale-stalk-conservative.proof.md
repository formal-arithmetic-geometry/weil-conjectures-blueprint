+++
kind  = "proof"
of    = "lem-cbc-proetale-stalk-conservative"
+++
*Step 1 (clause (1)).* For a weakly etale $g_i$, the inverse image $g_i^*$ is
restriction to the slice of $T_{\Proet}$ over $W_i$
([lem-weil-pbc-proetale-restriction-injectives]). A morphism of sheaves is an
isomorphism as soon as its restrictions to the slices over the members of a
family covering the final object are isomorphisms: bijectivity on sections
over an object $V$ follows from the sheaf condition for the covering
$\{V\times_TW_i\to V\}$, on whose members the morphism is bijective. The
converse is functoriality. A sheaf vanishes if and only if its map to $0$ is
an isomorphism. Inverse image along $g_i$ is exact, so it commutes with
cohomology sheaves of complexes, and a morphism of complexes is a
quasi-isomorphism if and only if it induces isomorphisms on all cohomology
sheaves; apply the sheaf statement to these.

*Step 2 (clause (2)).* The affine pro-etale objects form a dense subsite of
$T_{\Proet}$: every object is covered by them ([lem-weil-pbc-ind-etale-basis],
applied over the affine opens of $T$).
Restriction to this subsite is therefore faithful and reflects isomorphisms of
sheaves, and a morphism of sheaves which is bijective on sections over all
affine pro-etale objects is an isomorphism. For a short complex, the
restriction to the subsite is the sheafification of the presheaf complex of
sections, which is exact by hypothesis; sheafification is exact, and
restriction to the dense subsite reflects exactness. Applying this to the
short complexes computing the cohomology sheaves of the cone gives the
assertion on quasi-isomorphisms.

*Step 3 (clause (3)).* The functor $\nu_T^*$ is fully faithful on module
sheaves (the unit $F'\to\nu_{T,*}\nu_T^*F'$ is an isomorphism), so it reflects
isomorphisms: if $\nu_T^*\varphi$ is invertible with inverse $\psi$, then
$\psi=\nu_T^*\chi$ for a unique $\chi$, and $\chi$ is inverse to $\varphi$ by
faithfulness. The converse is functoriality. Isomorphisms of etale sheaves are
detected on the geometric stalks at the points $\bar s$ by
[lemma-weil-pbc-geometric-stalk-conservative]. For bounded-below complexes,
$\nu_T^*$ is fully faithful on $\Dplus$ by [thm-weil-pbc-site-comparison], and
the same argument shows that it reflects isomorphisms. The last assertion is
the definition of $\Dbc(T_{\Proet},\Lambda)$ in
[def-weil-pbc-proetale-modules] as the pullbacks of the bounded constructible
etale objects.
