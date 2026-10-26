+++
kind = "proof"
of = "sk-lem-int-ext"
uses = ["sk-lem-int-integral-heart", "sk-lem-formal-closed-support", "sk-cor-pe-bounded-continuity", "sk-lem-constructible-ext-continuity", "sk-def-cd", "sk-prop-integral-criterion"]
+++
Both statements reduce, by the long exact Ext sequences of a finite
filtration of $C$, to $C=a_!L$, where $a=i\circ u:S\hookrightarrow X$ is the
inclusion of a stratum, with $u:S\hookrightarrow Z$ open and
$i:Z\hookrightarrow X$ closed, and $L$ is locally the completion of a finitely
generated $\mathcal O_E$-module. Let $j$ be the open immersion complementary to
$i$. [sk-lem-formal-closed-support] holds for $\mathcal O_{E,X}$-modules with
the same proof. Tensor–Hom adjunction and the adjunction between $i_*$ and
$R\underline\Gamma_Z$ give

$$
R\operatorname{Hom}_X(a_!L,K)
=R\Gamma\bigl(S,\cHom_{\mathcal O_{E,S}}(L,\mathcal O_{E,S})
\otimes^{\mathbf L}_{\mathcal O_{E,S}}u^*R\underline\Gamma_ZK\bigr).
$$

By [sk-lem-int-integral-heart](3), tensoring with the dual
$\cHom_{\mathcal O_{E,S}}(L,\mathcal O_{E,S})$ has Tor amplitude $[0,1]$ and
commutes with filtered colimits.

(1) The proof of [sk-cor-pe-bounded-continuity] works for any sheaf of rings.
Apply it to the two terms of the fibre sequence defining
$R\underline\Gamma_Z$ (as in the proof of
[sk-lem-constructible-ext-continuity]) and use that tensoring with the dual
has finite Tor amplitude. This gives continuity for $C=a_!L$, and in
particular for $\Hom$ and $\Ext^1$ between constructible sheaves.

(2) Let $N\in\Cons(X,\mathcal O_E)$. Its reductions
$N\otimes^{\mathbf L}\mathcal O_{E,X}/\pi_E^n$ are constructible torsion
complexes in degrees $[-1,0]$, by the length one resolution, and
$N\simeq R\varprojlim_n(N\otimes^{\mathbf L}\mathcal O_{E,X}/\pi_E^n)$, since $N$
is derived complete ([sk-prop-integral-criterion]). The cohomological dimensions
$\operatorname{cd}_\ell(j)$ and $\operatorname{cd}_\ell(S)$ of [sk-def-cd] are
finite and depend only on $j$ and $S$. We bound the degrees of the formula
above, applied to each reduction of $N$:

- $R\underline\Gamma_Z$ of a torsion complex in degrees $[-1,0]$ has
  cohomology in degrees $\le\operatorname{cd}_\ell(j)+1$, by its fibre
  description;
- tensoring with the dual of $L$ raises the upper bound by at most one;
- $R\Gamma(S,-)$ raises it by at most $\operatorname{cd}_\ell(S)$.

Each reduction therefore contributes only in degrees
$\le\operatorname{cd}_\ell(j)+\operatorname{cd}_\ell(S)+2$. All the functors
involved ($R\underline\Gamma_Z$, open restriction, derived sections, closed
inverse image by Stacks, Tag 09AA, and tensoring with the dualizable dual of
$L$) commute with derived inverse limits. The derived inverse limit of a
countable tower raises the upper bound by at most one (Milnor sequence,
Stacks, Tag 08TB); this applies because the complexes and transition maps can
be taken in the abelian category of inverse systems before deriving. Hence

$$
\Ext^q_X(a_!L,N)=0\qquad(q>\operatorname{cd}_\ell(j)+\operatorname{cd}_\ell(S)+3).
$$

The bound depends only on $a$. For general $C$, take the maximum over the
finitely many pieces $a_!L$ of a filtration of $C$.
