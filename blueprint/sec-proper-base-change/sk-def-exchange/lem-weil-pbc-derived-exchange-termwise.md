+++
id = "lem-weil-pbc-derived-exchange-termwise"
kind = "lemma"
title = "The termwise construction of the derived exchange morphism"
order = 1041
uses = ["def-weil-pbc-cartesian-square", "def-weil-pbc-derived-categories", "def-weil-pbc-derived-exchange", "def-weil-pbc-direct-image", "def-weil-pbc-inverse-image", "def-weil-pbc-kinjective-resolutions", "def-weil-pbc-underived-exchange", "prop-weil-pbc-kinjective-resolutions-exist"]
+++
Let $\square$ be a cartesian square
[def-weil-pbc-cartesian-square] and let $K\in\Dplus(X_{\Et})$. If
$K\to I$ is a K-injective resolution
[def-weil-pbc-kinjective-resolutions] of $K$ and $g'^{-1}I\to J$ is a
K-injective resolution of $g'^{-1}I$ on $X'$, then the morphism

$$
 g^{-1}Rf_*K\longrightarrow Rf'_*g'^{-1}K
$$

of the derived category [def-weil-pbc-derived-categories] obtained by
applying the underived exchange morphism
[def-weil-pbc-underived-exchange] $\Ex^0_{\square,I}$ term by term
to $I$ and comparing $g'^{-1}I$ with $J$ is the derived exchange morphism
$\Ex_{\square,K}$ of [def-weil-pbc-derived-exchange].
