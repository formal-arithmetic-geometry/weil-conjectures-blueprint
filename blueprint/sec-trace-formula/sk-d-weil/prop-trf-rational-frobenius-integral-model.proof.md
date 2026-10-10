+++
kind  = "proof"
of    = "prop-trf-rational-frobenius-integral-model"
+++
*(1).* By [def-weil-rationalization-karoubi] the morphisms of
$D^b_c(X,E)$ are
$\operatorname{Hom}_{D^b_c(X,\mathcal O_E)}(Lg_\gamma^*K_{\mathcal O},K_{\mathcal O})\otimes_{\mathcal O_E}E$,
the rationalized pullback being that of the integral one
([prop-weil-pbc-rational-transport]). Since $E=\mathcal O_E[1/\varpi]$,
every element of $H\otimes_{\mathcal O_E}E=H[1/\varpi]$, for an
$\mathcal O_E$-module $H$, has the form $u\otimes\varpi^{-N}$ with
$u\in H$ and $N\geq0$. This is $\varphi_E=\varpi^{-N}u$.

*(2).* The reduction $u_n$ is the $n$-th evaluation of the morphism of
towers attached to $u$ by the functorial reduction tower of
[def-weil-pbc-adic-coefficient-datum], using
$(Lg_\gamma^*K_{\mathcal O})\otimes^L A_n\cong Lg_\gamma^*K_n$: since
$g_\gamma$ is an automorphism, $Lg_\gamma^*$ is an exact monoidal
equivalence fixing the constant coefficient sheaves
([def-weil-derived-pullback-tensor-hom]), so it commutes with the
reductions and with the transitions. Hence the $u_n$ are compatible with
the transitions. The isomorphism $\kappa$ of
[prop-trf-scheme-galois-comparison] is composed of the functoriality of
pullback for $\Phi=g_\gamma F_X^{(q)}$ and the trivialization of
absolute-Frobenius pullback of [lem-trf-absolute-frobenius-site], which is
induced on the pro-etale site itself; both are natural in the object and
compatible with the monoidal reduction $-\otimes^L_{A_{n+1}}A_n$.
Therefore $\psi_n=u_n\circ\kappa_{K_n}$ is a morphism
$L\Phi^*K_n\to K_n$, i.e. a Frobenius coefficient morphism, and the
$\psi_n$ are compatible with the transitions.

For the iterates argue by induction on $m$, the case $m=1$ being the
definition. Suppressing the composition isomorphisms of pullback (they
are part of both recursive definitions), the recursion of
[def-trf-frobenius-coefficient-morphism] and the induction hypothesis
give

$$
\psi_{n,m}=\psi_n\circ L\Phi^*\psi_{n,m-1}
=u_n\circ\kappa_{K_n}\circ L\Phi^*\bigl(u_n^{[m-1]}\bigr)\circ
L\Phi^*\bigl(\kappa^{(m-1)}_{K_n}\bigr).
$$

Naturality of $\kappa$ applied to
$u_n^{[m-1]}:Lg_\gamma^{(m-1)*}K_n\to K_n$ gives
$\kappa_{K_n}\circ L\Phi^*(u_n^{[m-1]})
=Lg_\gamma^*(u_n^{[m-1]})\circ\kappa_{Lg_\gamma^{(m-1)*}K_n}$, and the
multiplicativity of the iterates in [prop-trf-scheme-galois-comparison],
for $m=1+(m-1)$, gives
$\kappa_{Lg_\gamma^{(m-1)*}K_n}\circ L\Phi^*(\kappa^{(m-1)}_{K_n})
=\kappa^{(m)}_{K_n}$. Hence
$\psi_{n,m}=u_n\circ Lg_\gamma^*(u_n^{[m-1]})\circ\kappa^{(m)}_{K_n}
=u_n^{[m]}\circ\kappa^{(m)}_{K_n}$.

*(3).* The first equality is the definition of $F_{c,m}(\psi_n)$ in
[def-trf-frobenius-coefficient-morphism]. By (2),
$\psi_{n,m}=v\circ\kappa^{(m)}_{K_n}$ with $v=u_n^{[m]}$, and the general
clause of [prop-trf-graph-frobenius-operator], which allows an arbitrary,
not necessarily invertible $v$ and no Weil structure on $K_n$, gives
$T_{c_m}(\psi_{n,m})=R\Gamma_c(X,u_n^{[m]})\circ g_{\gamma,c}^{m,*}$.

