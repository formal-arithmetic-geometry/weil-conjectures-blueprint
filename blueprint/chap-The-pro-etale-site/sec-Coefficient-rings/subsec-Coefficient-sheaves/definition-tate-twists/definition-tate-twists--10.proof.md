+++
kind = "proof"
of = "definition-tate-twists--10"
order = 184017
uses = ["definition-tate-twists--2", "definition-tate-twists--8", "lemma-stability", "proposition-topos-functoriality", "lemma-comparison-completed-coefficients", "corollary-finite-quotients-their-transition-maps"]
+++
Put $U=X\times_k\operatorname{Spec}k^{\mathrm{sep}}$. The projection $g:U\to X$ is a pro-étale cover. Choose primitive $\ell^n$th roots of unity $\zeta_n\in k^{\mathrm{sep}}$ with $\zeta_{n+1}^{\ell}=\zeta_n$.

By [definition-tate-twists--2], the maps $a\mapsto\zeta_n^a$ identify the roots-of-unity sheaves on $U$ with the cokernels of multiplication by $\ell^n$ on $\mathbf Z_U$. These identifications commute with the power maps. After forming the free $g^{-1}\mathbf Z_{\ell,X}$-modules, they identify the pullback of the Tate-module tower with the quotient tower of $g^{-1}\mathbf Z_{\ell,X}$. Pullback along this weakly étale morphism preserves the limit in question. The limit of the quotient tower is the coefficient module itself, so $g^{-1}\mathbf Z_{\ell,X}(1)$ is trivial.

Pullback commutes with extension of scalars, and extension of scalars sends the free module of rank one to the free module of rank one. Thus the integral and algebraic-closure twists of degree one are trivial on $U$. Pullback preserves tensor products and, along $g$, internal Hom. Their tensor powers and duals are therefore trivial on the same cover. This supplies the local free modules of rank one.
