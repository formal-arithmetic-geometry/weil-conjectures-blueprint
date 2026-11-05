+++
id = "definition-relative-picard-functor--1"
kind = "definition"
title = "Relative Picard functor (1)"
name_showing = false
order = 1521001
aliases = ["bp-r473-1"]
lean = ["AlgebraicGeometry.picardFunctor"]
+++
For a morphism of schemes $f:C\to S$, let

$$
\operatorname{Pic}_{C/S}
=\bigl(T\longmapsto
\operatorname{Pic}(C_T)/f_T^*\operatorname{Pic}(T)\bigr)^{\mathrm{fppf}}.
$$

Here $C_T=C\times_ST$, and the superscript denotes sheafification on
the big fppf site of $S$.
