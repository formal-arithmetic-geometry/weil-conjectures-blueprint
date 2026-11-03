+++
kind  = "proof"
of    = "lem-av-rigidity-local"
+++
Choose an affine open $V\subseteq Z$ around the image point. As
$\operatorname{pr}_2$ is closed ($X$ is proper),
$Y\smallsetminus\operatorname{pr}_2\bigl(f^{-1}(Z\smallsetminus V)\bigr)$ is an open
neighbourhood of $y$; choose an affine open $U\ni y$ inside it, so that $f$ maps
$X\times_kU$ into $V$. Since $\Gamma(X,\mathcal O_X)=k$
(Stacks [0BUG](https://stacks.math.columbia.edu/tag/0BUG)), flat base change gives
$\Gamma(X\times_kU,\mathcal O)=\mathcal O(U)$ via $\operatorname{pr}_2^\#$, so the
morphism $X\times_kU\to V$ to the affine scheme $V$, which is given by a ring map
$\mathcal O(V)\to\Gamma(X\times_kU,\mathcal O)$, factors through
$\operatorname{pr}_2:X\times_kU\to U$. A proper geometrically integral $X$, as in the
tex, is geometrically connected and geometrically reduced.
