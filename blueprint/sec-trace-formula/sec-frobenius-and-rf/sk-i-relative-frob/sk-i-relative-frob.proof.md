+++
kind = "proof"
of = "sk-i-relative-frob"
+++
Since $r_m$ is a universal homeomorphism, pullback along it is an
equivalence and its unit is an isomorphism. The rest is base change
and composition of units.

*Proof of (1).* The map $r_m$ is the geometric base change of the
relative $q^m$-power Frobenius of $X_0/Y_0$. It is integral, radicial
and surjective [Stacks, Tag 0CCB](https://stacks.math.columbia.edu/tag/0CCB), and finite because it is integral and of
finite type. For affine $Y_0=\operatorname{Spec}R$ and
$X_0=\operatorname{Spec}S$, with $F$ the $q$-power Frobenius of $R$,
it is given on coordinate rings by

$$
R\otimes_{F^m,R}S\longrightarrow S,
\qquad b\otimes a\longmapsto f^\#(b)a^{q^m}.
$$

By topological invariance for classical objects of finite Tor amplitude, $r_m^*$
is an equivalence, so the unit $\eta_{r_m}$ in the construction is
an isomorphism. The first arrow is base change for compact supports, and
the last comes from the composition of direct images with compact support, since $r_m$ is
proper.
Pasting the cartesian squares defining $X'_m$ and $X'_n$, we get the
comparison for $m+n$, because the relative Frobenii compose and the unit of
their composite is the composite of the units. Thus

$$
\theta_{f,m+n,K}=
\theta_{f,m,(\Phi_X^n)^*K}\circ
(\Phi_Y^m)^*\theta_{f,n,K},
$$

which is the compatibility with iteration.

*Proof of (2).* The formula for $\psi'_m$ follows by induction on $m$
from the displayed iteration identity and the naturality of $\theta$.

*Proof of (3).* For a finite map $h$ we also write $h^*$ for the pullback
map on cohomology with compact support, defined by the unit of $h^*\dashv Rh_*$.
Since base change is compatible with these units, the pullback along
$\Phi_Y^m$, followed by the base change isomorphism,
is the pullback along $p_m$, and the
next arrow in $\theta_{f,m}$ becomes $r_m^*$. Their composite is
$r_m^*p_m^*=(p_mr_m)^*=(\Phi_X^m)^*$, and
composing with $R\Gamma_c(\psi_m)$ we see that the operators are
intertwined.

*Proof of (4).* We pull the construction back to the fixed point $y$. The base
change of $r_m$ to this fibre is its $q^m$-power scheme Frobenius,
and proper base change carries its unit to the unit on the fibre. Hence the same
calculation identifies $\psi'_{m,\bar y}$ with the Frobenius operator
on the cohomology with compact support of the fibre. At a rational point
$x$ of the fibre, the restricted correspondence $\psi_m|_{X_{\bar y}}$ has
stalk map $\psi_{m,\bar x}$, by composition of pullbacks.
