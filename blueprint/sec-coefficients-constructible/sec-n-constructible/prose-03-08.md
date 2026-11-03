+++
id = "prose-03-08"
kind = "hidden"
title = "Constructible complexes"
order = 143
+++
The complexes on which the six operations will be defined are the
constructible complexes of finite Tor amplitude. We define
constructibility by a local condition, so that one definition covers all
coefficient rings, and then show that for $\mathcal O_E$ it can be tested
on the reduction modulo $\pi_E$ (Proposition [sk-prop-integral-criterion]).
For a morphism $g:Z\to X$ and a $\Lambda_X$-module $M$ we write
$M|_Z=g^*M$, a $\Lambda_Z$-module.

The definition has three parts, and each answers a specific need. With
finite coefficients a constructible sheaf is, on the strata of a finite
stratification, locally constant with finite stalks. A stratification
cannot be avoided, already for sheaves coming from geometry: for
$j:\mathbf G_m\hookrightarrow\mathbf A^1$, the sheaf $j_!\Lambda$ is zero at
the origin and $\Lambda$ elsewhere, and it is not locally constant on
$\mathbf A^1$. For $\Lambda=\Zl$, however, “locally constant” with
value a $\Zl$-module would mean locally a constant sheaf with value the
discrete group, and this has the wrong cohomology, as we saw for
$\operatorname{Spec}\mathbf F_q$. The condition that $M$ be locally of the form
$\Lambda_U\otimes_{\Lambda(*)}P$ keeps the topology; for finite $\Lambda$
it is local constancy, and for $E$ it says that $M$ is lisse. Finite
presentation of $P$ replaces finiteness of the stalks. Finally, the six
operations should commute with change of coefficients, and this needs
finite Tor amplitude: over $\mathbf Z/\ell^2$ the sheaf $\mathbf F_\ell$
is constructible, but
$\mathbf F_\ell\otimes^{\mathbf L}_{\mathbf Z/\ell^2}\mathbf F_\ell$ has
cohomology $\mathbf F_\ell$ in every degree $\leq0$. The category
$D^b_{\mathrm{ctf}}$ is stable under change of coefficients and under
$\otimes^{\mathbf L}$, and it is the category of
Theorem [sk-thm-existence]. For $\mathcal O_E$, $E$ and $\overline{\mathbf Q}_\ell$ the
Tor condition is automatic (Proposition [sk-prop-n-ctf-equals-bc]).
