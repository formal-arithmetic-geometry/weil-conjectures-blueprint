+++
kind = "proof"
of = "proposition-no-fixed-class-degree-one"
order = 1092
+++
On the compactification the vanishing holds because
$J_0(k_0)$ is finite, and on the boundary it holds because Frobenius
acts by a power of $q$, which is not $1$. The residue sequence reduces the
open case to the proper one, and at the end we pass from integral to
rational coefficients.

*The proper case.* Let $U_0=C_0$ be proper, with Jacobian $J_0$.
Here the cohomology is the dual of the Tate module, and the question is
whether $1$ is an eigenvalue of Frobenius on it.  By
Proposition [proposition-no-frobenius-fixed-vector], arithmetic Frobenius has no
fixed vector on $T_\ell J$. Indeed, a fixed compatible tuple would
consist of $\ell$-power torsion points of the finite group $J_0(k_0)$.
This means that $B-1$ is invertible on $V_\ell J$.  Geometric Frobenius
acts on the untwisted $H^1$ by $B^t$
(Proposition [proposition-kummer-duality-integral-tate-module]). Since
$\det(B^t-1)=\det(B-1)\ne0$, it fixes neither a nonzero rational vector
nor a nonzero integral compatible tuple.  The argument applies to
every power of Frobenius, so the same holds over every finite
extension of $k_0$. We need this in the open case.

*The open case.* A fixed class has zero residues at
the boundary points, so it extends to the compactification, where the
proper case shows that it is zero. Choose $j:U\hookrightarrow C$ as in
Lemma [lemma-proper-smooth-model], with boundary $i:D\hookrightarrow C$.
At each finite level there is a canonical residue sequence

$$
0\longrightarrow H^1(C,A_n)\longrightarrow H^1(U,A_n)
\longrightarrow H^0(D,A_n(-1)).
$$

To obtain it with the correct twist and Frobenius action, we use the
dualizing complexes.  By transitivity, $i^!\omega_C=\omega_D=A_n$.
Since $\omega_C=A_n(1)[2]$, it follows that
$i^!A_{n,C}=A_{n,D}(-1)[-2]$.  The localization triangle
$i_*i^!A_{n,C}\to A_{n,C}\to Rj_*A_{n,U}$ now yields the displayed
sequence. All its maps are natural in the coefficients and under
automorphisms of the model.

Choose $m>0$ such that $F^m$ fixes all geometric boundary points, and
put $Q=q^m$.  On $\varprojlim_nH^0(D,A_n(-1))$, which is finite free
over $\mathbf Z_\ell$, the operator $F^m$ acts as $Q$. Since $Q-1\ne0$, it has no
nonzero fixed element. A fixed compatible class on $U$ therefore has zero
residues at every level. By exactness it lifts uniquely to
$H^1(C,A_n)$. By uniqueness the lifts are compatible and fixed by
$F^m$, and the proper case over $\mathbf F_Q$ shows that they vanish.

*Rational coefficients.* To pass from compatible systems of classes
to $H^1(U,E)$, we identify $H^1(U,\mathbf Q_\ell)$ with the rationalization of the
inverse limit and check that rationalizing does not create fixed vectors. By
Proposition [proposition-continuous-cohomology-pro-etale-cohomology], applied to the constant
sheaves $A_n$, we have $R\Gamma(U,\mathbf Z_\ell)=R\varprojlim_nR\Gamma(U,A_n)$,
and hence an exact sequence

$$
0\to\varprojlim\nolimits^1_nH^0(U,A_n)\to H^1(U,\mathbf Z_\ell)
\to\varprojlim_nH^1(U,A_n)\to0.
$$

The $\varprojlim^1$-term vanishes because the groups $H^0(U,A_n)=A_n$
have surjective transition maps.  On $U_{\mathrm{pro}\acute{e}t}$ the sheaf $\mathbf Q_\ell$ is
$\mathbf Z_\ell[1/\ell]$ (Lemma [lemma-comparison-completed-coefficients]), a filtered
colimit of copies of $\mathbf Z_\ell$, and cohomology on the quasi-compact and
quasi-separated scheme $U$ commutes with filtered colimits of sheaves
(Corollary [corollary-continuity-cohomology], applied to sheaves placed
in degree zero).  So $H^1(U,\mathbf Q_\ell)=H^1(U,\mathbf Z_\ell)\otimes\mathbf Q_\ell$ is the
rationalization of the inverse limit.

The inverse limit of the residue sequences is exact on the left, and
rationalization is exact. We obtain an exact sequence of finite-dimensional
$\mathbf Q_\ell$-spaces $0\to H^1(C,\mathbf Q_\ell)\to H^1(U,\mathbf Q_\ell)\to I\to0$, where $I$ is the image
of the residue map inside the rationalized boundary term. By the proper case,
$F^m-1$ is invertible on $H^1(C,\mathbf Q_\ell)$. On the boundary term $F^m-1$ acts by
$Q-1$, so it is injective on the $F^m$-stable subspace $I$. Now let $v$ be a
vector of $H^1(U,\mathbf Q_\ell)$ killed by $F^m-1$. Its image in $I$ is killed by
$F^m-1$, hence zero. So $v$ comes from $H^1(C,\mathbf Q_\ell)$, where it is zero by the
proper case. A vector fixed by $F$ is fixed by $F^m$, and therefore Frobenius
has no fixed rational vector. Extending scalars to $E$ gives the assertion
over $E$.
