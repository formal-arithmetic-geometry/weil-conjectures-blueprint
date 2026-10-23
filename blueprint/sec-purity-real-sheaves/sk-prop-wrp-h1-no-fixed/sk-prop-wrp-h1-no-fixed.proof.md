+++
kind  = "proof"
of    = "sk-prop-wrp-h1-no-fixed"
+++
First let $U_0=C_0$ be proper. By [sk-p-tate], arithmetic Frobenius has no
fixed vector on $T_\ell J$, and $B-1$ is invertible on $V_\ell J$
([lem-wf-finite-field-tate-no-fixed]). The reason is elementary: a fixed
compatible tuple lies at each level in the finite group $J_0(k_0)$, and if
the $\ell$-primary part of this group is killed by $\ell^a$, then
compatibility gives $t_n=\ell^at_{n+a}=0$. Clearing denominators, we obtain
the rational assertion. By [sk-d-real-jacobian], geometric Frobenius
acts on the untwisted $H^1$ by $B^t$. Since
$\det(B^t-1)=\det(B-1)\ne0$, it fixes neither a nonzero rational vector
nor a nonzero integral compatible tuple
([lem-wf-proper-curve-compatible-h1-no-fixed]). The same argument applies
after every finite extension of the ground field.

In the open case, choose $j:U\hookrightarrow C$ as in
[sk-i-real-compactification], with boundary $i:D\hookrightarrow C$.
At each finite level there is a canonical residue sequence

$$
 0\longrightarrow H^1(C,A_n)\longrightarrow H^1(U,A_n)
  \longrightarrow H^0(D,A_n(-1))
$$

([lem-wf-open-curve-residue-sequence]). To obtain it with the correct twist
and Frobenius action, we use the dualizing complexes. Transitivity gives
$i^!\omega_C=\omega_D=A_n$, and since $\omega_C=A_n(1)[2]$
([sk-thm-sf-identification]), it follows that $i^!A_{n,C}=A_{n,D}(-1)[-2]$.
The localization triangle $i_*i^!A_{n,C}\to A_{n,C}\to Rj_*A_{n,U}$
([sk-prop-sf-open-closed-triangle]) now yields the displayed sequence, and
all its maps are natural in the coefficients and under automorphisms of the
model.

Choose $m>0$ such that $F^m$ fixes all geometric boundary points, and
put $Q=q^m$. Then $F^m$ acts as $Q$ on $\varprojlim_nH^0(D,A_n(-1))$.
This module is finite free over $\Zl$ and $Q-1\ne0$, so a fixed element
is zero. Consequently a fixed compatible class on $U$ has zero
residues at every level. By exactness it lifts uniquely to
$H^1(C,A_n)$, and by uniqueness the lifts are compatible and fixed by
$F^m$. The proper case over $\mathbf F_Q$ shows that they vanish
([prop-wf-open-curve-h1-no-frobenius-fixed]).

It remains to pass to rational coefficients. By
[sk-prop-pe-continuous-cohomology], [sk-prop-sfb-qlbar-colimit-x] and the
localization assertion of [sk-cor-pe-bounded-continuity], $H^1(U,\Ql)$ is the
rationalization of this inverse limit ([d-real-cohom]); the
$\varprojlim^1$-term in degree one vanishes because the groups
$H^0(U,A_n)=A_n$ have surjective transition maps. The inverse limit of the
residue sequences is exact on the left, and rationalization is exact.
Rationally, $F^m-1$ is invertible on the proper term and on the boundary
term, hence on the image of the residue map, and therefore also on the
middle term. Thus Frobenius has no fixed rational vector, and
extending scalars to $E$ gives the assertion over $E$.
