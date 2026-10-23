+++
id = "sk-lem-stratified-lattice"
kind = "lemma"
title = "Lattices after a finite stratification"
order = 2184
uses = ["sk-lem-coefficient-heart", "sk-prop-sfb-qlbar-colimit-x"]
tags = ["sketch"]
+++
Statements with coefficients $\cO_E/\pi_E^n$ reach $E$-coefficients only through integral
lattices. A lisse $E_X$-module need not have a lattice on all of $X$, but it has one on each
stratum of a finite stratification, and for dévissage arguments this suffices. A global
lattice can fail to exist when $X$ is not normal. Let $X$ be a projective line with $0$ and
$\infty$ glued to a node, and let $Y\to X$ be the infinite chain of projective lines covering
it, an étale $\mathbf Z$-torsor. Descending $E_Y$ along $Y\to X$, with the generator of
$\mathbf Z$ acting by multiplication by $\ell$, gives a lisse $E_X$-module $L$ of rank one.
Since $Y$ is connected, a lattice in $L|_Y\cong E_Y$ is a constant lattice $\pi_E^m\cO_E$, and
no such lattice is stable under multiplication by $\ell$; so $L$ has no lattice on $X$. On the
open stratum $X\smallsetminus\{\text{node}\}\cong\mathbf G_m$ the torsor is trivial and $L$ is
constant.

Let $X$ be a standing scheme and $L$ a lisse $E_X$-module. There is a finite stratification
of $X$ by locally closed subschemes $S$ such that each $L|_S$ contains a lisse
$\cO_{E,S}$-submodule $L_0$ with $L_0[1/\ell]=L|_S$.
