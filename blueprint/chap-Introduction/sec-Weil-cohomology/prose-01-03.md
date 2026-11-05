+++
id = "prose-01-03"
kind = "hidden"
title = "Weil cohomology"
order = 7
+++
Write $X=X_0\times_{\mathbf F_q}\overline{\mathbf F}_q$, and let
$F:X\to X$ be the *Frobenius*: if $X_0$ is cut out of an affine space by
equations with coefficients in $\mathbf F_q$, then $F$ raises each
coordinate to its $q$-th power. A point of $X$ is fixed by $F^m$ exactly
when its coordinates lie in $\mathbf F_{q^m}$, so
$\#X_0(\mathbf F_{q^m})$ is the number of fixed points of $F^m$. Weil's
idea was to count these fixed points as in topology.

Suppose that we had a cohomology theory with compact supports, assigning to
$X$ finite-dimensional vector spaces $H^i_c(X)$ over a field of
characteristic zero on which $F$ acts. Compact supports are needed because
the trace formula below has to hold for every $X_0$, proper or not: point
counts are additive when $X_0$ is cut into an open subscheme and its
complement, and compactly supported cohomology has the matching long exact
sequence. For proper $X_0$ we write $H^i(X)=H^i_c(X)$; for the conjectures,
which concern smooth proper varieties, this is the only cohomology we need.
Suppose that the theory satisfies the following.

- (a) *Finiteness.* $H^i_c(X)=0$ unless $0\le i\le 2\dim X$.
- (b) *Trace formula.* The fixed points of $F^m$ are counted by a
  Lefschetz formula,
  $$
  \#X_0(\mathbf F_{q^m})=\sum_i(-1)^i\operatorname{Tr}\bigl(F^m\mid H^i_c(X)\bigr).
  $$
- (c) *Poincaré duality.* For smooth proper $X_0$ of pure dimension
  $d$, cup product gives a perfect pairing between $H^i$ and $H^{2d-i}$,
  and $\langle Fx,Fy\rangle=q^d\langle x,y\rangle$. The factor $q^d$ is
  the degree of $F$. It is the scalar by which $F$ acts on the
  one-dimensional space $H^{2d}$ when $X$ is connected.
- (d) *Purity.* For smooth proper $X_0$, the eigenvalues of $F$ on
  $H^i(X)$ are algebraic integers all of whose complex conjugates have
  absolute value $q^{i/2}$.

Then the conjectures follow. For rationality we compare logarithms. For an
endomorphism $F$ of a finite-dimensional vector space $V$ we have

$$
\log\det(1-TF\mid V)^{-1}=\sum_{m\ge1}\operatorname{Tr}(F^m\mid V)\frac{T^m}{m},
$$

as one sees by triangulating $F$: if $F$ has eigenvalues $\alpha_1,\dots,\alpha_b$,
both sides equal $\sum_j\sum_m\alpha_j^mT^m/m$. Substituting the trace formula
(b) into the definition of $Z$ therefore gives

$$
\log Z(X_0,T)=\sum_{m\ge1}\sum_i(-1)^i\operatorname{Tr}\bigl(F^m\mid H^i_c(X)\bigr)\frac{T^m}{m}
=\sum_i(-1)^{i+1}\log\det\bigl(1-TF\mid H^i_c(X)\bigr),
$$

and so

$$
Z(X_0,T)=\prod_i\det\bigl(1-TF\mid H^i_c(X)\bigr)^{(-1)^{i+1}},
$$

a finite product by (a). In particular $Z(X_0,T)$ is rational, and for
smooth proper $X_0$ the polynomial $P_i(T)$ of the conjectures is
$\det(1-TF\mid H^i(X))$. By duality, the
eigenvalues in degree $2d-i$ are the numbers $q^d/\alpha$ for the
eigenvalues $\alpha$ in degree $i$, and this gives the functional equation.
Purity gives the Riemann hypothesis.

Purity also shows that the factors do not depend on the cohomology theory.
Indeed, the factors in different degrees have reciprocal roots of different
absolute values, so no cancellation can occur in the alternating product.
Each factor is therefore determined by $Z(X_0,T)$ alone, and so is its
degree $b_i$.

Which cohomology could this be? On an irreducible scheme a constant sheaf
is flasque, so its Zariski cohomology vanishes in positive degrees. It
cannot see the $2g$ independent loops of a curve of genus $g$. Coherent
cohomology sees $H^1(C,\mathcal O_C)$, of dimension $g$. But this is a
vector space over $\overline{\mathbf F}_q$, and traces on it determine
numbers of points only modulo $p$.

