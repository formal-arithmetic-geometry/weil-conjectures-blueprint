+++
id = "sk-def-exchange"
kind = "definition"
title = "Derived exchange"
order = 1287
lean = ["AlgebraicGeometry.Etale.baseChange", "AlgebraicGeometry.Etale.squareUpperStarIso", "AlgebraicGeometry.Etale.pullbackSquareComparison", "AlgebraicGeometry.Etale.baseChangeMap", "AlgebraicGeometry.Etale.baseChangeMap_naturality", "AlgebraicGeometry.Etale.baseChangeMap_app_pullSection", "AlgebraicGeometry.Etale.derivedUpperStarLowerStarAdjunctionPlus", "AlgebraicGeometry.Etale.baseChange_naturality", "AlgebraicGeometry.Etale.baseChange_eq_derivedBaseChangeMapPlus", "AlgebraicGeometry.Etale.derivedBaseChangeMapPlus_eq_termwise"]
uses = ["sk-def-conv", "sk-def-pbc-conventions"]
tags = ["sketch"]
+++
Consider a cartesian square

$$
\begin{array}{ccc}
X' & \xrightarrow{g'} & X\\
{\scriptstyle f'}\downarrow & & \downarrow{\scriptstyle f}\\
Y' & \xrightarrow{g} & Y.
\end{array}
$$

Since $gf'=fg'$, the composition isomorphisms of inverse images define an
isomorphism

$$
\theta_\square:f'^{-1}g^{-1}\xrightarrow{\ \sim\ }g'^{-1}f^{-1}.
$$

Since inverse images are exact, $\theta_\square$ also denotes the induced
isomorphism on bounded below derived categories. Let $F$ be a sheaf on
$X_{\Et}$. The *underived exchange map*

$$
\Ex^0_{\square,F}:g^{-1}f_*F\longrightarrow f'_*g'^{-1}F
$$

is the adjoint, under $f'^{-1}\dashv f'_*$, of

$$
f'^{-1}g^{-1}f_*F\xrightarrow{\ \theta_\square\ }g'^{-1}f^{-1}f_*F
\xrightarrow{\ g'^{-1}\varepsilon_f\ }g'^{-1}F.
$$

Here $\varepsilon_f:f^{-1}f_*\to\mathrm{id}$ is the counit. Equivalently,
first apply the unit $g^{-1}f_*F\to f'_*f'^{-1}g^{-1}f_*F$, and then apply
$f'_*$ to the displayed composite. This construction is natural in $F$, and it
applies equally to sheaves of $\Lambda$-modules.

On sections the map has a simple description, which we use to compute it on
stalks. A section of $g^{-1}f_*F$ over an étale $V\to Y'$ is represented by
an étale $W\to Y$, a map $V\to Y'\times_YW$, and a section over $X\times_YW$.
The exchange map restricts this section along

$$
X'\times_{Y'}V\longrightarrow X\times_YW,
$$

and passes to sheafification.

**Definition (derived exchange).** For $K\in D^+(X_{\Et},\Lambda)$, the
*exchange morphism*

$$
\Ex_{\square,K}:g^{-1}Rf_*K\longrightarrow Rf'_*g'^{-1}K
$$

is the adjoint, under $f'^{-1}\dashv Rf'_*$, of

$$
f'^{-1}g^{-1}Rf_*K\xrightarrow{\ \theta_\square\ }g'^{-1}f^{-1}Rf_*K
\xrightarrow{\ g'^{-1}\varepsilon_f\ }g'^{-1}K,
$$

where $\varepsilon_f:f^{-1}Rf_*\to\mathrm{id}$ now denotes the derived
counit. The morphism is natural in $K$.

The derived adjunction exists because inverse image is exact and its right
adjoint preserves injectives. To construct the exchange map, we only need a
commutative square; the cartesian hypothesis matters only for the question
whether the map is an isomorphism.

To compute $\Ex_{\square,K}$, choose a bounded below injective resolution
$K\to I^\bullet$ and an injective replacement $g'^{-1}I^\bullet\to J^\bullet$.
Then the exchange map is represented by the morphism of complexes

$$
g^{-1}f_*I^\bullet\xrightarrow{\ \Ex^0_{\square,I^\bullet}\ }
f'_*g'^{-1}I^\bullet\longrightarrow f'_*J^\bullet.
$$

The first arrow is the underived exchange map in each degree. By exactness of
$g^{-1}$ the source is $g^{-1}Rf_*K$, and the last complex computes
$Rf'_*g'^{-1}K$. Since comparison maps between injective resolutions are
unique up to homotopy, this formula is independent of the choices. It is the
adjoint map of the definition, because under adjunction the first arrow
corresponds to the square isomorphism followed by the counit, and the
replacement map is the canonical passage to the derived direct image.
