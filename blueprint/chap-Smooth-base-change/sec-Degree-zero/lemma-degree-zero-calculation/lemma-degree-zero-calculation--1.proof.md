+++
kind = "proof"
of = "lemma-degree-zero-calculation--1"
order = 666002
uses = ["definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-degree-zero-calculation"]
+++
Represent $F_{\acute{e}t}[0]$ by the complex concentrated in degree zero.
Since inverse image is exact and direct image is left exact, there are
canonical identifications

$$
H^0\bigl(g^{-1}Rf_*(F_{\acute{e}t}[0])\bigr)
\simeq g^{-1}f_*F_{\acute{e}t},
\qquad
H^0\bigl(Rf'_*g'^{-1}(F_{\acute{e}t}[0])\bigr)
\simeq f'_*g'^{-1}F_{\acute{e}t}.
$$

To identify the map, use the compatibility of the derived base change map
with the underived map on complexes and the comparison maps from direct
image to its right derived functor. These comparison maps induce
isomorphisms in degree zero on a sheaf placed in degree zero. Exactness of
$g^{-1}$ preserves the first comparison, and $g'^{-1}$ carries
$F_{\acute{e}t}[0]$ to $(g'^{-1}F_{\acute{e}t})[0]$ for the second.
Taking degree-zero cohomology of this compatibility therefore identifies
the two base change maps as arrows.

The underived map is an isomorphism by [lemma-degree-zero-calculation],
so the degree-zero derived map is an isomorphism as well.