An argument of Serre (see [deninger22]) shows that the coefficient field
cannot be $\mathbf Q$, $\mathbf R$ or $\mathbf Q_p$ either. Let $C$ be a
supersingular elliptic curve over $\overline{\mathbf F}_p$. Then
$D=\operatorname{End}(C)\otimes\mathbf Q$ is a quaternion algebra over
$\mathbf Q$, and $D\otimes\mathbf R$ and $D\otimes\mathbf Q_p$ are still
division algebras [deuring41].
Endomorphisms of $C$ would act on $H^1(C)$, a vector space of dimension
$2g=2$ over the coefficient field $K$. This gives a map of
four-dimensional $K$-algebras $D\otimes K\to M_2(K)$. The map is injective
because $D\otimes K$ is simple, hence it is an isomorphism. That is impossible if
$D\otimes K$ is a division algebra. For $\ell\neq p$, on the other hand,
$D\otimes\mathbf Q_\ell\simeq M_2(\mathbf Q_\ell)$, and the argument does not exclude $\mathbf Q_\ell$.

The theory that works is étale cohomology. Its idea is to replace the
open subsets of the Zariski topology by étale maps $U\to X$, which play the
role of small open neighbourhoods in topology: like a covering space, an
étale map is a local isomorphism in the sense of the implicit function
theorem. A sheaf in this topology assigns a group to every étale map
$U\to X$, compatibly with restriction, and étale cohomology is the derived
functor of global sections. Because there are many more étale maps than
open subsets, a sheaf can now have nonzero cohomology in positive degrees.

For a curve we can already see the missing loops in degree one. Let $C$ be
a smooth projective connected curve of genus $g$ over $\overline{\mathbf F}_q$,
and let $n$ be prime to $q$. Three étale sheaves are involved: $\mathbf G_m$,
which sends $U\to C$ to the unit group $\mathcal O(U)^\times$; the same sheaf
with the $n$th power map $t\mapsto t^n$; and its kernel $\mu_n$, the sheaf of
$n$th roots of unity. The sequence

$$
0\to\mu_n\to\mathbf G_m\xrightarrow{\;t\mapsto t^n\;}\mathbf G_m\to0
$$

is exact in the étale topology. Indeed, surjectivity of a map of sheaves
only has to hold locally, and an $n$th root of a unit $a$ exists on the
étale cover defined by $t^n=a$, which is étale because $n$ is invertible.
(In the Zariski topology the last map is not surjective.) As in the Zariski
topology, $H^1(C_{\acute{e}t},\mathbf G_m)$ is the Picard group of $C$ (Hilbert's
Theorem 90). The global units of $C$ are $\overline{\mathbf F}_q^\times$, in which
$n$th roots exist, so $H^0(\mathbf G_m)\xrightarrow{n}H^0(\mathbf G_m)$ is
surjective. The long exact sequence therefore identifies
$H^1(C_{\acute{e}t},\mu_n)$ with the kernel of multiplication by $n$ on
$H^1(C_{\acute{e}t},\mathbf G_m)=\operatorname{Pic}(C)$.

To compute this kernel we use the degree. It gives an exact sequence
$0\to\operatorname{Pic}^0(C)\to\operatorname{Pic}(C)\xrightarrow{\deg}\mathbf Z\to0$,
and since $\mathbf Z$ has no torsion, every line bundle killed by $n$ has
degree zero. So $\operatorname{Pic}(C)[n]=\operatorname{Pic}^0(C)[n]$. The group
$\operatorname{Pic}^0(C)$ is the group of points of the *Jacobian* $J$ of
$C$, an abelian variety of dimension $g$ (Section [sec-The-Jacobian]), and on an
abelian variety of dimension $g$ the $n$-torsion points form a group
$(\mathbf Z/n)^{2g}$ when $n$ is prime to the characteristic
(Proposition [proposition-integral-tate-module]). Altogether,

$$
H^1(C_{\acute{e}t},\mu_n)\simeq\operatorname{Pic}(C)[n]=J[n]\simeq(\mathbf Z/n)^{2g}
$$

(Proposition [proposition-smooth-proper-curves-torsion-prime]), which is the
size of $H^1$ of a compact Riemann surface of genus $g$ with coefficients
$\mathbf Z/n$. Now let $n=\ell^k$ and let $k\to\infty$. The groups $J[\ell^k]$, with the
maps $J[\ell^{k+1}]\to J[\ell^k]$ given by multiplication by $\ell$, form the
*Tate module* $T_\ell J=\varprojlim_kJ[\ell^k]$, free of rank $2g$ over
$\mathbf Z_\ell$ (Proposition [proposition-integral-tate-module]). On the cohomology
side these maps correspond to $\mu_{\ell^{k+1}}\to\mu_{\ell^k}$, $z\mapsto z^\ell$,
so the identification above passes to the limit:

$$
\varprojlim_kH^1(C_{\acute{e}t},\mu_{\ell^k})\simeq T_\ell J
$$

