+++
id = "situation-weil"
kind = "hidden"
title = "Convention"
order = 1056
+++
**Convention.** Put $k_0=\mathbf F_q$, $k=\overline{\mathbf F}_q$, and fix a prime
$\ell\nmid q$ and a field embedding $\iota:\overline{\mathbf Q}_\ell\hookrightarrow\mathbf C$.
For $X_0/k_0$ separated of finite type, we write $X=X_0\times_{k_0}k$,
and for a closed point $x$ of $X_0$ write $\deg(x)=[\kappa(x):k_0]$ for
its degree and $q_x=q^{\deg(x)}=\#\kappa(x)$. Moreover, geometric Frobenius, Weil complexes and their Frobenius operators are those of
Section [sec-Weil-complexes]. As there, a Weil sheaf is a Weil complex concentrated in degree zero, and the six operations carry Weil structures to Weil
structures. In this Part Weil sheaves and complexes have coefficients in
$\overline{\mathbf Q}_\ell$; a Weil complex $K$ with coefficients in a finite extension
$E\subset\overline{\mathbf Q}_\ell$ of $\mathbf Q_\ell$ is called pure, mixed, or of weights at most $w$ if
$K\otimes_E\overline{\mathbf Q}_\ell$ is (see Lemma [lemma-weil-sheaves-point-mixed] and the
remark after it for why scalars must be extended).

On a connected normal scheme of finite type over a field, we identify a
lisse $E$-sheaf with the corresponding continuous representation of the
profinite fundamental group, by
Proposition [proposition-lattices-representations-normal-scheme], proved in
Section [sec-Lisse-sheaves-as-representations] below. This covers all arguments with representations below, since they take place on smooth schemes. Moreover, a lisse Weil $\overline{\mathbf Q}_\ell$-sheaf has a lisse Weil model over some finite extension
$E/\mathbf Q_\ell$, and two models become identified after a finite extension of
scalars. This model includes the Weil isomorphism, which need not
preserve a geometric $\mathcal O_E$-lattice.

For a geometrically connected smooth curve $U_0$, put $U=U_0\times_{k_0}k$
and choose a geometric point $\bar\eta$ of $U$. We then write $\pi_1(U)$ and $\pi_1(U_0)$ for $\pi_1(U,\bar\eta)$ and $\pi_1(U_0,\bar\eta)$.  The inverse image
of the integer powers of geometric Frobenius in $\pi_1(U_0)$ is its Weil
group $W(U_0)$.  It contains the geometric fundamental group, with an
exact sequence

$$
1\longrightarrow \pi_1(U)\longrightarrow W(U_0)
\xrightarrow{\deg}\mathbf Z\longrightarrow1.
$$

A degree-one lift $s$ splits this sequence as a group extension.
In these terms, lisse Weil sheaves are the same as representations $\rho$ of $W(U_0)$,
defined over a finite extension of $\mathbf Q_\ell$, whose restriction to
$\pi_1(U)$ is continuous. For
$x\in|U_0|$, the local Frobenius $\operatorname{Frob}_x$ at $x$
(Theorem [theorem-trace-formula-euler-product]) is a conjugacy class of degree $\deg(x)$.
