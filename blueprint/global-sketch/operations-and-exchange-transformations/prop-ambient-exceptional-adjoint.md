+++
id = "prop-ambient-exceptional-adjoint"
kind = "theorem"
title = "Ambient exceptional right adjoint"
order = 53
tags = ["latex:proposition"]
uses = ["def-compact-support-direct-image", "def-full-cohomological-dimension", "def-weil-finite-coefficient-datum", "prop-compactification-coherence"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$. Let $n\geq1$, let
$f:X\to Y$ be separated and of finite type, choose a compactification
$\gamma=(j,p)\in\operatorname{Comp}(f)$, and let $c\geq0$ be an
integer such that
$\operatorname{FullCD}(p,\mathcal O_E/\varpi_E^n;c)$ holds. The ambient
candidate attached to this chosen compactification,

$$
Rf_{!,n}^{\gamma}=Rp_{*,n}j_{!,n}:
D\bigl(X_{\mathrm{proet}},(\mathcal O_E/\varpi_E^n)_X\bigr)
\longrightarrow
D\bigl(Y_{\mathrm{proet}},(\mathcal O_E/\varpi_E^n)_Y\bigr)
$$

is exact, preserves arbitrary coproducts, and has a right adjoint, denoted
relative to this choice by

$$
Rf_n^{\times}:
D\bigl(Y_{\mathrm{proet}},(\mathcal O_E/\varpi_E^n)_Y\bigr)
\longrightarrow
D\bigl(X_{\mathrm{proet}},(\mathcal O_E/\varpi_E^n)_X\bigr).
$$

Its restriction to $D^b_c(X,\mathcal O_E/\varpi_E^n)$ identifies with the
compactification-independent functor of
Definition [def-compact-support-direct-image]. No
compactification-independence assertion for the ambient unbounded functor is
used here; independence and coefficient compatibility of its constructible
right-adjoint restriction are required explicitly in the admissibility data
below.
