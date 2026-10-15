+++
kind = "proof"
of = "det-sp-tower-injective-components"
+++
By [det-sp-tower-evaluation-adjoint], $I_\bullet$ embeds into
$\prod_nr_nJ_n$ with $J_n$ injective $\mathcal O_{E,T}/\ell^n$-modules; as $I_\bullet$
is injective the embedding splits, so $I_\bullet$ is a direct summand of
$\prod_nr_nJ_n$, and at level $r$ this is a direct summand of
$\prod_{n\leq r}J_n$, a finite product.

An injective module over a sheaf of rings $\mathcal R$ on a site is flasque in
the sense that $H^q(U,J)=0$ for $q>0$ and every object $U$; this vanishing is a
statement about the underlying abelian sheaf (cohomology of a module sheaf can
be computed in abelian sheaves), so it is unaffected by restricting scalars
along $\mathcal O_{E,T}/\ell^r\to\mathcal O_{E,T}/\ell^n$. Finite products and
direct summands of sheaves with vanishing higher cohomology on all objects
again have this property. Hence $I_r$ has vanishing higher cohomology on every
object of $T_{\mathrm{proét}}$, so $R^qg_*I_r$, the sheafification of
$V\mapsto H^q(V\times_ST,I_r)$, vanishes for $q>0$: $I_r$ is $g_*$-acyclic.

Finally, $Rg_{*,\bullet}C_\bullet=g_{*,\bullet}I_\bullet^\cdot$, whose level $n$ is
$g_*I_n^\cdot$. Evaluation is exact, so $I_n^\cdot$ is a bounded below resolution of
$C_n$ by $g_*$-acyclic sheaves, and $g_*I_n^\cdot$ computes
$Rg_{*,\mathcal O_E/\ell^n}C_n$.
