+++
id = "sk-def-exchange"
kind = "definition"
title = "Derived base change map"
order = 1399
lean = ["AlgebraicGeometry.Etale.baseChange", "AlgebraicGeometry.Etale.squareUpperStarIso", "AlgebraicGeometry.Etale.pullbackSquareComparison", "AlgebraicGeometry.Etale.baseChangeMap", "AlgebraicGeometry.Etale.baseChangeMap_naturality", "AlgebraicGeometry.Etale.baseChangeMap_app_pullSection", "AlgebraicGeometry.Etale.derivedUpperStarLowerStarAdjunctionPlus", "AlgebraicGeometry.Etale.baseChange_naturality", "AlgebraicGeometry.Etale.baseChange_eq_derivedBaseChangeMapPlus", "AlgebraicGeometry.Etale.derivedBaseChangeMapPlus_eq_termwise"]
uses = ["sk-def-conv", "sk-def-pbc-conventions"]
tags = ["sketch"]
+++
Proper base change asserts that a specific map, from the pullback of the
direct image to the direct image of the pullback, is an isomorphism. We
define this map first, and describe it on sections so that we can compute
it on stalks. Consider a cartesian square

$$
\begin{array}{ccc}
X' & \xrightarrow{g'} & X\\
{\scriptstyle f'}\downarrow & & \downarrow{\scriptstyle f}\\
Y' & \xrightarrow{g} & Y.
\end{array}
$$

Since $gf'=fg'$, the composition isomorphisms of inverse images give
an isomorphism $f'^*g^*\simeq g'^*f^*$, on sheaves and, since inverse
images are exact, on bounded below derived categories. Let $F$ be a
sheaf on $X_{\Et}$. The *underived base change map*

$$
 g^*f_*F\longrightarrow f'_*g'^*F
$$

is the adjoint, under $f'^*\dashv f'_*$, of

$$
 f'^*g^*f_*F
 \simeq g'^*f^*f_*F
 \xrightarrow{g'^*\varepsilon_f}g'^*F,
$$

where $\varepsilon_f:f^*f_*\to\mathrm{id}$ is the counit.
Equivalently, first apply the unit
$g^*f_*F\to f'_*f'^*g^*f_*F$, and then apply $f'_*$ to
the displayed composite. This construction is natural in $F$, and it applies
equally to sheaves of $\Lambda$-modules.

On sections the map has the following simple description. A section of $g^*f_*F$ over an
étale $V\to Y'$ is represented by an étale $W\to Y$, a map $V\to
Y'\times_YW$, and a section over $X\times_YW$. The base change map restricts
this section along

$$
 X'\times_{Y'}V\longrightarrow X\times_YW,
$$

and it is the sheafification of this map of presheaves.

**Definition (derived base change map).** For $K\in D^+(X_{\Et},\Lambda)$, the *base change map*

$$
 g^*Rf_*K\longrightarrow Rf'_*g'^*K
$$

is the adjoint, under $f'^*\dashv Rf'_*$, of

$$
 f'^*g^*Rf_*K
 \simeq g'^*f^*Rf_*K
 \xrightarrow{g'^*\varepsilon_f}g'^*K,
$$

where $\varepsilon_f:f^*Rf_*\to\mathrm{id}$ now denotes the derived
counit. The morphism is natural in $K$. (Elsewhere in the blueprint it is
written $\Ex_{\square,K}$, the underived map $\Ex^0_{\square,F}$, and the square
isomorphism $\theta_\square$.)

The derived adjunction exists because inverse image is exact and its
right adjoint preserves injectives. The construction of the base change
map uses only that the square commutes, and the cartesian hypothesis
enters when we ask whether the map is an isomorphism.

To compute the derived base change map, choose a bounded below
injective resolution $K\to I^\bullet$ and an injective replacement
$g'^*I^\bullet\to J^\bullet$. Then the base change map is represented by the
morphism of complexes

$$
 g^*f_*I^\bullet
 \longrightarrow
 f'_*g'^*I^\bullet\longrightarrow f'_*J^\bullet.
$$

The first arrow is the underived base change map in each degree. By
exactness of $g^*$ the source is $g^*Rf_*K$, and the last complex
computes $Rf'_*g'^*K$. Since comparison maps between injective resolutions
are unique up to homotopy, this formula is independent of the
choices. It is the adjoint map of the definition, because
under adjunction the first arrow corresponds to the square isomorphism
followed by the counit, and the replacement map is the canonical passage
to the derived direct image.
