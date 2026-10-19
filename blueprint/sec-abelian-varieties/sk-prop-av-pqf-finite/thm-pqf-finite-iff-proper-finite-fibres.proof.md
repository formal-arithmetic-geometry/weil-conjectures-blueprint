+++
kind  = "proof"
of    = "thm-pqf-finite-iff-proper-finite-fibres"
+++
*(1) $\Rightarrow$ (2).* If $f$ is finite, then $f$ is proper by
[lem-weil-pbc-finite-proper] of the ambient-foundations chapter, and $f$ is
quasi-finite by [pqf-lem-finite-qf]. A quasi-finite morphism has
finite fibres by [pqf-lem-qf-finitefibres]. Hence $f$ is proper
with finite fibres.

*(2) $\Rightarrow$ (1).* Assume $f$ is proper with finite fibres. By
[pqf-lem-proper-basic], $f$ is separated, universally closed, of finite
type and quasi-compact, so it is quasi-finite by
[pqf-lem-qf-finitefibres], hence quasi-finite at every point of $X$ by
[pqf-lem-qf-locqf-qc]. Finiteness is local on $S$
([def-weil-pbc-scheme-conventions], [pqf-lem-affine-local-target]), and
the restriction of $f$ over an open of $S$ is again proper with finite
fibres, so we may assume $S=\operatorname{Spec}R$ affine; we must show that
$X$ is affine with $\Gamma(X,\mathcal O_X)$ a finite $R$-module. Since $S$
is quasi-compact and quasi-separated, Zariski's main theorem
[thm-pqf-zmt-factorization] factors $f=p\circ j$ with
$j:X\hookrightarrow T$ an open immersion and $p:T\to S$ finite; then
$T=\operatorname{Spec}B$ for a finite $R$-algebra $B$, and $p$ is
separated. The graph $(\mathrm{id}_X,j):X\to X\times_ST$ is a closed
immersion (a base change of the diagonal of $p$), and the projection
$X\times_ST\to T$ is closed (a base change of the universally closed $f$),
so $j(X)$ is open and closed in $\operatorname{Spec}B$. Hence
$j(X)=D(e)$ for an idempotent $e\in B$, and
$X\cong\operatorname{Spec}(B/(1-e)B)$ is affine with
$\Gamma(X,\mathcal O_X)$ a quotient of the finite $R$-module $B$. So $f$ is
finite.

*The locally Noetherian case without Zariski's main theorem.* If $S$ is
locally Noetherian, (2) $\Rightarrow$ (1) can also be seen as follows.
It suffices to prove that $f$ is affine: if $f$ is affine, then $f$ is
universally closed by [pqf-lem-proper-basic] (it is proper), so
$f$ is integral by [pqf-lem-integral-univclosed]; since $f$ is
proper it is of finite type, hence locally of finite type, by
[def-weil-pbc-scheme-conventions]; therefore $f$ is finite by
[pqf-lem-integral-lft-finite].

To prove that $f$ is affine, by
[pqf-lem-affine-local-target] we may assume that $S$ is affine,
and our goal is to show that $X$ is affine. Since $f$ is proper, $X$
is separated and quasi-compact by [pqf-lem-proper-basic], so we
may use [pqf-lem-serre-criterion] to prove that $X$ is affine.
Let $\mathcal I\subset\mathcal O_X$ be a quasi-coherent sheaf of
ideals of finite type. First, $X$ is locally Noetherian: $f$ is of
finite type by [def-weil-pbc-scheme-conventions] and $S$ is
locally Noetherian, so [pqf-lem-locnoeth-lft] applies. Hence
$\mathcal I$, being quasi-coherent of finite type on the locally
Noetherian scheme $X$, is coherent by
[pqf-lem-coherent-ft-locnoeth]. By
[pqf-lem-fff-vanishing] applied to the coherent sheaf
$\mathcal I$ we get $(R^1f_*\mathcal I)_s=0$ for all $s\in S$
(the fibre $f^{-1}(\{s\})$ is finite by assumption), i.e. the sheaf
$R^1f_*\mathcal I$ has vanishing stalks at every point, so
$R^1f_*\mathcal I=0$ by [pqf-lem-sheaf-zero-stalks]. From the
Leray spectral sequence [pqf-lem-leray] of the morphism $f$, more
precisely from its low degree terms
[pqf-lem-leray-lowdegree], we obtain

$$
\mathrm H^1(X,\mathcal I)\cong\mathrm H^1(S,f_*\mathcal I).
$$

Now $f$ is quasi-compact and quasi-separated by
[pqf-lem-proper-basic], so $f_*\mathcal I$ is quasi-coherent by
[pqf-lem-pushforward-qcoh]. Since $S$ is affine,
[pqf-lem-affine-vanishing] gives
$\mathrm H^1(S,f_*\mathcal I)=0$. Hence
$\mathrm H^1(X,\mathcal I)=0$ for every quasi-coherent ideal of finite
type, and [pqf-lem-serre-criterion] shows that $X$ is affine.
Since $S$ is affine as well, $f$ is affine by
[pqf-def-affine-morphism], which finishes this second argument.
