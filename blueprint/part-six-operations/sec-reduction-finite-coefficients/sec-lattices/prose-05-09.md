+++
id = "prose-05-09"
kind = "hidden"
title = "Lattices"
order = 251
+++
We pass from statements with coefficients $\mathcal O_E/\pi_E^n$ to
statements with coefficients $E$ through integral lattices. A lisse
$E_X$-module may fail to have a lattice on all of $X$, but it has one on
each stratum of a finite stratification, and this is enough for dévissage
arguments. The stratified statement
(Lemma [sk-lem-stratified-lattice]) supplies the integral generators
of Lemma [sk-lem-integral-models](4) and is the first step of the
uniform Ext bound and of the degree bound for proper direct image in
Section [sec-six-functors-basics]. On a connected normal scheme we obtain a
global lattice, and with it the description of lisse $E$-sheaves as
representations of $\pi_1(X,\bar x)$
(Proposition [sk-p-real-integral]).

A global lattice can fail to exist when $X$ is not normal. Let $X$ be a
projective line with $0$ and $\infty$ glued to a node, and let $Y\to X$
be the infinite chain of projective lines covering it, an étale
$\mathbf Z$-torsor. Descending $E_Y$ along $Y\to X$, with the generator
of $\mathbf Z$ acting by multiplication by $\ell$, we obtain a lisse
$E_X$-module $L$ of rank one. Since $Y$ is connected, a lattice in
$L|_Y\simeq E_Y$ is a constant lattice $\pi_E^m\mathcal O_E$. The
pullback of a lattice in $L$ would be such a lattice, preserved by the
descent datum. But the generator of $\mathbf Z$ carries
$\pi_E^m\mathcal O_E$ to $\ell\pi_E^m\mathcal O_E$, which is strictly
smaller. Hence $L$ has no lattice
on $X$. On the open stratum $X\smallsetminus\{\text{node}\}\simeq\mathbf G_m$
the torsor is trivial and $L$ is constant.
