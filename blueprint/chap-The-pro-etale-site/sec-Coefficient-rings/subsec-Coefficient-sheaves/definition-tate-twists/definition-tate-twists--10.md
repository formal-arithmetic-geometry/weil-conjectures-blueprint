+++
id = "definition-tate-twists--10"
kind = "lemma"
title = "Rank of the Tate twist"
order = 184011
aliases = ["bp-r053-10"]
lean = ["AlgebraicGeometry.ProEtale.isLocallyFree_integralTateTwist", "AlgebraicGeometry.ProEtale.isLocallyFree_tateTwist"]
uses = ["definition-tate-twists--5", "definition-tate-twists--9", "definition-tate-twists--11", "definition-tate-twists--12"]
+++
Let $X$ be a scheme over a field $k$ in which $\ell$ is invertible, and let $E/\mathbf Q_\ell$ be finite with a chosen embedding into $\overline{\mathbf Q}_\ell$. Use the integral twist
$$
\mathcal O_{E,X}(1)=\mathcal O_{E,X}\otimes_{\mathbf Z_{\ell,X}}\mathbf Z_{\ell,X}(1)
$$
and the algebraic-closure twist of [definition-tate-twists--9]. For every $d\in\mathbf Z$, the modules $\mathcal O_{E,X}(d)$ and $\QbarX(d)$, formed by tensor powers and duals, are locally free. In fact, they are trivial over the pro-étale cover $X\times_k\operatorname{Spec}k^{\mathrm{sep}}\to X$, so the local free modules have rank one.
