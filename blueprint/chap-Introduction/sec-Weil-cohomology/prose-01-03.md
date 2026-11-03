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

Suppose that we had a cohomology theory assigning to $X$
finite-dimensional vector spaces $H^i(X)$ over a field of
characteristic zero, on which $F$ acts, together with a version with
compact supports, $H^i_c(X)$, which agrees with $H^i(X)$ when $X_0$ is
proper. Suppose that it satisfies the following.

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

Then the conjectures follow. Taking logarithms in the trace formula shows
that $Z(X_0,T)$ is the alternating product of the polynomials
$\det(1-TF\mid H^i_c(X))$. In particular it is rational. By duality, the
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
numbers of points only modulo $p$. Serre showed that the
coefficient field cannot be $\mathbf Q$, $\mathbf R$ or $\mathbf Q_p$ either.
If $C$ is a supersingular elliptic curve over $\overline{\mathbf F}_p$, then
$D=\operatorname{End}(C)\otimes\mathbf Q$ is a quaternion algebra over
$\mathbf Q$, and $D\otimes\mathbf R$ and $D\otimes\mathbf Q_p$ are still
division algebras (Deuring).
Endomorphisms of $C$ would act on $H^1(C)$, a vector space of dimension
$2g=2$ over the coefficient field $K$. This gives a map of
four-dimensional $K$-algebras $D\otimes K\to M_2(K)$. The map is injective
because $D\otimes K$ is simple, hence it is an isomorphism. That is impossible if
$D\otimes K$ is a division algebra. For $\ell\neq p$, on the other hand,
$D\otimes\mathbf Q_\ell\simeq M_2(\mathbf Q_\ell)$, and the argument does not exclude $\mathbf Q_\ell$.

Étale cohomology, the theory that works, replaces open subsets by étale
maps $U\to X$. For a curve it already finds the missing loops. Let $C$ be a
smooth projective connected curve of genus $g$ over $\overline{\mathbf F}_q$,
with Jacobian $J$, and let $n$ be prime to $q$. The sequence

$$
0\to\mu_n\to\mathbf G_m\xrightarrow{\;t\mapsto t^n\;}\mathbf G_m\to0
$$

is exact in the étale topology, because an $n$th root of a unit $a$
exists on the étale cover defined by $t^n=a$. As in the Zariski
topology, $H^1(C_{\acute{e}t},\mathbf G_m)$ is the Picard group of $C$ (Hilbert's
Theorem 90). The global units of $C$ are $\overline{\mathbf F}_q^\times$, in
which $n$th roots exist, so the long exact sequence identifies
$H^1(C_{\acute{e}t},\mu_n)$ with the $n$-torsion of $\operatorname{Pic}(C)$. Since
$\operatorname{Pic}(C)/\operatorname{Pic}^0(C)\simeq\mathbf Z$ has no torsion,
this is the $n$-torsion of the Jacobian:

$$
H^1(C_{\acute{e}t},\mu_n)\simeq\operatorname{Pic}(C)[n]=J[n]\simeq(\mathbf Z/n)^{2g}
$$

(Proposition [proposition-smooth-proper-curves-torsion-prime]). The last
isomorphism is a fact about abelian varieties of dimension $g$. Taking
$n=\ell^k$ and letting $k\to\infty$, one obtains the Tate module $T_\ell J$,
free of rank $2g$ over $\mathbf Z_\ell$ (Proposition [proposition-integral-tate-module]).
It is $H^1$ of $C$ with coefficients $\varprojlim_k\mu_{\ell^k}$. Weil used
it in his proof for curves. Let $\pi$ be the endomorphism of $J$ induced by
Frobenius; it raises the coordinates of torsion points to the $q$-th
power. Then $P_1(T)=\det(1-T\pi\mid T_\ell J)$. For the curve $C_0$ above,
$\pi$ acts on $T_\ell J$ with characteristic polynomial $T^2+3$, and indeed
$P_1(T)=1+3T^2$.

So one takes coefficients $\mathbf Z/\ell^k$ first and then passes to the
limit. The limit cannot be taken naively, as $\operatorname{Spec}\mathbf F_q$
already shows. On it, étale sheaves are sets with a continuous action of
the Galois group $\widehat{\mathbf Z}$, and $H^1$ with coefficients in an
abelian group $A$ is the group of continuous homomorphisms
$\widehat{\mathbf Z}\to A$. For $A=\mathbf Z/\ell^k$ this is $\mathbf Z/\ell^k$,
and the limit of these groups is $\mathbf Z_\ell$. But the étale topology sees $\mathbf Z_\ell$
only as a discrete group. A continuous homomorphism from the compact group
$\widehat{\mathbf Z}$ to the discrete torsion-free group $\mathbf Z_\ell$ is zero, so
the constant sheaf $\mathbf Z_\ell$ has $H^1=0$. What one wants is the limit of the
cohomology groups, not the cohomology of the limit sheaf. After inverting
$\ell$ this gives a theory with coefficients in $\mathbf Q_\ell$. The eigenvalues of
Frobenius lie in an algebraic closure $\overline{\mathbf Q}_\ell$ of $\mathbf Q_\ell$ rather than in $\mathbf Q_\ell$
itself, and so we also allow coefficients in $\overline{\mathbf Q}_\ell$, where characteristic
polynomials split.

The resulting theory is $\ell$-adic cohomology, for a prime $\ell$ not dividing $q$. It was
constructed by Grothendieck and his collaborators, who proved (a), (b) and
(c) for it in SGA 4 and SGA 5 [sga4], [sga5]. Purity (d) is the hard part,
and Deligne proved it [deligne74], [deligne80]. We follow Laumon's
proof [laumon87], which uses the Fourier transform.

Of statement (4) we prove that $b_i=b_{2d-i}$. We also prove that
$b_i=\dim H^i(X,\mathbf Q_\ell)$ for every $\ell$ not dividing $q$; in particular this
dimension does not depend on $\ell$
(Theorem [theorem-weil-conjectures-smooth-proper-schemes]). The comparison
with the Betti numbers of a lift to characteristic zero needs the comparison
theorem between étale and singular cohomology, which we do not prove.
