+++
id = "prose-09-01"
kind = "hidden"
title = "Overview of smooth base change and the map"
order = 2151
+++
Proper base change says that ordinary direct image commutes with an
arbitrary change of base when the morphism pushed forward is proper.
Smooth base change reaches the same conclusion with the hypotheses
on the other side of the square: the morphism $f$ along which we take
direct image is arbitrary, and the change of base $g$ is smooth.

Smooth base change completes the base change theorems of the six
operations, but the proof of the Weil conjectures does not use it. Verdier
biduality restricts complexes to the geometric generic fibre of a family
over a curve, which is a limit of schemes étale over the base, and base
change along an étale map is formal ([sk-lem-pd-generic-restriction]).
The Künneth formula along a product projection $X\times T\to Y\times T$,
which the trace formula uses, is a base change along $Y\times T\to Y$; this
map is smooth only when $T$ is, and for singular $T$ we use instead base
change for open direct images over the ground field
([sk-lem-tf-independent-base-change]). A reader interested only in the
Weil conjectures may skip this section.

We first prove the theorem for torsion sheaves
([sk-thm-smooth-base-change]) by induction on the
cohomological degree. The theorem for bounded below complexes ([sk-thm-sbc-derived]) and on
$\Dctf(-,\Lambda)$ for every admissible $\Lambda$
([sk-thm-sbc-coefficients]) then follow by a spectral sequence
and by [sk-prop-reduction-to-finite].

Consider a cartesian square, with $X'=Y'\times_YX$,

$$
\begin{CD}
 X' @>{g'}>> X\\
 @V{f'}VV @VV{f}V\\
 Y' @>{g}>> Y.
\end{CD}
$$

In smooth base change for torsion sheaves
([sk-thm-smooth-base-change]) we assume that $f$ is quasi-compact
and quasi-separated (qcqs) and that $g$ is smooth, while in the theorem on
$\Dctf$ all schemes are of finite type over $k$. Every inverse
image below is the exact inverse image for the pullback of the coefficient
ring, so that $g^*=Lg^*$ and $g'^*=Lg'^*$.

Let $K\in D(X_{\mathrm{pro\acute et}},\Lambda)$. The base change map

$$
g^*Rf_*K\longrightarrow Rf'_*g'^*K
$$

is defined as the adjoint transpose, for $f'^*\dashv Rf'_*$, of the
following composite, where $\varepsilon_f:f^*Rf_*\to\mathrm{id}$ is
the counit of $f^*\dashv Rf_*$:

$$
f'^*g^*Rf_*K\simeq g'^*f^*Rf_*K
       \xrightarrow{g'^*\varepsilon_f}g'^*K.
$$

Equivalently, with $\eta_{f'}$ the unit of $f'^*\dashv Rf'_*$, it is
the composite

$$
g^*Rf_*K\xrightarrow{\eta_{f'}}
 Rf'_*f'^*g^*Rf_*K\simeq Rf'_*g'^*f^*Rf_*K
       \xrightarrow{Rf'_*g'^*\varepsilon_f}Rf'_*g'^*K.
$$

This is the pro-étale form of the base change map of
[sk-def-exchange], and it is defined for every cartesian
square as displayed above. In the proofs below we transport the base change map
between the étale and pro-étale sites and between coefficient
rings, so we need to know that it is compatible with these comparisons.
