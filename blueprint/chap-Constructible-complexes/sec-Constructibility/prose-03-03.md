+++
id = "prose-03-03"
kind = "hidden"
title = "Constructibility (1)"
order = 218
+++
The complexes on which the six operations will be defined are the
constructible complexes of finite Tor amplitude. We define
constructibility by a local condition, so that one definition covers all
coefficient rings, and then show that for $\mathcal O_E$ it can be tested
on the reduction modulo $\pi_E$ (Proposition [proposition-integral-constructibility-criterion]).
For a morphism $g:Z\to X$ and a $\Lambda_X$-module $M$ we write
$M|_Z=g^*M$, a $\Lambda_Z$-module.

With finite coefficients a constructible sheaf is, on the strata of a
finite stratification, locally constant with finite stalks. Each of
the three parts of our definition answers a specific need. A stratification
cannot be avoided, already for sheaves coming from geometry: for
$j:\mathbf G_m\hookrightarrow\mathbf A^1$, the sheaf $j_!\Lambda$ is zero at
the origin and $\Lambda$ elsewhere, so it is not locally constant on
$\mathbf A^1$.

Local constancy itself has to be rephrased. For $\Lambda=\mathbf Z_\ell$,
“locally constant” with value a $\mathbf Z_\ell$-module would mean locally a constant
sheaf with value the discrete group. On $\operatorname{Spec}\mathbf F_q$
such a sheaf has $H^1=0$ (Section [sec-Weil-cohomology]). The condition that $M$ be locally of the form
$\Lambda_U\otimes_{\Lambda(*)}P$ keeps the topology. For finite $\Lambda$
it is local constancy, and for $E$ it says that $M$ is locally free of
finite rank. Finite presentation of $P$ replaces finiteness of the stalks.

Finally, the six operations should commute with change of coefficients, and
this needs finite Tor amplitude. Over $\mathbf Z/\ell^2$ the sheaf $\mathbf F_\ell$
is constructible, but
$\mathbf F_\ell\otimes^{\mathbf L}_{\mathbf Z/\ell^2}\mathbf F_\ell$ has
cohomology $\mathbf F_\ell$ in every degree $\leq0$. The category
$D^b_{\mathrm{ctf}}$ is stable under change of coefficients and under
$\otimes^{\mathbf L}$. For $\mathcal O_E$, $E$ and $\overline{\mathbf Q}_\ell$ the
Tor condition is automatic (Proposition [proposition-ctf-equals-bc]).