By [def-weil-integral-rational-qbar-compact-support],
$R\Gamma_c(X,-)$ on $D^b_c(X,\mathcal O_E)$ is the derived limit of the
levelwise compact-support cohomology of the reduction tower of
[def-weil-pbc-adic-coefficient-datum]; on morphisms it is the derived
limit of the levelwise maps. The integral morphism $u^{[m]}$ (formed from
$u$ by the integral pullbacks) has reductions $u_n^{[m]}$, because
$Lg_\gamma^{i*}$ commutes with the reductions as in (2); and the integral
base-change isomorphism $g_{\gamma,c}^{m,*}$ is the derived limit of the
levelwise ones, the pullback $Lg_\gamma^{m*}$ carrying the reduction tower
of $K_{\mathcal O}$ to that of $Lg_\gamma^{m*}K_{\mathcal O}$. Hence
$U_m$ is the derived limit of the levelwise composites
$R\Gamma_c(X,u_n^{[m]})\circ g_{\gamma,c}^{m,*}=F_{c,m}(\psi_n)$.

At the stage $E$, $R\Gamma_c(X,K_E)=R\Gamma_c(X,K_{\mathcal O})\otimes_{\mathcal O_E}E$
([def-weil-integral-rational-qbar-compact-support]), and every
rationalized functor or natural transformation acts on
$\operatorname{Hom}\otimes_{\mathcal O_E}E$ by $f\otimes\lambda\mapsto
F(f)\otimes\lambda$ ([prop-weil-pbc-rational-transport]); composition in
$D^b_c(X,E)$ is $E$-bilinear. Hence
$L(g_\gamma^{i})^*\varphi_E=\varpi^{-N}\,L(g_\gamma^{i})^*u$ for each $i$,
the composition isomorphisms are those of the integral pullbacks, and

$$
\varphi_E^{[m]}=\prod_{i=0}^{m-1}\varpi^{-N}\cdot
\bigl(u\circ Lg_\gamma^*u\circ\cdots\circ L(g_\gamma^{m-1})^*u\bigr)
=\varpi^{-Nm}u^{[m]}.
$$

Applying the $E$-linear map induced by the rationalized $R\Gamma_c(X,-)$
and composing with the rationalization of the integral
$g_{\gamma,c}^{m,*}$ gives
$F_{c,K_E}^{\,m}=\varpi^{-Nm}\bigl(R\Gamma_c(X,u^{[m]})\circ g_{\gamma,c}^{m,*}\bigr)\otimes E
=\varpi^{-Nm}(U_m\otimes E)$.

*(4).* By the stalk normalization and (2),
$\psi_{n,m,\bar y}=(u_n^{[m]})_{\bar y}\circ(\kappa^{(m)}_{K_n})_{\bar y}\circ\iota_{K_n}
=u^{[m]}_{n,\bar y}\circ\tau_{y,m}$. The stalk functor $L\bar y^*$ is a
pullback, hence monoidal and compatible with the reductions
([def-weil-derived-pullback-tensor-hom]), and $\tau_{y,m}$ is natural and
compatible with the reductions by the same argument as for $\kappa$ in
(2), its integral form being the derived limit of the levelwise ones; so
$U_{y,m}=u^{[m]}_{\bar y}\circ\tau_{y,m}$ reduces modulo
$\varpi^n$ to $u^{[m]}_{n,\bar y}\circ\tau_{y,m}=\psi_{n,m,\bar y}$. At
the stage $E$, the stalk of $K_E$ is $K_{\mathcal O,\bar y}\otimes E$ and,
exactly as in (3), $\varphi^{[m]}_{E,\bar y}=\varpi^{-Nm}(u^{[m]}_{\bar y}\otimes E)$,
whence $F_{y,m}=\varphi^{[m]}_{E,\bar y}\circ\tau_{y,m}
=\varpi^{-Nm}(U_{y,m}\otimes E)$.

The remark on $(N+1,\varpi u)$ is $(\varpi u)^{[m]}=\varpi^mu^{[m]}$, by
$\mathcal O_E$-linearity of the pullbacks. In the example, identify the
coefficient categories of $X=\Spec k$ with complexes of modules, so that
$u=\operatorname{diag}(1,\ell)$ is an endomorphism of the lattice
$\mathcal O_E^2$. If $c\,\varphi_E$ were an automorphism of some lattice
$L\subset E^2$, then its characteristic polynomial and that of its inverse
would have coefficients in $\mathcal O_E$, so its eigenvalues $c$ and
$c\ell$ would both be units of the integral closure of $\mathcal O_E$;
then so would be their quotient $\ell$, which is absurd.
