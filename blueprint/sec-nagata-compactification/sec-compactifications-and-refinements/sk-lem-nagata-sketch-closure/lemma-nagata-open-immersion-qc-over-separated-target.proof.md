+++
kind  = "proof"
of    = "lemma-nagata-open-immersion-qc-over-separated-target"
+++
Write $f\colon T\to Y$ and $p\colon Y\to B$, so that $p\circ f\colon T\to B$
is quasi-compact. Factor $f$ through its graph,

$$
T\xrightarrow{\ \Gamma_f\ }T\times_BY\xrightarrow{\ \mathrm{pr}_2\ }Y.
$$

The graph $\Gamma_f$ is the base change of the diagonal
$\Delta_{Y/B}\colon Y\to Y\times_BY$ along
$f\times\mathrm{id}_Y\colon T\times_BY\to Y\times_BY$; since $p$ is
quasi-separated, $\Delta_{Y/B}$ is quasi-compact, hence so is $\Gamma_f$. The
projection $\mathrm{pr}_2$ is the base change of the quasi-compact morphism
$p\circ f$ along $p$, hence quasi-compact. Quasi-compact morphisms are stable
under composition, so $f=\mathrm{pr}_2\circ\Gamma_f$ is quasi-compact. The
last assertion is immediate.
