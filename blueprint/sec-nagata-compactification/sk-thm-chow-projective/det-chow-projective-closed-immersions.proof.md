+++
kind  = "proof"
of    = "det-chow-projective-closed-immersions"
uses = ["lem-weil-pbc-proper-to-separated", "lem-weil-pbc-proper-immersion-closed", "lemma-nagata-projective-space-base-change-proper"]
+++
*Part 1.* $f$ and $\pi$ are proper, hence so is $f\pi:\widetilde X\to S$.
The projection $q_S:\mathbf P^n_S\to S$ is proper
([lemma-nagata-projective-space-base-change-proper]), in particular
separated. Thus $i_S$ is an $S$-morphism from a proper $S$-scheme to a
separated $S$-scheme, hence proper ([lem-weil-pbc-proper-to-separated]):
it factors as its graph $\widetilde X\to\widetilde X\times_S\mathbf P^n_S$,
a closed immersion because $\mathbf P^n_S\to S$ is separated, followed by
the projection to $\mathbf P^n_S$, which is the base change of the proper
$f\pi$. A proper immersion is a closed immersion
([lem-weil-pbc-proper-immersion-closed]). So $i_S$ is a closed immersion,
and $f\pi=q_S\circ i_S$ is projective.

*Part 2.* Factor $i_X$ as

$$
\widetilde X\xrightarrow{\ \Gamma_\pi\ }\widetilde X\times_SX
\xrightarrow{\ i_S\times\mathrm{id}_X\ }\mathbf P^n_S\times_SX .
$$

The graph $\Gamma_\pi=(\mathrm{id},\pi)$ is the base change of the diagonal
$\Delta_{X/S}$ along $\pi\times\mathrm{id}_X$, a closed immersion since
$f$ is proper, hence separated. The second arrow is the base change of the
closed immersion $i_S$ along $X\to S$, hence a closed immersion. Their
composite is $(\pi,i_S)=i_X$, a closed immersion. Composing with the
projection $\mathbf P^n_X\to X$ gives $\pi$, so $\pi$ is projective.
