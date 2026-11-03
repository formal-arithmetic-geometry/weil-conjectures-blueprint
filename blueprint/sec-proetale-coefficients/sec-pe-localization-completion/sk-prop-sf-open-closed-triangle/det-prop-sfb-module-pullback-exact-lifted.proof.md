+++
kind = "proof"
of = "det-prop-sfb-module-pullback-exact-lifted"
uses = ["lem-sfb-modobj-forget-left-exact", "lem-sfb-modobj-forget-right-exact", "lem-sfb-modobj-forget-faithful"]
+++
Write $U_{\mathcal R}$ and $U_{F(\mathcal R)}$ for the forgetful functors. By construction of the
transport, $U_{F(\mathcal R)}\circ\operatorname{mapMod}(F)=F\circ U_{\mathcal R}$.

**$U_{F(\mathcal R)}$ reflects isomorphisms.** It is faithful
([lem-sfb-modobj-forget-faithful]). If $\varphi\colon M\to N$ is a module map whose underlying
morphism has an inverse $\psi$, then
$\psi\gamma_N=\psi\gamma_N(F(\mathcal R)\otimes\varphi)(F(\mathcal R)\otimes\psi)
=\psi\varphi\gamma_M(F(\mathcal R)\otimes\psi)=\gamma_M(F(\mathcal R)\otimes\psi)$, so $\psi$ is a
module map and $\varphi$ is an isomorphism of module objects.

**Left exactness.** Let $J$ be a finite category and $D\colon J\to\Mod_{\mathcal R}(\mathcal C)$ a
diagram with limit cone $c$. The forgetful functor $U_{\mathcal R}$ preserves finite limits
([lem-sfb-modobj-forget-left-exact]), and $F$ does by assumption, so
$U_{F(\mathcal R)}(\operatorname{mapMod}(F)(c))=F(U_{\mathcal R}(c))$ is a limit cone in $\mathcal D$.
The category $\Mod_{F(\mathcal R)}(\mathcal D)$ has finite limits, and $U_{F(\mathcal R)}$ preserves
them ([lem-sfb-modobj-forget-left-exact]); comparing $\operatorname{mapMod}(F)(c)$ with a limit cone of
$\operatorname{mapMod}(F)\circ D$, the comparison map becomes an isomorphism after applying
$U_{F(\mathcal R)}$, hence is an isomorphism because $U_{F(\mathcal R)}$ reflects isomorphisms. So
$\operatorname{mapMod}(F)(c)$ is a limit cone.

**Right exactness.** The same argument with finite colimits, using
[lem-sfb-modobj-forget-right-exact] for both forgetful functors.
