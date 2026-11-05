+++
kind = "proof"
of = "lemma-comparison-via-relative-frobenius"
order = 1000
+++
The only geometric fact we use is that, since $r_m$ is a universal
homeomorphism, pullback along it is an equivalence and its unit is an
isomorphism. The rest is base change and composition of units, and each
part uses the previous ones.

*Proof of (1).* The identities $p_mr_m=\Phi_X^m$ and $f'_mr_m=f$
hold by the definition of $r_m=(f,\Phi_X^m)$, since $f\Phi_X^m=\Phi_Y^mf$.
The map $r_m$ is the geometric base change of the
relative $q^m$-power Frobenius of $X_0/Y_0$. It is integral, radicial
and surjective [Stacks, [0CCB](https://stacks.math.columbia.edu/tag/0CCB)], and finite because it is integral and of
finite type. For affine $Y_0=\operatorname{Spec}R$ and
$X_0=\operatorname{Spec}S$, with $F$ the $q$-power Frobenius of $R$,
it is given on coordinate rings by

$$
R\otimes_{F^m,R}S\longrightarrow S,
\qquad b\otimes a\longmapsto f^\#(b)a^{q^m}.
$$

By topological invariance for classical objects of finite Tor amplitude, $r_m^*$
is an equivalence, so the unit $\eta_{r_m}$ in the construction is
an isomorphism. In the construction, the first arrow is base change for compact supports, and
the last comes from the composition of direct images with compact support, since $r_m$ is
proper.
Moreover, pasting the cartesian squares defining $X'_m$ and $X'_n$, we get the
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

*Proof of (3).* Both endomorphisms are a pullback map followed by
$R\Gamma_c$ of the correspondence, so we must see that the pullback along
$\Phi_Y^m$ on $R\Gamma_c(Y,L)$ becomes the pullback along $\Phi_X^m$
on $R\Gamma_c(X,K)$. For a finite map $h$ we also write $h^*$ for the pullback
map on cohomology with compact support, defined by the unit of $h^*\dashv Rh_*$.
Since base change is compatible with these units, the pullback along
$\Phi_Y^m$, followed by the base change isomorphism,
is the pullback along $p_m$, and the
next arrow in $\theta_{f,m}$ becomes $r_m^*$. Their composite is
$r_m^*p_m^*=(p_mr_m)^*=(\Phi_X^m)^*$, and
composing with $R\Gamma_c(\psi_m)$ we see that the operators are
intertwined.

*Proof of (4).* We pull the construction back to the fixed point
$y$. Since $\Phi_Y^m$ fixes $\bar y$, the fibre of $X'_m\to Y$ over
$\bar y$ is again the fibre $X_{\bar y}$ of $f$, and $r_m$ restricts to
a self-map of $X_{\bar y}$. For $f:\mathbf A^1\to s$ and $m=1$, for
instance, $X'_1=\mathbf A^1$ and $r_1$ is $t\mapsto t^q$. In general, the base change of $r_m$ to this fibre is its $q^m$-power scheme Frobenius,
and by proper base change its unit restricts to the unit on the fibre. Hence the same
calculation identifies $\psi'_{m,\bar y}$ with the Frobenius operator
on the cohomology with compact support of the fibre. Moreover, at a rational point $x$ of the fibre, the restricted correspondence $\psi_m|_{X_{\bar y}}$ has
stalk map $\psi_{m,\bar x}$, by composition of pullbacks.
