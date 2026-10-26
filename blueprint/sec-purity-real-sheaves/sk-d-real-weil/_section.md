+++
id = "sk-d-real-weil"
kind = "definition"
title = "Weil structures and the weight convention"
order = 3766
uses = ["sk-d-weil", "sk-def-sf-weil-complexes", "sk-lem-tf-frobenius-convention", "sk-p-real-integral"]
lean = ["AlgebraicGeometry.WeilGroup", "AlgebraicGeometry.WeilGroup.IsLisse"]
tags = ["sketch"]
+++
*Convention.* Put $k_0=\mathbf F_q$, $k=\overline{\mathbf F}_q$, and fix a prime
$\ell\nmid q$ and a field embedding
$\iota:\overline{\mathbf Q}_\ell\hookrightarrow\mathbf C$.
For $X_0/k_0$ separated of finite type, write $X=X_0\times_{k_0}k$.
We use geometric Frobenius and Weil structures as in [sk-d-weil] and
[sk-lem-tf-frobenius-convention]. A Weil sheaf is a Weil complex concentrated
in degree zero. Derived constructions take place in the geometric pro-étale
category and carry the induced Weil isomorphisms of
[sk-def-sf-weil-complexes].

On a connected smooth scheme of finite type over a field, we identify a
lisse $\overline{\mathbf Q}_\ell$-sheaf with the corresponding continuous representation of the
profinite fundamental group, by [sk-p-real-integral]. All arguments with
representations below take place on smooth schemes. A lisse Weil
$\overline{\mathbf Q}_\ell$-sheaf has a lisse Weil model over some finite
extension $E/\Ql$, and two models become identified after a finite extension
of scalars. The model includes the Weil isomorphism, which need not
preserve a geometric $\mathcal O_E$-lattice.

For a geometrically connected smooth curve $U_0$, choose a geometric base
point and set $P=\pi_1(U)$, where $U=U_0\times_{k_0}k$. The inverse image
of the integer powers of geometric Frobenius in $\pi_1(U_0)$ is its Weil
group. It has an exact sequence

$$
 1\longrightarrow P\longrightarrow W(U_0)
   \xrightarrow{\deg}\mathbf Z\longrightarrow0.
$$

A degree-one lift $s$ splits this sequence as a group extension.
Lisse Weil sheaves are the same as representations of this group,
defined over a finite extension of $\Ql$, whose restriction to $P$ is
continuous. Since the quotient $\mathbf Z$ is discrete, continuity
imposes no boundedness condition on $\rho(s)$. For $x\in|U_0|$, put
$d(x)=[\kappa(x):k_0]$ and $q_x=q^{d(x)}$. The local Frobenius $F_x$
at $x$ is a conjugacy class of degree $d(x)$.

In this description, the Weil isomorphism is given by transport by $s$,
and conversely the Weil isomorphism determines the action of $s$.
Passing to the finite reductions, one sees that the correspondence
commutes with finite extension of scalars and with inverse image
between normal schemes.

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
