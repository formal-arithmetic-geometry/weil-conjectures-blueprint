+++
kind  = "proof"
of    = "det-lem-integral-models-operations"
+++
We use the criterion of [sk-prop-integral-criterion]: membership in $\Dbc(-,\cO_E)$ means
derived $\pi_E$-completeness plus bounded constructibility of the reduction modulo $\pi_E$.
Write $\bar K=K\otimes^{\mathbf L}\cO_E/\pi_E$, the cone of $\pi_E$ on $K$.

*Local form.* By \stacks{09C2} and \stacks{09C7}, every $K\in\Dbc(X,\cO_E)$ is bounded, and
there is a finite stratification of $X$ such that on each stratum $K$ is pro-étale locally a
bounded complex of finite free $\cO_{E}$-modules (pulled back to $\cO_{E,X}$).

(1) $f^*$ is exact and $f^*\cO_{E,Y}=\cO_{E,X}$ ([sk-prop-sfb-cartesian-coefficients]); it sends
finite free modules to finite free modules, and strata and covers pull back to strata and
covers. So $f^*K$ has, on the pulled-back strata, the same local form; such a complex is
derived complete (it is complete locally, being a bounded complex of finite free
$\cO_{E,X}$-modules, and completeness is local) and its reduction $f^*\bar K$ is bounded
constructible by the classical torsion theory. Hence $f^*K\in\Dbc(X,\cO_E)$.

(4) Both sides are computed by flat resolutions and $a_!$, $a^*$ are exact; there is a natural
map $a_!(L\otimes^{\mathbf L}a^*M)\to a_!L\otimes^{\mathbf L}M$ (adjoint, for $u_!$, to the
identification on $S$, and for $i_*$ the projection formula map). On the stratum $S$ both sides
restrict to $L\otimes^{\mathbf L}a^*M$ (as $a^*a_!=\mathrm{id}$ and $a^*$ is monoidal), and on
$X\smallsetminus S$ (the open complement of $\overline S$ and the closed $\overline S\smallsetminus S$)
both restrict to $0$. These restrictions are jointly conservative (\stacks{09AD}), so the map
is an isomorphism.

(2) First suppose $M$ is, on a pro-étale cover, a bounded complex of finite free modules.
Then $K\otimes^{\mathbf L}M$ is locally a finite sum of shifts of $K$, so derived complete, and
$\overline{K\otimes^{\mathbf L}M}=\bar K\otimes^{\mathbf L}_{\cO_E/\pi_E}\bar M$, a bounded
constructible complex over the field $\cO_E/\pi_E$. In general, use the open–closed
dévissage: for an open stratum $u\colon U\hookrightarrow X$ with closed complement $i$, the
triangle $u_!u^*M\to M\to i_*i^*M\to$ and (4) give a triangle
$u_!(u^*K\otimes^{\mathbf L}u^*M)\to K\otimes^{\mathbf L}M\to i_*(i^*K\otimes^{\mathbf L}i^*M)\to$.
By induction on the number of strata (and (1), (3)) the outer terms lie in $\Dbc$, which is
closed under extensions (completeness and constructibility of reductions are), so the middle
term does.

(3) For a quasi-compact open immersion $u$, $u_!$ is exact and preserves limits
(\stacks{09BP}); $i_*$ is exact and preserves limits (\stacks{09AA}, \stacks{09BM}). So both
commute with $\operatorname{R\lim}$ and with the cone of $\pi_E$, hence preserve derived
completeness and commute with reduction. On reductions they are the extension by zero and the
closed direct image of torsion sheaves, which preserve bounded constructibility. (All open
immersions are quasi-compact since the schemes are Noetherian.)
