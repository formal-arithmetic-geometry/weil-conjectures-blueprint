+++
id = "thm-dg-finite-type-constructibility"
kind = "theorem"
title = "Bounded constructibility of every finite-type direct image"
lean = ["AlgebraicGeometry.Etale.boundedConstructible_rightDerivedLowerStar_of_locallyOfFiniteType"]
order = 2722
uses = ["cor-fin-deligne-open-finite-coefficients", "def-weil-pbc-constructible-complexes", "def-weil-pbc-derived-categories", "def-weil-pbc-extension-by-zero", "def-weil-pbc-scheme-conventions", "lem-fin-proper-bounded-constructible", "lem-weil-derived-direct-image-composition", "lem-weil-pbc-grothendieck-spectral-sequence", "sbc-def-coefficient-conventions", "thm-constructible-serre"]
+++
Let $f:X\to Y$ be a morphism between finite-type schemes over
a field $k$, and let $A$ be a finite ring annihilated by an
integer invertible in $k$. Then

$$
Rf_*:D^b_c(X,A)\longrightarrow D^b_c(Y,A)
$$

is defined on the ordinary derived categories. The morphism
$f$ need not be separated.
