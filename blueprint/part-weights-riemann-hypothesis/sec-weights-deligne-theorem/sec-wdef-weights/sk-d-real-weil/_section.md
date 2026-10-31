+++
id = "sk-d-real-weil"
kind = "definition"
title = "Weil structures and the weight convention"
order = 629
lean = ["AlgebraicGeometry.WeilGroup", "AlgebraicGeometry.WeilGroup.IsLisse"]
uses = ["sk-d-weil", "sk-def-sf-weil-complexes", "sk-lem-tf-frobenius-convention", "sk-p-real-integral", "sk-thm-trace-transport"]
tags = ["sketch", "latex:convention"]
+++
Put $k_0=\mathbf F_q$, $k=\overline{\mathbf F}_q$, and fix a prime
$\ell\nmid q$ and a field embedding $\iota:\overline{\mathbf Q}_\ell\hookrightarrow\mathbf C$.
For $X_0/k_0$ separated of finite type, write $X=X_0\times_{k_0}k$,
and for a closed point $x$ of $X_0$ write $\deg(x)=[\kappa(x):k_0]$ for
its degree and $q_x=q^{\deg(x)}=\#\kappa(x)$. Geometric Frobenius, Weil
complexes and their Frobenius operators are those of
Section [sec-frobenius]. A Weil sheaf is a Weil complex concentrated
in degree zero, and the six operations carry Weil structures to Weil
structures.

On a connected normal scheme of finite type over a field, we identify a
lisse $E$-sheaf with the corresponding continuous representation of the
profinite fundamental group, by
Proposition [sk-p-real-integral]. All arguments with
representations below take place on smooth schemes. A lisse Weil
$\overline{\mathbf Q}_\ell$-sheaf has a lisse Weil model over some finite extension
$E/\Ql$, and two models become identified after a finite extension of
scalars. The model includes the Weil isomorphism, which need not
preserve a geometric $\mathcal O_E$-lattice.

For a geometrically connected smooth curve $U_0$, put $U=U_0\times_{k_0}k$
and choose a geometric point $\bar\eta$ of $U$. We write $\pi_1(U)$ and
$\pi_1(U_0)$ for $\pi_1(U,\bar\eta)$ and $\pi_1(U_0,\bar\eta)$; changing
$\bar\eta$ changes them by inner automorphisms, which do not affect any
statement below. The inverse image
of the integer powers of geometric Frobenius in $\pi_1(U_0)$ is its Weil
group $W(U_0)$. It contains the geometric fundamental group, with an
exact sequence

$$
1\longrightarrow \pi_1(U)\longrightarrow W(U_0)
\xrightarrow{\deg}\mathbf Z\longrightarrow1.
$$

A degree-one lift $s$ splits this sequence as a group extension.
Lisse Weil sheaves are the same as representations $\rho$ of $W(U_0)$,
defined over a finite extension of $\Ql$, whose restriction to
$\pi_1(U)$ is continuous. Since the quotient $\mathbf Z$ is discrete,
continuity imposes no boundedness condition on $\rho(s)$. For
$x\in|U_0|$, the local Frobenius $\operatorname{Frob}_x$ at $x$
(Theorem [sk-thm-trace-transport]; it is written $\pi_x$ in the Stacks
Project and $F_x$ in SGA 4½) is a conjugacy class of degree $\deg(x)$.

*Complement.* In the detail nodes the degree $d(x)$ is also written $e_x$,
a curve means a nonempty separated smooth $\Fq$-scheme of finite type, of pure
dimension one, with connected base change ([d-real-setup]), and the
degree-one lift is also written $\gamma$, with $F=\rho(\gamma)$. The local
Frobenius $F_x$ is the image in $W(U_0)$ of the geometric Frobenius of a
decomposition group at $x$, for a chosen path from a geometric point over $x$
to the base point; it is well defined up to conjugacy in $W(U_0)$. The
correspondence $\mathcal F\mapsto(\mathcal F_{\bar\eta},\rho_{\mathcal F})$ is an
exact tensor equivalence between lisse Weil sheaves on $U_0$ and these
representations, so subobjects, quotients and subquotients match in both
directions ([prop-wf-weil-sheaf-representation-equivalence]). A constructible
Weil sheaf is lisse of finite rank on each stratum of a finite stratification
into locally closed subschemes.
