+++
id = "prop-weil-pbc-rlim-functoriality"
kind = "theorem"
title = "Functoriality of the sequential derived inverse limit"
order = 1310
uses = ["def-weil-derived-limit", "def-weil-pbc-adic-coefficient-datum", "def-weil-pbc-derived-inverse-limit", "def-weil-pbc-kinjective-resolutions", "prop-weil-pbc-derived-inverse-limit-computation"]
tags = ["latex:proposition"]
+++
Let $\operatorname{Tow}_{A}(T)$ be the tower category of
[def-weil-pbc-adic-coefficient-datum], an abelian category with enough
injectives. Fixing a functorial K-injective resolution
[def-weil-pbc-kinjective-resolutions] $M_\bullet\to I_\bullet$ of every
object of $\operatorname{Tow}_{A}(T)$, the assignment

$$
 \Rlim:D(\operatorname{Tow}_{A}(T))\longrightarrow D(T_{\Proet},A),
 \qquad
 M_\bullet\longmapsto\varprojlim_nI_n
$$

is a triangulated functor, and any two such choices of functorial K-injective
resolutions give isomorphic functors.
