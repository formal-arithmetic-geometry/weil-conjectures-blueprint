+++
id = "prose-03-03"
kind = "hidden"
title = "Constructibility (1)"
order = 218
+++
With finite coefficients a constructible sheaf is, on the strata of a
finite stratification, locally constant with finite stalks. The six
operations, however, will act on constructible complexes of finite Tor amplitude
for every coefficient ring, so we need a definition of constructibility that covers all coefficient
rings at once. We give it by a local condition
(Definition [definition-constructible-sheaves]). This condition has two parts, a
stratification and a local model that replaces local constancy, and the
complexes we use must in addition have finite Tor amplitude. As we explain below, each of the
three conditions answers a specific need. For $\mathcal O_E$ we then
show that constructibility can be tested on the reduction modulo $\pi_E$
(Proposition [proposition-integral-constructibility-criterion]). For a
morphism $g:Z\to X$ and a $\Lambda_X$-module $M$ we write $M|_Z=g^*M$, a
$\Lambda_Z$-module.

A stratification
cannot be avoided, already for sheaves coming from geometry: for
$j:\mathbf G_m\hookrightarrow\mathbf A^1$, the sheaf $j_!\Lambda$ is zero at
the origin and $\Lambda$ elsewhere, so it is not locally constant on
$\mathbf A^1$.

Local constancy itself has to be rephrased. For instance, for $\Lambda=\mathbf Z_\ell$,
“locally constant” with value a $\mathbf Z_\ell$-module would mean locally a constant
sheaf with value the discrete group, but on $\operatorname{Spec}\mathbf F_q$
such a sheaf has $H^1=0$ (Section [sec-Weil-cohomology]), whereas the
answer we want is $\mathbf Z_\ell$. We therefore ask instead that $M$ be locally of the
form $\Lambda_U\otimes_{\Lambda(*)}P$, with $P$ a finitely presented module over the ring $\Lambda(*)$ of sections
over the point, as in the opening of this section. This keeps the $\ell$-adic topology. For finite $\Lambda$
it is local constancy, and for $E$ it says that $M$ is locally free of
finite rank. In this formulation, finite presentation of $P$ replaces finiteness of the stalks.

Finally, the six operations should commute with change of coefficients, and
this needs finite Tor amplitude. Over $\mathbf Z/\ell^2$ the sheaf $\mathbf F_\ell$
is constructible, but
$\mathbf F_\ell\otimes^{\mathbf L}_{\mathbf Z/\ell^2}\mathbf F_\ell$ has
cohomology $\mathbf F_\ell$ in every degree $\leq0$. With the Tor condition imposed, by contrast,
the category
$D^b_{\mathrm{ctf}}$ is stable under change of coefficients and under
$\otimes^{\mathbf L}$, and for $\mathcal O_E$, $E$ and $\overline{\mathbf Q}_\ell$ the
Tor condition is automatic (Proposition [proposition-ctf-equals-bc]).
