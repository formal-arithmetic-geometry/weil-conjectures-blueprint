+++
id = "lem-wf-reductive-connected-centre"
kind = "lemma"
title = "A connected central subgroup on a semisimple module is a torus"
order = 4023
uses = ["def-wf-algebraic-character", "def-wf-algebraic-components", "def-wf-algebraic-representations", "def-wf-algebraic-torus", "def-wf-semisimple-module", "def-wf-simple-module", "lem-wf-schur-scalar"]
+++
Let $H\subseteq\operatorname{GL}(V)$ be connected and suppose that
$V$ is a faithful
semisimple $H$-module. Then
$Z(H)^\circ$ is a
torus. In particular, $Z(H)$ is
finite if and only if $Z(H)^\circ=1$.

## Proof

Write $V=\bigoplus_{i=1}^r M_i$ as a direct sum of simple
$H$-modules, using [def-wf-simple-module], [def-wf-semisimple-module].
Every $z\in Z(H)$ preserves each $M_i$ and commutes there with the
$H$-action. Schur's scalar lemma [lem-wf-schur-scalar] therefore
gives scalars $c_i(z)$ with
$z|_{M_i}=c_i(z)1_{M_i}$. The map

$$
\iota:Z(H)^\circ\longrightarrow T_0:=(\mathbf G_m)^r,\qquad
z\longmapsto(c_1(z),\ldots,c_r(z))
$$

is a homomorphism of algebraic groups. It is injective because the
module of [def-wf-algebraic-representations] is faithful. It also
has closed image: the block-scalar embedding
$T_0\hookrightarrow\operatorname{GL}(V)$ identifies the image with
the inverse image of the closed subgroup $Z(H)^\circ$.
Thus $S:=\iota(Z(H)^\circ)$ is a connected closed subgroup of $T_0$.

We now verify directly that every connected closed subgroup of $T_0$
is a torus. Put $k=\overline{\mathbf Q}_\ell$ and
$k[T_0]=k[x_1^{\pm1},\ldots,x_r^{\pm1}]$. Distinct algebraic
characters in the sense of [def-wf-algebraic-character] are
linearly independent. Indeed, from a shortest relation
$\sum_i a_i\chi_i=0$, choose $s$ with
$\chi_1(s)\ne\chi_2(s)$, translate the relation by $s$, and subtract
$\chi_2(s)$ times the original relation; this gives a shorter nonzero
relation.

Set

$$
L:=\{a\in\mathbf Z^r:x^a|_S=1\}.
$$

Group the terms of any Laurent polynomial
$f=\sum_a b_ax^a$ vanishing on $S$ according to the equal restricted
characters. Linear independence shows that the coefficients in each
class sum to zero. Choosing one exponent $a_0$ in that class rewrites
its contribution as

$$
\sum_a b_a(x^a-x^{a_0})
=\sum_a b_ax^{a_0}(x^{a-a_0}-1),
$$

where every $a-a_0$ belongs to $L$. Consequently

$$
I(S)=(x^a-1:a\in L).
$$

By Smith normal form, after changing the basis of $\mathbf Z^r$, and
hence the coordinates of $T_0$, one has
$L=d_1\mathbf Z e_1\oplus\cdots\oplus d_s\mathbf Z e_s$, with
$d_i>0$ and $d_i\mid d_{i+1}$. Thus

$$
S\simeq\mu_{d_1}\times\cdots\times\mu_{d_s}
\times\mathbf G_m^{\,r-s}.
$$

In characteristic zero each $\mu_{d_i}$ is a disjoint union of
$d_i$ points. Since $S$ is connected, every $d_i=1$, and
$S\simeq\mathbf G_m^{\,r-s}$, a torus in the sense of
[def-wf-algebraic-torus]. Finally, translating the identity
component through the finitely many components of a finite-type algebraic
group (the component finiteness of
[def-wf-algebraic-components]) shows directly that the group is a
finite union of such cosets. It
is therefore finite exactly when that component is trivial.
