+++
id = "prose-P1-01"
kind = "hidden"
title = "The six operations"
order = 21
+++
The table of Section [sec-n-dictionary] lists what we want: for every
morphism $f$ of schemes of finite type over $k$, functors $f^*$, $Rf_*$,
$Rf_!$, $f^!$, $\otimes^{\mathbf L}$ and $\cHom$ on a derived category of
$\ell$-adic sheaves, with the adjunctions $f^*\dashv Rf_*$,
$Rf_!\dashv f^!$ and $-\otimes^{\mathbf L}K\dashv\cHom(K,-)$, the base
change and projection formulas, and finiteness: each operation carries
constructible complexes to constructible complexes. This part constructs
them. The result is Theorem [sk-thm-existence] together with
Proposition [sk-thm-sf-ctf-stability], and it holds simultaneously for the
coefficient rings

$$
A,\ \Zl,\ \mathcal O_E,\ \Ql,\ E,\ \overline{\mathbf Q}_\ell,
$$

compatibly with every change of coefficients between them
(Section [sec-n-change]).

For torsion coefficients much of this is classical: SGA 4 constructs
$Rf_!$ and $f^!$ on the étale site and proves the finiteness theorems
for $\mathbf Z/\ell^n$ (SGA4, SGA4.5). Two things are missing for
the Weil conjectures. First, the eigenvalues of Frobenius live in
characteristic zero, so we need the same operations for $\Zl$, $\Ql$ and
$\overline{\mathbf Q}_\ell$, compatibly with reduction modulo $\ell^n$; on the étale site
an $\ell$-adic sheaf is a system $(F_n)$, and every derived construction
has to be made by hand on such systems (Eke). Second, the
exceptional inverse image $f^!$ is a right adjoint, so its existence is a
question about all of $D$, not only about constructible objects, and
finiteness of $f^!$ is a separate and genuinely geometric theorem. We
meet the first difficulty by working on the pro-étale site of Bhatt
and Scholze, where $\Zl$ is an honest sheaf of rings
(Sections [sec-proetale-coefficients] and [sec-coefficients-constructible]), and the
second by Brown representability, which produces $f^!$ formally once we
know that the localizing subcategory in question is compactly generated
by constructible complexes and that $Rf_!$ preserves direct sums
(Section [sec-six-functors-basics]).

The point of the pro-étale approach is that the geometry needs to be
done only once, with torsion coefficients, on the étale site, where it
is classical. The comparison theorems carry it to the pro-étale site,
and derived completion and inverting $\ell$ carry it to the other rings.
So the part has the following shape. Two geometric theorems with torsion
coefficients carry the weight. Proper base change
(Section [sec-proper-base-change]) makes $Rf_!$ well defined and
computes its stalks. Deligne's generic base change theorem for $Rj_*$
(Section [sec-constructibility-upper-shriek]), with the calculation of $f^!$
for $\mathbf P^1$ and for closed immersions, gives finiteness of $f^!$.
Around them, Sections [sec-reduction-finite-coefficients] and [sec-six-functors] pass
from torsion to $\ell$-adic coefficients: a constructible complex over
$\mathcal O_E$ is determined by its reductions modulo $\pi_E^n$
(Proposition [sk-prop-integral-criterion]), and a statement that an
exact transformation is an isomorphism may be checked with finite
coefficients (Proposition [sk-prop-reduction-to-finite]). The last
section proves smooth base change, which we need for the Künneth
formula in Part “Duality and the trace formula”.

Throughout this part the base field is finite or algebraically closed,
and Frobenius plays no role.
