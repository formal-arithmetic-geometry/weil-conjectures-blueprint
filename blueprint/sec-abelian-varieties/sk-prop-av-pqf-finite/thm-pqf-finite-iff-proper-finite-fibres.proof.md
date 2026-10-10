+++
kind  = "proof"
of    = "thm-pqf-finite-iff-proper-finite-fibres"
+++
*(1) $\Rightarrow$ (2).* If $f$ is finite, then $f$ is proper by
[lem-weil-pbc-finite-proper] of the ambient-foundations chapter, and $f$ is
quasi-finite by [pqf-lem-finite-qf]. A quasi-finite morphism has
finite fibres by [pqf-lem-qf-finitefibres]. Hence $f$ is proper
with finite fibres.

*(2) $\Rightarrow$ (1).* Assume $f$ is proper with finite fibres.
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
[pqf-def-affine-morphism], which finishes the proof.
