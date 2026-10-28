+++
id = "sk-lem-stratified-lattice"
kind = "lemma"
title = "Lattices after a finite stratification"
order = 2308
uses = ["sk-def-sfb-constructible"]
tags = ["sketch"]
+++
A lisse $E_X$-module may fail to have a lattice on all of $X$, but it has one on each stratum
of a finite stratification, and this is enough for dévissage arguments. A global lattice can
fail to exist when $X$ is not normal. Let $X$ be a projective line with $0$ and $\infty$ glued
to a node, and let $Y\to X$ be the infinite chain of projective lines covering it, an étale
$\mathbf Z$-torsor. Descending $E_Y$ along $Y\to X$, with the generator of $\mathbf Z$ acting
by multiplication by $\ell$, we obtain a lisse $E_X$-module $L$ of rank one. Since $Y$ is
connected, a lattice in $L|_Y\simeq E_Y$ is a constant lattice $\pi_E^m\cO_E$. The pullback of
a lattice in $L$ would be such a lattice, preserved by the descent datum. But the generator of
$\mathbf Z$ carries $\pi_E^m\cO_E$ to $\ell\pi_E^m\cO_E$, which is strictly smaller. Hence $L$
has no lattice on $X$. On the open stratum $X\smallsetminus\{\text{node}\}\simeq\mathbf G_m$ the
torsor is trivial and $L$ is constant.

Let $L$ be a lisse $E_X$-module ([sk-def-sfb-constructible]). There is a finite stratification
of $X$ by locally closed subschemes $S$ such that each $L|_S$ contains a lisse
$\cO_{E,S}$-submodule $L_0$ with $L_0[1/\ell]=L|_S$.
