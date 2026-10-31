+++
id = "prose-10-12"
kind = "hidden"
title = "The orientation from the diagonal"
order = 448
+++
Since $f^!K\simeq f^*K\otimes^{\mathbf L}\omega_f$, it remains, for finite coefficients, to construct
a single global isomorphism
$\omega_f\simeq(\mathbf Z/\ell^n\mathbf Z)_X(d)[2d]$.
We obtain it from the diagonal
$\Delta:X\to X\times_YX$, which is a section of the smooth projection
$p_1$. Deformation to the normal bundle moves $\Delta$ to the zero
section of the relative tangent bundle $T_{X/Y}$, where
Proposition [sk-prop-an] provides the
isomorphism.

The diagonal is the right object because it is attached to $f$ without
choices, and because $\omega_f$ is recovered from it:
$\omega_f\simeq\Delta^*\omega_{p_1}$ by base change. Near the diagonal,
$X\times_YX$ looks like a neighbourhood of the zero section in $T_{X/Y}$,
but only to first order, and the deformation makes this precise without
choosing a tubular neighbourhood. The comparison it produces
(Lemma [sk-thm-dnc]) is pinned down by requiring it to be the
identity at $t=1$, and this uniqueness is used repeatedly afterwards:
for naturality (Lemma [sk-lem-lem-sp-dnc-naturality]), for the comparison
with charts at the end of the subsection, and for base change and
change of coefficients in Section [sec-sp-grp-trace] and
Section [sec-sp-grp-ladic-summary].

The deformation argument works for any section of a smooth morphism. Let $g:V\to S$ be smooth of pure
relative dimension $d$ and let $s:S\to V$ be a section of $g$ that is a
closed immersion. Then $s$ is a regular immersion of codimension $d$.
Let $N_s$ be its normal bundle, with projection $\pi:N_s\to S$ and zero
section $z:S\to N_s$.

The *deformation to the normal bundle* is the open subscheme
$\mathcal D_{s(S)}V$ of the blowup of $V\times\mathbf A^1$ along
$s(S)\times\{0\}$ obtained by removing the strict transform of
$V\times\{0\}$. It comes with a smooth morphism
$\widetilde g:\mathcal D_{s(S)}V\to\mathbf A^1_S$ and a section
$\widetilde s:\mathbf A^1_S\to\mathcal D_{s(S)}V$ that is a closed
immersion. Over $t=1$ the pair $(\widetilde g,\widetilde s)$ restricts
to $(g,s)$, and over $t=0$ to $(\pi,z)$. In local terms, let $t$ be the
coordinate of $\mathbf A^1$, and let $x_1,\ldots,x_d$ be functions on an
open neighbourhood $U$ of $s(S)$ in $V$ which are étale coordinates over
$S$ and generate the ideal of $s(S)$. On the part of
$\mathcal D_{s(S)}V$ lying over $U\times\mathbf A^1$, the quotients
$u_i=x_i/t$ are regular functions, so that $x_i=tu_i$ there. At $t=0$ the
function $u_i$ restricts to the linear function on $N_s$ given by the class
of $x_i$ in the conormal sheaf. Since these classes form a basis of the
conormal sheaf, the $u_i$ restrict to linear coordinates on $N_s$.
