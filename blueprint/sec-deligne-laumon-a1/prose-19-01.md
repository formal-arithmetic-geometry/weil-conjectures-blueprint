+++
id = "prose-19-01"
kind = "hidden"
title = "Strategy for weights of curve cohomology"
order = 4221
+++
The main result of this section is the bound on curves to which
Section “The weight bound and why it holds” reduces the weight theorem: for a pure lisse Weil
sheaf $F$ of weight $w$ on a smooth curve, the group
$H_c^r(C,F)$ has weights at most $w+r$ (Theorem [sk-cor-wft-curve-upper]).
Only $r=1$ needs work, since Lemma [sk-l-dl-a1-endpoints] settles
the other degrees on an affine curve. Let $M$ be an irreducible sheaf
on an open of the affine line, no geometric constituent of which is of
the form $\mathcal L_{\psi(ax)}$. Then the group $H^1_c$ of $j_*M$ is the
stalk at the origin of the middle extension of the lisse sheaf $M'$ of
Proposition [sk-p-dl-a1-middle], so it suffices to show that $M'$ is pure
of weight $w+1$. The difficulty is that $M'$ need not be real, so
Theorem [sk-p-real-purity] does not apply to it directly. We
show instead that a twist of $M'$ is a quotient of a real sheaf, which
makes it pure of some weight, and then the Plancherel formula
identifies this weight as $w+1$. An arbitrary curve is reduced to the line by a
finite map.

Throughout this subsection and the next, $j:U_0\hookrightarrow\mathbf A^1_{k_0}$
is a dense open and $M$ is a nonzero irreducible lisse Weil sheaf
on $U_0$, pure of weight $w$. We assume that no geometric irreducible
constituent of $M$ is the restriction of $\mathcal L_{\psi(ax)}$ for
some $a\in\bar k_0$, and we let $M'$ be the lisse Weil sheaf on a dense
open $j':U'_0\hookrightarrow\mathbf A^{1\vee}_{k_0}$ with
$\operatorname{FT}_\psi((j_*M)[1])\simeq(j'_*M')[1]$
(Proposition [sk-p-dl-a1-middle]).

The real sheaf that we construct below is built from extensions by
zero, because these have the simplest Fourier transforms. We first
compare the transform of $j_!M$ with that of the middle extension
$j_*M$; they differ by a lisse sheaf of weights at most $w$.
