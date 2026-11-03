+++
kind  = "proof"
of    = "lem-weil-pbc-projective-embedding"
+++
The composite of $(a,b)$ with the projection
$X\times_Y\mathbf P^n_Y\to\mathbf P^n_Y$ is the closed immersion $b$. This
projection is the base change of $f$ along $\mathbf P^n_Y\to Y$, hence
separated. If $g\circ h$ is a closed immersion and $g$ is separated, then
$h$ is a closed immersion: $h$ is the graph $T\to T\times_{\mathbf P^n_Y}(X\times_Y\mathbf P^n_Y)$,
a closed immersion as a base change of the diagonal of $g$, followed by the
base change of the closed immersion $g\circ h$. Hence $(a,b)$ is a closed
immersion. For the special case, a proper morphism is separated and
$i_Y$ is a closed immersion with $p\circ i_Y=f\circ\pi$ by
[cor-chow-lemma-proper]; apply
the general statement with $T=\widetilde X$, $a=\pi$ and $b=i_Y$.