(Proposition [proposition-h-1-curve-tate-module]). In other words, the
Tate module is the first cohomology of $C$ with coefficients in the inverse
system $(\mu_{\ell^k})_k$, which is written $\mathbf Z_\ell(1)$ (we come back to what
this limit means below). Weil used $T_\ell J$ in his proof for curves, in
place of an $H^1$ that was not yet available.

Frobenius acts on both sides. Let $\pi$ be the endomorphism of $J$ induced by
Frobenius; it raises the coordinates of torsion points to the $q$-th power,
and under the isomorphism above it is the action of the arithmetic
Frobenius $\sigma:z\mapsto z^q$ in $\operatorname{Gal}(\overline{\mathbf F}_q/\mathbf F_q)$
on the torsion points. The map $F$ on cohomology is pullback along the
Frobenius of $C$, which is the inverse of this Galois action on
$\overline{\mathbf F}_q$-points (we compare the two Frobenius maps in
Section [sec-Frobenius-correspondences]). Hence $F$ acts on
$\varprojlim_kH^1(C_{\acute{e}t},\mu_{\ell^k})$ by $\pi^{-1}$. Weil showed [weil48-av] that the characteristic polynomial of $\pi$ on
$T_\ell J$ has integer coefficients, and that the numerator of the zeta
function is

$$
P_1(T)=\det(1-T\pi\mid T_\ell J).
$$

Because of the twist, $F$ acts on the untwisted group $H^1(C,\mathbf Q_\ell)$ by
$q\pi^{-1}$ (Section [sec-Weil-complexes]). Its eigenvalues $q/\alpha$ run
through the eigenvalues $\alpha$ of $\pi$ again, by the functional equation, so
also $P_1(T)=\det(1-TF\mid H^1(C,\mathbf Q_\ell))$, as predicted in
Section [sec-The-Weil-conjectures]. For the curve $C_0$ above,
$\pi$ acts on $T_\ell J$ with characteristic polynomial $T^2+3$, and indeed
$P_1(T)=1+3T^2$.

The example suggests how to obtain a theory with coefficients of
characteristic zero: compute étale cohomology with the finite coefficients
$\mathbf Z/\ell^k$, where the theory works, take the inverse limit over $k$
to obtain $\mathbf Z_\ell$-modules, and finally invert $\ell$. The limit has to be
taken with care, as $\operatorname{Spec}\mathbf F_q$ already shows. On it, étale sheaves are sets with a continuous action of
the Galois group $\widehat{\mathbf Z}$, and $H^1$ with coefficients in an
abelian group $A$ is the group of continuous homomorphisms
$\widehat{\mathbf Z}\to A$. For $A=\mathbf Z/\ell^k$ this is $\mathbf Z/\ell^k$,
and the limit of these groups is $\mathbf Z_\ell$. But the étale topology sees $\mathbf Z_\ell$
only as a discrete group, and a continuous homomorphism from the compact group
$\widehat{\mathbf Z}$ to the discrete torsion-free group $\mathbf Z_\ell$ is zero, so
the constant sheaf $\mathbf Z_\ell$ has $H^1=0$. What one wants, therefore, is the limit of the
cohomology groups, not the cohomology of the limit sheaf. After inverting
$\ell$ this gives a theory with coefficients in $\mathbf Q_\ell$. However, the eigenvalues of
Frobenius lie in an algebraic closure $\overline{\mathbf Q}_\ell$ of $\mathbf Q_\ell$ rather than in $\mathbf Q_\ell$
itself, and so we also allow coefficients in $\overline{\mathbf Q}_\ell$, where characteristic
polynomials split.

The resulting theory is $\ell$-adic cohomology, for a prime $\ell$ not dividing $q$. It was
constructed by Grothendieck and his collaborators, who proved (a), (b) and
(c) for it in SGA 4 and SGA 5 [sga4], [sga5]. Purity (d) is the hard part,
and Deligne proved it [deligne74], [deligne80]. The general form of
his theorem, on weights of $Rf_!$, was later reproved by Laumon with the
$\ell$-adic Fourier transform [laumon87] (see also [katz88], [kiehl-weissauer01]); we call it the
Deligne–Laumon theorem. Our proof uses the Fourier transform as Laumon does,
but it is organized differently in places.

Of statement (4) we prove that $b_i=b_{2d-i}$. We also prove that
$b_i=\dim H^i(X,\mathbf Q_\ell)$ for every $\ell$ not dividing $q$; in particular this
dimension does not depend on $\ell$
(Theorem [theorem-weil-conjectures-smooth-proper-schemes]). The comparison
with the Betti numbers of a lift to characteristic zero needs the comparison
theorem between étale and singular cohomology, which we do not prove.
