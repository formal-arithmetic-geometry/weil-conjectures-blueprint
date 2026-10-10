+++
kind  = "proof"
of    = "cor-fd-l2-plancherel-middle-extension"
+++
The trace function of [def-fd-trace-function] is unchanged in
absolute value by the shift $[1]$: the shift multiplies the
alternating trace by $-1$, of $\iota$-modulus one, so
$\|f_{j_*\mathcal M[1]}\|_m=\|f_{j_*\mathcal M}\|_m$ and likewise
$\|f_{j'_*\mathcal M'[1]}\|_m=\|f_{j'_*\mathcal M'}\|_m$ for every
$m$. The Plancherel shift [lem-fd-l2-plancherel-shift], applied
to the Weil complex $j_*\mathcal M[1]$, therefore reads

$$
\|j'_*\mathcal M'\|
=\bigl\|\operatorname{FT}_\psi(j_*\mathcal M[1])\bigr\|
=\|j_*\mathcal M\|+1 .
$$

By the middle-extension comparison [lem-fd-l2-middle-extension],
$\|j_*\mathcal M\|=\|\mathcal M\|=w$ and
$\|j'_*\mathcal M'\|=\|\mathcal M'\|=v$, the second equality in each
case being the rigidity [lem-wf-l2-purity-rigidity] applied to the
punctually pure lisse sheaf $\mathcal M$ respectively $\mathcal M'$.
Substituting, $v=w+1$.

For the last assertion, [prop-a1-fourier-middle-extension] supplies the
middle-extension shape with $\mathcal M'$ lisse on the dense open
$U'_0$, and [thm-fd-generic-fourier-sheaf-pure] shows that
$\mathcal M'$ is punctually $\iota$-pure of some real weight $v$ on all
of $U'_0$. All hypotheses of the first part are then met, so $v=w+1$.
