+++
id = "prop-compact-support-coefficient-passage-detailed"
kind = "theorem"
title = "Coefficient passage and constructible landing for proper support"
order = 6807
lean = ["AlgebraicGeometry.Proetale.compactSupport_coefficientPassage"]
tags = ["latex:proposition"]
uses = ["prop-finite-compact-support-constructibility"]
+++
Let $K_0$ be a field, let $X,Y$ be finite-type $K_0$-schemes, and let
$f:X\to Y$ be a separated finite-type $K_0$-morphism. Fix a prime $\ell$,
write $\Ql=\mathbf Q_\ell$, choose an algebraic closure $\Qlb$ of $\Ql$, and
require that its image in $K_0$ is invertible. Choose a finite extension
$E/\Ql$, its valuation ring $\mathcal O_E$, and $n\in\mathbf Z_{\geq1}$, with
$A=A_{E,n}$. For each $\Lambda\in\{\mathcal O_E,E,\Qlb\}$, assume that every
finite-level compact-support direct image sends bounded constructible
complexes to bounded constructible complexes with a coefficient-independent
cohomological interval. Its derived-complete, rational, or common-stage
passage give an exact triangulated functor
$$
 Rf_!:D^b_c(X,\Lambda)\longrightarrow D^b_c(Y,\Lambda).
$$
For integral coefficients and every $K\in D^b_c(X,\mathcal O_E)$, put
$K_n=K\otimes^L_{\mathcal O_E}A_{E,n}$. There are natural isomorphisms, for
every $n\geq1$,
$$
 (Rf_!K)\otimes^L_{\mathcal O_E}A_{E,n}
 \xrightarrow{\sim}Rf_{!,n}K_n.
$$
These isomorphisms and the compactification comparisons are compatible with
reduction, composition, rationalization, finite scalar extension, and the
common-stage $\Qlb$-construction.

*Import note.* The id `prop-compact-support-coefficient-passage` is already
taken on the blueprint by the corresponding object of the earlier sketch
import, so this detailed version carries a `-detailed` suffix.

## Proof

Let $K\in D^b_c(X,\mathcal O_E)$ and write
$K_n=K\otimes^L_{\mathcal O_E}A_{E,n}$. By the finite-coefficient
compact-support constructibility statement, every $Rf_{!,n}K_n$ is bounded
constructible on $Y$, with a cohomological interval independent of the
compactification; the assumed coefficient-independent interval of the
statement provides a common bound for the intervals of the $Rf_{!,n}K_n$,
$n\geq1$, which is what makes the limit below uniform in $n$. The construction
of the integral, rational and common-stage compact-support direct image
therefore defines
$$
 Rf_!K=R\varprojlim_n\operatorname{Res}_nRf_{!,n}K_n
$$
and its reduction modulo $\varpi_E^n$ is naturally $Rf_{!,n}K_n$. The
transition maps are the reduction maps, so this identification is functorial
in $K$ and compatible with the coherent compactification comparisons.

If $K_E$ is the rationalization of $K$, the same cited definition gives
$$
 Rf_!K_E=(Rf_!K)\otimes^L_{\mathcal O_E}E,
$$
and if $K_{\Qlb}$ is represented over a finite $E\subset\Qlb$, it gives
$$
 Rf_!K_{\Qlb}=Rf_!K_E\otimes_E\Qlb.
$$
Derived tensor, rationalization, and the common-stage construction are exact
triangulated functors by that definition; hence the resulting $Rf_!$ is exact
at all three coefficient levels. The displayed reduction identifications
commute with composition, scalar extension, and compactification comparison
because each is induced levelwise by the corresponding finite-level map.

Unresolved dependencies: def:weil-integral-rational-qbar-compact-support, def:weil-scheme-morphism-properties
