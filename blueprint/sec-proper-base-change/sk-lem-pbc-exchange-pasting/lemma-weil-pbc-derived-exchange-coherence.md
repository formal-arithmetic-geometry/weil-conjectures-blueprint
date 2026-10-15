+++
id = "lemma-weil-pbc-derived-exchange-coherence"
kind = "lemma"
title = "Resolution independence, identities, and pasting"
order = 1074
lean = ["AlgebraicGeometry.Etale.derivedBaseChangeMapPlus_ext", "AlgebraicGeometry.Etale.derivedBaseChangeMapPlus_paste_horiz", "AlgebraicGeometry.Etale.derivedBaseChangeMapPlus_paste_vert"]
uses = ["def-weil-pbc-derived-exchange", "def-weil-pbc-underived-exchange"]
+++
Let $\mathcal A$ be a coefficient category as in
[def-weil-pbc-derived-exchange], and consider derived exchange morphisms
[def-weil-pbc-derived-exchange] of commutative squares of schemes.

1. *(Uniqueness.)* For a commutative square $\square$, every natural
transformation $g^{-1}Rf_*\to Rf'_*g'^{-1}$ on $\Dplus(X_{\Et},\mathcal A)$
which, on every bounded below complex $K$, is computed by the termwise
underived exchange morphism [def-weil-pbc-underived-exchange] (in the sense of
[lemma-weil-pbc-derived-exchange-replacement]) equals $\Ex_{\square}$. In
particular $\Ex_{\square,K}$ does not depend on the choice of a resolution.
2. *(Vertical pasting.)* For commutative squares $\square_1$ (with
$f\circ g'=g\circ f'$, $f:X\to Y$, $f':X'\to Y'$) and $\square_2$ (with
$e\circ g=k\circ e'$, $e:Y\to Z$, $e':Y'\to Z'$), the exchange morphism of the
pasted square ($(e\circ f)\circ g'=k\circ(e'\circ f')$) equals the composite

$$
 k^{-1}R(e f)_*\cong k^{-1}Re_*Rf_*\xrightarrow{\Ex_{\square_2}}
 Re'_*g^{-1}Rf_*\xrightarrow{\Ex_{\square_1}}Re'_*Rf'_*g'^{-1}
 \cong R(e'f')_*g'^{-1},
$$

the outer isomorphisms being the composition isomorphisms of derived direct
images.
3. *(Horizontal pasting.)* For commutative squares $\square_1$ (with
$f\circ g'=g\circ f'$) and $\square_2$ (with $f'\circ g''=h\circ f''$,
$f'':X''\to Y''$, $g'':X''\to X'$, $h:Y''\to Y'$), the exchange morphism of the
pasted square ($f\circ(g'g'')=(gh)\circ f''$) equals the composite

$$
 (gh)^{-1}Rf_*\cong h^{-1}g^{-1}Rf_*\xrightarrow{\Ex_{\square_1}}
 h^{-1}Rf'_*g'^{-1}\xrightarrow{\Ex_{\square_2}}Rf''_*g''^{-1}g'^{-1}
 \cong Rf''_*(g'g'')^{-1},
$$

the outer isomorphisms being the composition isomorphisms of inverse images.
