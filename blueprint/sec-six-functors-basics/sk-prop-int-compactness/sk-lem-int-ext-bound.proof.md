+++
kind = "proof"
of = "det-lem-int-ext-bound"
+++
Write $N_n=N\otimes^{\mathbf L}\mathcal O_{E,X}/\pi_E^n$. By the length one
resolution of $\mathcal O_E/\pi_E^n$, $N_n$ is the cone of $\pi_E^n$ on $N$, a
constructible torsion complex in degrees $[-1,0]$, and
$N\simeq R\varprojlim_nN_n$, since $N$ is derived complete
([sk-prop-integral-criterion]). The
cohomological dimensions $\operatorname{cd}_\ell(j)$ and
$\operatorname{cd}_\ell(S)$ of [sk-def-cd] are finite and depend only on $j$
and $S$. Apply the formula of [det-lem-int-ext-formula](2) to $N_n$:

- $R\underline\Gamma_ZN_n$ is $i^*$ of the fibre of $N_n\to Rj_*j^*N_n$;
  since $Rj_*$ of a torsion complex in degrees $[-1,0]$ has cohomology in
  degrees $\le\operatorname{cd}_\ell(j)$, the fibre has cohomology in degrees
  $\le\operatorname{cd}_\ell(j)+1$;
- tensoring with $L^\vee$, of Tor amplitude $[0,1]$, raises the upper bound
  by at most one, and $u^*$ is exact;
- $R\Gamma(S,-)$ raises it by at most $\operatorname{cd}_\ell(S)$.

So $R\operatorname{Hom}_X(a_!L,N_n)$ has cohomology in degrees
$\le\operatorname{cd}_\ell(j)+\operatorname{cd}_\ell(S)+2$. All functors
involved ($R\underline\Gamma_Z$, i.e. $Rj_*$, $j^*$ and closed inverse image
(Stacks, Tag 09AA), open restriction, derived sections, and tensoring with the
dualizable $L^\vee$) commute with derived inverse limits, so
$R\operatorname{Hom}_X(a_!L,N)\simeq R\varprojlim_nR\operatorname{Hom}_X(a_!L,N_n)$.
The derived limit of a countable tower raises the upper bound by at most one
(Milnor sequence, Stacks, Tag 08TB); this applies because the complexes and
transition maps can be taken in the abelian category of inverse systems
before deriving. Hence the vanishing for
$q>\operatorname{cd}_\ell(j)+\operatorname{cd}_\ell(S)+3$; the bound depends only
on $a$.

For general $C\in\Cons(X,\mathcal O_E)$, filter $C$ as in
[det-lem-int-ext-formula](1) by finitely many pieces $a_!L$ in degree $0$.
The long exact Ext sequences show that $d_C$, the maximum of the bounds of
the pieces, works.
