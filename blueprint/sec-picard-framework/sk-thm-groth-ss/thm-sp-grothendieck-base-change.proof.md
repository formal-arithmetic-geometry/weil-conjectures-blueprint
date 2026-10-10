+++
kind  = "proof"
of    = "thm-sp-grothendieck-base-change"
+++
*Step 1: the map of double complexes.* By the proof of
[thm-sp-grothendieck] the two spectral sequences are those of the double
complexes $C^{\bullet,\bullet}$ and $C'^{\bullet,\bullet}$ obtained from
injective resolutions $X\to I^\bullet$, $X'\to I'^\bullet$ and
Cartan--Eilenberg resolutions of $F(I^\bullet)$ and $F'(I'^\bullet)$.
Exactness of $\alpha$ and of $\beta$ carries an injective resolution of $X$
to a resolution of $\alpha X$ with acyclic terms, and the commutativity of
the squares identifies $\beta F(I^\bullet)$ with $F'\alpha(I^\bullet)$ up to
the fixed natural isomorphism; applying $\beta$ termwise to the
Cartan--Eilenberg resolution and using exactness and the acyclicity
hypotheses therefore produces a morphism of double complexes
$C^{\bullet,\bullet}\to C'^{\bullet,\bullet}$ over $X\to\alpha X$. Exactness
of $\gamma$ is used in the same way to compare the total complexes after
applying the two functors.

*Step 2: the map of spectral sequences.* A morphism of double complexes
induces a morphism of the filtered total complexes and hence, by
[thm-sp-spectral-object-yields], a morphism of the associated exact couples;
by [lem-sp-couple-morphism] it induces a morphism of the spectral sequences,
commuting with the differentials and with the page identifications, and
natural in the resolutions and hence in $X\to\alpha X$. The acyclicity
hypotheses of [def-sp-composite-acyclicity] are what identify the
$E_2$-pages of the two sequences with $R^pG(R^qF(X))$ and
$R^pG'(R^qF'(\alpha X))$, and they are preserved by exactness of the vertical
functors.

*Step 3: base change.* In the base-change situation of the
proper-base-change chapter the vertical functors are the inverse images
$g'^{-1}$, $g'^{-1}$, $g^{-1}$ along the maps of a cartesian square; these
are exact, since inverse image of sheaves is exact, and the two squares
commute by the base-change identification of the inverse images in a
cartesian square. Step 1 and Step 2 therefore apply and give the
compatibility of the Grothendieck spectral sequence with inverse image along
a base change.
