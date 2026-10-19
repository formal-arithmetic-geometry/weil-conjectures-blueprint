+++
id = "sk-def-sf-weil-complexes"
kind = "definition"
title = "Weil structure"
order = 1837
uses = ["def-weil-weil-sheaf-complex"]
tags = ["sketch"]
+++
Fix $k_0=\mathbb F_q$ and its algebraic closure $k$, and let $f:X\to Y$ be
obtained from a smooth morphism $f_0:X_0\to Y_0$ over $k_0$ by extension to
$k$. For a scheme $T=T_0\times_{k_0}k$, let
$\operatorname{Fr}_T:T\to T$ be the semilinear automorphism induced by the
geometric Frobenius $\sigma=\sigma_{\mathrm{ar}}^{-1}\in\operatorname{Gal}(k/k_0)$,
and for an admissible coefficient ring $\Lambda$ let
$\operatorname{Fr}_T^*:\Dctf(T,\Lambda)\to\Dctf(T,\Lambda)$ be the induced
pullback.

For $K\in\Dctf(Y,\Lambda)$, a *Weil structure* is an isomorphism in
$\Dctf(Y,\Lambda)$

$$
\phi_K:\operatorname{Fr}_Y^*K\xrightarrow{\sim}K.
$$

A *strict Weil complex* (in this section simply a *Weil complex*) is a pair
$(K,\phi_K)$ with this structure. A morphism
$(K,\phi_K)\to(L,\phi_L)$ is a morphism $h:K\to L$ in $\Dctf(Y,\Lambda)$
satisfying

$$
h\circ\phi_K=\phi_L\circ\operatorname{Fr}_Y^*(h).
$$

The same definition applies on $X$ or on any $T=T_0\times_{k_0}k$.

*Complement (normalization, scope and duals).* The Tate twist $\Lambda_T(r)$ carries
its canonical Weil structure $\tau_r:\operatorname{Fr}_T^*\Lambda_T(r)\xrightarrow{\sim}\Lambda_T(r)$,
normalized so that geometric Frobenius acts on $\Lambda(r)$ by $q^{-r}$ (hence
by $q^{r}$ on $\Lambda(-r)$); write $\varphi_\Lambda=\tau_0$ for the canonical
structure on $\Lambda_T$. Strict Weil complexes form a category of pairs over
the underlying derived category, not a triangulated (derived) category of Weil
sheaves: its Hom groups are not Ext groups of Weil sheaves (a nonsplit
Frobenius extension of $\Lambda$ by $\Lambda$, a Jordan block, gives no nonzero
map $\Lambda\to\Lambda[1]$ of pairs). For $\Lambda\in\{E,\Qlb\}$, where
$\Dctf=\Dbc$ and $\operatorname{Fr}_T$ is the geometric-Frobenius automorphism
$g_T$, they are the strict Weil complexes of [def-weil-weil-sheaf-complex], and
the triangulated category $D^b_{c,\mathrm W}(T,\Lambda)$ of Weil complexes
defined there maps to them by $K\mapsto(\operatorname{For}(K),\theta_K)$; this
functor is an equivalence on the hearts but not faithful. Only traces, stalk Frobenius maps,
weights of cohomology sheaves, equivariant maps and functorial triangles are
used. For a Weil complex $(K,\phi_K)$ on $T$, the *contragredient datum* on
$K^\vee=R\mathcal Hom_T(K,\Lambda_T)$ is the composite

$$
\phi_{K^\vee}:\operatorname{Fr}_T^*R\mathcal Hom_T(K,\Lambda_T)
\xrightarrow{\sim}R\mathcal Hom_T(\operatorname{Fr}_T^*K,\operatorname{Fr}_T^*\Lambda_T)
\xrightarrow{R\mathcal Hom(\mathrm{id},\varphi_\Lambda)}R\mathcal Hom_T(\operatorname{Fr}_T^*K,\Lambda_T)
\xrightarrow{R\mathcal Hom(\phi_K^{-1},\mathrm{id})}R\mathcal Hom_T(K,\Lambda_T),
$$

the first arrow being the canonical pullback isomorphism, and the datum on the
twisted dual is $\phi_{K^\vee(r)}=\phi_{K^\vee}\otimes\tau_r$.
