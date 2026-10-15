+++
kind  = "proof"
of    = "det-lem-bounded-continuity-sections"
+++
(1) A colimit $\varinjlim_{j\in J}M_j$ is the cokernel of
$\bigoplus_{(j\to j')}M_j\to\bigoplus_jM_j$, the map being $x\mapsto x-\phi_{jj'}(x)$ on the
summand indexed by $j\to j'$. An additive functor preserving direct sums and cokernels
(right exactness) preserves this presentation, hence the colimit. Evaluation on $W_n$ is
exact on $A$-modules because $W_n$ is weakly contractible (every surjection of sheaves is
surjective on sections over $W_n$), and commutes with direct sums because $W_n$ is
quasi-compact and quasi-separated ([sk-cor-pe-sections]).

(2) The first statement is the hypercovering computation of [sk-prop-pe-hypercover]: on
weakly contractible objects the terms $K^m$ are acyclic for $\Gamma(W_n,-)$, so the Čech-type
double complex of the hypercovering computes $R\Gamma(Y,K^\bullet)$ for bounded below $K$.
In total degree $q$ we need $n\ge0$ and $m=q-n\ge a$, i.e. $0\le n\le q-a$: finitely many
terms.

(3) By (1), $(\varinjlim_iK_i^m)(W_n)=\varinjlim_iK_i^m(W_n)$, compatibly with both
differentials; by (2) each term of the total complex is a finite direct sum of such, and
finite direct sums commute with colimits. So
$\operatorname{Tot}((\varinjlim_iK_i)(W_\bullet))=\varinjlim_i\operatorname{Tot}(K_i(W_\bullet))$
as complexes of abelian groups. Filtered colimits of abelian groups are exact, so cohomology
commutes with them, and (2) identifies the cohomology groups with $H^q(Y,-)$. The map is
the natural one because the identification of (2) is natural in $K$.
