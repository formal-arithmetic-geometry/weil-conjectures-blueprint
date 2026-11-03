+++
id = "prose-01-03"
kind = "hidden"
title = "A cohomology that counts points"
order = 7
+++
Weil also explained why the conjectures should be true. Suppose that
there is a cohomology theory for varieties over
$\overline{\mathbf F}_q$, assigning to $X=X_0\times_{\mathbf F_q}\overline{\mathbf F}_q$
finite-dimensional vector spaces $H^i_c(X)$ over a field of
characteristic zero, on which the Frobenius $F$ of $X_0$ acts. These are
cohomology groups with compact supports, and they agree with the
ordinary cohomology groups $H^i(X)$ when $X_0$ is proper. The theory
should satisfy the following.

- (a) *Finiteness.* $H^i_c(X)=0$ unless $0\le i\le 2\dim X$.
- (b) *Trace formula.* The points of $X_0$ over
  $\mathbf F_{q^m}$ are the fixed points of $F^m$, and they are counted
  by a Lefschetz formula,

$$
\#X_0(\mathbf F_{q^m})=\sum_i(-1)^i\operatorname{Tr}\bigl(F^m\mid H^i_c(X)\bigr).
$$

- (c) *Poincaré duality.* For smooth proper $X_0$ of pure dimension
  $d$, cup product gives a perfect pairing between $H^i$ and $H^{2d-i}$,
  and $\langle Fx,Fy\rangle=q^d\langle x,y\rangle$.
- (d) *Purity.* For smooth proper $X_0$, the eigenvalues of $F$ on
  $H^i(X)$ are algebraic integers all of whose complex conjugates have
  absolute value $q^{i/2}$.

Then (a) and (b) imply rationality: taking logarithms of both sides of
the trace formula, we see that $Z(X_0,T)$ is the alternating product of
the polynomials $\det(1-TF\mid H^i_c(X))$. Duality (c) says that the eigenvalues in degree
$2d-i$ are the $q^d/\alpha$ for the eigenvalues $\alpha$ in degree $i$,
and the functional equation follows. Purity (d) implies the Riemann
hypothesis, and more: since the factors in different degrees
have roots of different absolute values, they cannot cancel in the
alternating product, so they are determined by $Z(X_0,T)$ alone. In
particular they have integer coefficients and do not depend on the
cohomology theory, which gives the first half of statement (4).

Which cohomology could this be? The obvious candidates fail. On an
irreducible scheme every constant sheaf is flasque, so Zariski cohomology
with constant coefficients vanishes in positive degrees: the Zariski
topology is too coarse to see the $2g$ cycles of a curve of genus $g$.
Coherent cohomology of such a curve $C$ sees $H^1(C,\mathcal O_C)$, of
dimension $g$, but it
is a vector space over $\overline{\mathbf F}_q$, so traces of Frobenius
on it determine numbers of points only modulo $p$. Serre observed that
the coefficient field cannot be too small either. If $C$ is a
supersingular elliptic curve over $\overline{\mathbf F}_p$, then
$\operatorname{End}(C)\otimes\mathbf Q$ is a quaternion algebra over
$\mathbf Q$ ramified exactly at $p$ and $\infty$. It would act faithfully
on the two-dimensional space $H^1(C)$, so the coefficient field must
split it. This excludes $\mathbf Q$, $\mathbf R$ and $\mathbf Q_p$, but
not $\mathbf Q_\ell$ for $\ell\neq p$.

Curves show what to do instead. Let $C$ be a smooth projective connected
curve of genus $g$ over $\overline{\mathbf F}_q$, let $J$ be its
Jacobian, and let $n$ be prime to $q$. A $\mu_n$-torsor on $C$ is a
finite étale cover, invisible to the Zariski topology, and the Kummer
sequence $0\to\mu_n\to\mathbf G_m\xrightarrow{n}\mathbf G_m\to0$ on the
étale site gives

$$
H^1(C_{\acute{e}t},\mu_n)\simeq\operatorname{Pic}(C)[n]=J[n]\simeq(\mathbf Z/n)^{2g}
$$

(Proposition [sk-thm-curveestimate]). These are the $2g$ missing cycles.
For $n=\ell^k$ and $k\to\infty$ one obtains the Tate module $T_\ell J$,
free of rank $2g$ over $\Zl$ (Proposition [sk-prop-av-tate-rank]), which
Weil used in his proof for curves. For the curve $C_0$ above, Frobenius
acts on $T_\ell J$ with characteristic polynomial $T^2+3$, the reciprocal
polynomial of $P_1(T)=1+3T^2$; this curve is supersingular, as in
Serre's argument. Étale cohomology extends this to all
degrees and all varieties: étale maps play the role of small open
sets, so that cohomology with torsion coefficients sees the topology, and
passing to $\Zl=\varprojlim_k\mathbf Z/\ell^k$ and inverting $\ell$ gives
coefficients in $\Ql$.

Grothendieck constructed such a theory: $\ell$-adic cohomology, for a
prime $\ell$ not dividing $q$. He and his collaborators proved (a), (b) and (c) in
SGA 4 and SGA 5 [sga4, SGA5], and this proves rationality and the
functional equation (Section [sec-tf-determinants]). Purity (d) is the hard
part. It was proved by Deligne [deligne74], and later in a
more general form [deligne80]. We follow the proof of Deligne's
theorem on weights by the Fourier transform, due to Laumon [laumon87]. Its main idea is to
prove an upper bound for the absolute values of the Frobenius
eigenvalues (the *weights*) on the cohomology with compact supports
of the fibres of every morphism $f$, with coefficients in every mixed
$\ell$-adic sheaf. Duality then turns the upper bound into purity.

We prove two parts of the statement (4) on Betti numbers: that
$b_i=b_{2d-i}$, and that $b_i=\dim H^i(X,\Ql)$ for every $\ell$ not
dividing $q$, so that this dimension does not depend on $\ell$ (Theorem [sk-thm-weil-final]). The comparison
of $b_i$ with the Betti numbers of a lift to characteristic zero needs
the comparison theorem between étale and singular cohomology, which
we do not prove.
