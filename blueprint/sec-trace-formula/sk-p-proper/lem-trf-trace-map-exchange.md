+++
id = "lem-trf-trace-map-exchange"
kind = "lemma"
title = "Exchange of the trace maps"
order = 2456
uses = ["def-trf-admissibility", "def-trf-coefficient-pushforward", "lem-trf-trace-map-from-external-duality", "lem-trf-trace-source-exchange", "thm-trf-dualizing-complex-composition", "thm-trf-fixed-point-base-change", "thm-trf-verdier-duality"]
+++
In the setting of [def-trf-coefficient-pushforward], write
$F=\operatorname{Fix}(c)$, $F'=\operatorname{Fix}(b)$ and let
$h:F\to F'$ be the induced map. The trace maps
$\mathfrak t_{c,K}$ and $\mathfrak t_{b,K'}$ of
[lem-trf-trace-map-from-external-duality] satisfy

$$
Rh_*R\Gamma(F,\mathfrak t_{c,K})
\cong
R\Gamma(F',\mathfrak t_{b,K'})
$$

after the identifications below, i.e. the diagram

$$
\begin{gathered}
R\Gamma(C,\mathcal H_c(K))\xrightarrow{\mathfrak t_{c,K}}
R\Gamma(F,\omega_{F,A})\\
\uparrow\hphantom{\sim}\qquad\qquad\qquad\qquad\uparrow\\
R\Gamma(D,\mathcal H_b(K'))\xrightarrow{\mathfrak t_{b,K'}}
R\Gamma(F',\omega_{F',A})
\end{gathered}
$$

commutes, the vertical arrows being the pushforwards along $g$ and
$h$ composed with the exchange of
[lem-trf-trace-source-exchange] respectively the dualizing-data
comparison.

## Proof

By [lem-trf-trace-map-from-external-duality], the trace map is the
composite

$$
R\Gamma(C,\mathcal H_c(K))
\cong R\Gamma\bigl(C,Rc^!(K\boxtimes_A^{\mathrm L}D_XK)\bigr)
\xrightarrow{R\Gamma(Rc^!e_K)}
R\Gamma\bigl(C,Rc^!R\Delta_{X*}\omega_{X,A}\bigr)
\cong R\Gamma(F,\omega_{F,A}),
$$

the first isomorphism being the external duality
[thm-trf-verdier-duality], the second the adjoint $e_K$ of
evaluation, and the third the fixed-square base change
[thm-trf-fixed-point-base-change] followed by the dualizing
composition [thm-trf-dualizing-complex-composition]. Each of the
four ingredients is natural under the correspondence map $g$:

1. the external-duality comparison of
[thm-trf-verdier-duality] is adjoint-canonical, hence natural;
1. the map $e_K$ is natural in $K$, and the properness
identification $Rf_*=Rf_!$ together with the exchange of
[def-trf-admissibility] gives the compatibility of the external
products and of the dualizing data under $f$, so
$Rg_*Rc^!e_K$ corresponds to $Rb^!e_{K'}$;
1. the fixed-square base change [thm-trf-fixed-point-base-change]
is compatible with the induced $h:F\to F'$ because the fixed squares
of $c$ and $b$ form a commutative cube over the square of
correspondences;
1. the dualizing composition [thm-trf-dualizing-complex-composition]
is functorial.

Assembling the four naturalities gives the commutativity of the diagram,
which is the assertion.
