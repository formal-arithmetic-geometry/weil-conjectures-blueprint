+++
kind  = "proof"
of    = "prop-weil-pbc-comparison-direct-image"
+++
*The underived map.* For etale $E\to V$ both $\nu_{V,*}u_{\Proet,*}G$ and
$u_{\Et,*}\nu_{U,*}G$ are $E\mapsto G(E\times_VU)$, as in the proof of
[lem-weil-pbc-comparison-pullback]. Let
$\beta_F:\nu_V^*u_{\Et,*}F\to u_{\Proet,*}\nu_U^*F$ be the mate of this
identification under the adjunctions $\nu^*\dashv\nu_*$ of
[def-weil-pbc-site-comparison-morphism]; it is natural in the etale sheaf $F$
on $U$. We show that $\beta_F$ is an isomorphism. This is local on $V$, so take
$V$ affine. By [lem-weil-pbc-ind-etale-basis] it suffices to evaluate on the
basis objects [def-weil-pbc-ind-etale-basis]. Let $W=\varprojlim_iW_i$ be one,
with $W_i\to V$ affine etale of finite presentation, and put
$U_i=U\times_VW_i$ and $U_W=U\times_VW=\varprojlim_iU_i$. The $U_i$ are
quasi-compact, quasi-separated and etale over $U$, because $u$ is
quasi-compact and quasi-separated, and the transition maps are affine. By
[lem-weil-pbc-comparison-sections],

$$
 (\nu_V^*u_{\Et,*}F)(W)=\varinjlim_i(u_{\Et,*}F)(W_i)=\varinjlim_iF(U_i).
$$

On the other side $(u_{\Proet,*}\nu_U^*F)(W)=(\nu_U^*F)(U_W)$. Restricted to
$U_W$, the sheaf $\nu_U^*F$ is computed by the same section formula on the
cofiltered system $(U_i)$, and continuity of sections
[lem-weil-pbc-etale-section-continuity] gives
$(\nu_U^*F)(U_W)=\varinjlim_iF(U_i)$. These identifications are compatible with
$\beta_F(W)$, which is therefore bijective. Hence $\beta$ is an isomorphism.

*Acyclicity of pulled-back injectives.* Let $I$ be an injective etale module
sheaf on $U$. The higher direct images $R^qu_{\Proet,*}\nu_U^*I$ are the
sheafifications of $W\mapsto H^q(U_{W,\Proet},(\nu_U^*I)|_{U_W})$ on the basis
objects $W$, by [lem-weil-pbc-proetale-restriction-injectives]. For $q>0$ these
groups vanish: by [lem-weil-pbc-comparison-global-cohomology] they are the etale
cohomology groups $H^q(U_{W,\Et},I|_{U_W})$, by
[lem-weil-pbc-derived-cohomology-continuity] these are
$\varinjlim_iH^q(U_{i,\Et},I|_{U_i})$, and each $I|_{U_i}$ is injective by
[lem-weil-pbc-etale-restriction-injectives]. So $\nu_U^*I$ is acyclic for
$u_{\Proet,*}$.

*The derived map.* Represent $L$ by a bounded-below complex $I^\bullet$ of
injective etale module sheaves. Then $Ru_{\Et,*}L=u_{\Et,*}I^\bullet$, and
$\nu_V^*$ is exact, so $\nu_V^*Ru_{\Et,*}L=\nu_V^*u_{\Et,*}I^\bullet$. The
complex $\nu_U^*I^\bullet$ represents $\nu_U^*L$ and is a bounded-below
complex of $u_{\Proet,*}$-acyclic sheaves, so
$Ru_{\Proet,*}\nu_U^*L=u_{\Proet,*}\nu_U^*I^\bullet$ (the derived functors are
those of [def-weil-pbc-proetale-operations]; the inverse images are exact by
[prop-weil-pbc-inverse-image-exact] and, applied with $\mathcal A=\Mod_\Lambda$
on sheaves of $\Lambda$-modules, [lem-sfb-finite-upper-star-exact]).
Applied termwise, the isomorphism $\beta$ gives the asserted isomorphism. By
construction it is the base-change morphism of right derived functors induced
by $\beta$, hence natural in $L$. See
[Stacks Project, Section 61.19](https://stacks.math.columbia.edu/tag/099R)
for the comparison's standard setting.
