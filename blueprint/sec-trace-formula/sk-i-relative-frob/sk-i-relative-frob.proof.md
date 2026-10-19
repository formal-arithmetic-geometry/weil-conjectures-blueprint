+++
kind = "proof"
of = "sk-i-relative-frob"
+++
*Item (1).* The map $r_m$ is the geometric base change of the
relative $q^m$-power Frobenius of $X_0/Y_0$. It is integral, radicial
and surjective
([Stacks, Tag 0CCB](https://stacks.math.columbia.edu/tag/0CCB)), and finite because it is integral and of
finite type. For affine $Y_0=\operatorname{Spec}R$ and
$X_0=\operatorname{Spec}S$, with $F$ the $q$-power Frobenius of $R$,
it is given on coordinate rings by

$$
 R\otimes_{F^m,R}S\longrightarrow S,
 \qquad b\otimes a\longmapsto f^\#(b)a^{q^m}.
$$

By topological invariance on classical finite-Tor objects, $r_m^*$
is an equivalence, so the unit $\eta_{r_m}$ in the construction is
an isomorphism. The first arrow is compact-support base change, and
the last is composition of $!$-pushforward, using that $r_m$ is
proper.
Pasting the Cartesian squares defining $X'_m$ and $X'_n$ gives the
comparison for $m+n$: the relative Frobenii compose, and the unit of
their composite is the composite of the units. Thus

$$
 \theta_{f,m+n,K}=
 \theta_{f,m,(\Phi_X^n)^*K}\circ
 (\Phi_Y^m)^*\theta_{f,n,K},
$$

which is the compatibility with iteration.

*Item (2).* The displayed iteration identity and the naturality
of $\theta$ give the formula for $\psi'_m$ by induction on $m$.

*Item (3).* Write $h^\sharp$ for compact pullback along
a finite map $h$, defined by its ordinary unit. Compatibility of base
change with these units identifies compact pullback along
$\Phi_Y^m$, followed by the base-change isomorphism
$\operatorname{Ex}_!$, with compact pullback along $p_m$, and the
next arrow in $\theta_{f,m}$ becomes $r_m^\sharp$. Their composite is
$r_m^\sharp p_m^\sharp=(p_mr_m)^\sharp=(\Phi_X^m)^\sharp$, and
postcomposing with $R\Gamma_c(\psi_m)$ gives the intertwining of the
operators.

*Item (4).* Pull the construction back to the fixed point $y$. The base
change of $r_m$ to this fibre is its $q^m$-power scheme Frobenius,
and proper base change carries its unit to the fibre unit. The same
calculation therefore identifies $\psi'_{m,\bar y}$ with the compact
Frobenius operator of the fibre. Its stalk map at a rational point
$x$ of the fibre is $\psi_{m,\bar x}$, by composition of pullbacks.
