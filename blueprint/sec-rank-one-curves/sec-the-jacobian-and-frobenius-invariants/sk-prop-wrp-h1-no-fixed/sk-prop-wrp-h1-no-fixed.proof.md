+++
kind = "proof"
of = "sk-prop-wrp-h1-no-fixed"
+++
A Frobenius-fixed vector in the Tate module would
give $\ell$-power torsion points of arbitrarily high order in the
finite group $J_0(k_0)$, while on the boundary Frobenius acts by a
power of $q$, which is not $1$.

*The proper case.* Let $U_0=C_0$ be proper. By
Proposition [sk-p-tate], arithmetic Frobenius has no
fixed vector on $T_\ell J$, since a fixed compatible tuple would
consist of $\ell$-power torsion points of the finite group $J_0(k_0)$,
and hence $B-1$ is invertible on $V_\ell J$. By
Proposition [sk-d-real-jacobian], geometric Frobenius
acts on the untwisted $H^1$ by $B^t$. Since
$\det(B^t-1)=\det(B-1)\ne0$, it fixes neither a nonzero rational vector
nor a nonzero integral compatible tuple. The proposition applies to
every power of Frobenius, so this also holds over every finite
extension of $k_0$, which the open case needs.

*The open case.* Choose $j:U\hookrightarrow C$ as in
Lemma [sk-i-real-compactification], with boundary $i:D\hookrightarrow C$.
At each finite level there is a canonical residue sequence

$$
0\longrightarrow H^1(C,A_n)\longrightarrow H^1(U,A_n)
\longrightarrow H^0(D,A_n(-1)).
$$

To obtain it with the correct twist and Frobenius action, we use the
dualizing complexes. By transitivity, $i^!\omega_C=\omega_D=A_n$,
and since $\omega_C=A_n(1)[2]$, it follows that
$i^!A_{n,C}=A_{n,D}(-1)[-2]$. The localization triangle
$i_*i^!A_{n,C}\to A_{n,C}\to Rj_*A_{n,U}$ now yields the displayed
sequence, and all its maps are natural in the coefficients and under
automorphisms of the model.

Choose $m>0$ such that $F^m$ fixes all geometric boundary points, and
put $Q=q^m$. Then $F^m$ acts as $Q$ on $\varprojlim_nH^0(D,A_n(-1))$.
Since this module is finite free over $\Zl$ and $Q-1\ne0$, a fixed
element is zero. Consequently a fixed compatible class on $U$ has zero
residues at every level. By exactness it lifts uniquely to
$H^1(C,A_n)$, and by uniqueness the lifts are compatible and fixed by
$F^m$. The proper case over $\mathbf F_Q$ shows that they vanish.

*Rational coefficients.* By
Proposition [sk-prop-pe-continuous-cohomology], applied to the constant
sheaves $A_n$, we have $R\Gamma(U,\Zl)=R\varprojlim_nR\Gamma(U,A_n)$,
and hence an exact sequence

$$
0\to\varprojlim\nolimits^1_nH^0(U,A_n)\to H^1(U,\Zl)
\to\varprojlim_nH^1(U,A_n)\to0.
$$

The $\varprojlim^1$-term vanishes because the groups $H^0(U,A_n)=A_n$
have surjective transition maps. On $U_{\mathrm{pro}\acute{e}t}$ the sheaf $\Ql$ is
$\Zl[1/\ell]$ (Lemma [sk-prop-sfb-qlbar-colimit-x]), a filtered
colimit of copies of $\Zl$, and cohomology on the quasi-compact scheme
$U$ commutes with filtered colimits
(Lemma [sk-lem-proper-heart-continuity]). Hence we get $H^1(U,\Ql)=H^1(U,\Zl)\otimes\Ql$. Thus $H^1(U,\Ql)$ is the
rationalization of the inverse limit. The inverse limit of the residue sequences is exact
on the left, and rationalization is exact. Rationally, $F^m-1$ is
invertible on the proper term and on the boundary term, hence on the
image of the residue map (an injective endomorphism of a
finite-dimensional space), and therefore also on the middle term.
Since a vector fixed by $F$ is fixed by $F^m$, Frobenius has no fixed
rational vector, and extending scalars to $E$ we obtain the assertion
over $E$.
