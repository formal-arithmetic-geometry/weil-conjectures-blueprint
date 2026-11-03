+++
kind  = "proof"
of    = "lem-pc-sigma-subfunctor"
+++
The sets $\operatorname{Ker}(\sigma_T^*)$ are subsets of
$\operatorname{Pic}(X_T)$ by [def-pc-pic-sigma-functor], and
$\operatorname{Pic}(X_T)$ with its pullback maps is the Picard presheaf of
[def-pc-picard-presheaf]; it remains to check the condition of
[def-pc-subfunctor]. Let $u:T'\to T$ be a morphism of schemes over
$S$, write $u_X:X_{T'}\to X_T$ for the base change of $u$
([def-pc-base-change]) and let
$[\mathcal L]\in\operatorname{Ker}(\sigma_T^*)$. The base-changed
sections are $\sigma_T=(\sigma\circ t,\mathrm{id}_T):T\to X\times_ST$ and
$\sigma_{T'}=(\sigma\circ t',\mathrm{id}_{T'})$, where $t:T\to S$ and
$t'=t\circ u$ are the structure morphisms (for $S=\operatorname{Spec}(k)$
these are the sections of [def-pc-rational-point]); under the identification
$X_{T'}=X_T\times_TT'$ of [def-pc-base-change] the composites
$u_X\circ\sigma_{T'}$ and $\sigma_T\circ u$ are therefore both the
morphism $T'\to X_T=X\times_ST$ with components $\sigma\circ t'$ and $u$.
Pullback of invertible modules
is contravariant and compatible with composition
([def-sc-picard-group]), so
$\sigma_{T'}^*\circ u_X^*=u^*\circ\sigma_T^*$ as maps on Picard groups, and
therefore

$$
\sigma_{T'}^*(u_X^*\mathcal L)\cong u^*(\sigma_T^*\mathcal L)
\cong u^*\mathcal O_T\cong\mathcal O_{T'},
$$

because $\sigma_T^*\mathcal L\cong\mathcal O_T$. Hence
$u_X^*\mathcal L\in\operatorname{Ker}(\sigma_{T'}^*)$, which is exactly
the subfunctor condition.
