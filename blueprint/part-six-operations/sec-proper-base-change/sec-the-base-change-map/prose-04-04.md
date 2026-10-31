+++
id = "prose-04-04"
kind = "hidden"
title = "The base change map (2)"
order = 176
+++
The derived adjunction exists because inverse image is exact and its
right adjoint preserves injectives. The construction of the base change
map uses only that the square commutes, and the cartesian hypothesis
enters when we ask whether the map is an isomorphism.

To compute (4.3), choose a bounded below
injective resolution $K\to I^\bullet$ and an injective replacement
$g'^*I^\bullet\to J^\bullet$. Then the base change map is represented by the
morphism of complexes

$$
g^*f_*I^\bullet
\longrightarrow
f'_*g'^*I^\bullet\longrightarrow f'_*J^\bullet.
\tag{4.4}
$$

The first arrow is the underived base change map in each degree. By
exactness of $g^*$ the source is $g^*Rf_*K$, and the last complex
computes $Rf'_*g'^*K$. Since comparison maps between injective resolutions
are unique up to homotopy, this formula is independent of the
choices. It is the adjoint map of Definition [sk-def-exchange], because
under adjunction the first arrow corresponds to the square isomorphism
followed by the counit, and the replacement map is the canonical passage
to the derived direct image.

Base change maps for composite squares are composites of base change
maps. Lemma [sk-lem-sbc-exchange-compatibility] uses this when it
transports the base change map to the pro-étale site.
