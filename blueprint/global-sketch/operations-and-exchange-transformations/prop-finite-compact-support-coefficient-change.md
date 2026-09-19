+++
id = "prop-finite-compact-support-coefficient-change"
kind = "theorem"
title = "Finite-level coefficient change for proper support"
order = 49
tags = ["latex:proposition"]
uses = ["def-compact-support-direct-image", "def-finite-reduction", "def-weil-finite-coefficient-datum", "prop-compactification-coherence"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ and a separated finite-type
morphism $f:X\to Y$. Let $1\leq m\leq n$, and suppose that
$K_n\in D^b_c(X,\mathcal O_E/\varpi_E^n)$ and
$K_m\in D^b_c(X,\mathcal O_E/\varpi_E^m)$ are equipped with an
isomorphism

$$
(\mathcal O_E/\varpi_E^m)_X
\otimes^L_{(\mathcal O_E/\varpi_E^n)_X}K_n
\xrightarrow{\sim}K_m.
$$

Then the canonical coefficient-change morphism is an isomorphism

$$
(\mathcal O_E/\varpi_E^m)_Y
\otimes^L_{(\mathcal O_E/\varpi_E^n)_Y}Rf_{!,n}K_n
\xrightarrow{\sim}Rf_{!,m}K_m.
$$

These isomorphisms are transitive in $m\leq n$ and commute with the
compactification-coherence maps. Consequently, applying $Rf_{!,n}$ to
the stages of a strict reduction tower again produces a strict reduction
tower.
