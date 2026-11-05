+++
id = "proposition-compatibility-purity-base-change--4"
kind = "proposition"
title = "Algebraically closed coefficients"
order = 797008
aliases = ["bp-r239-4"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.smoothOrientation_baseChange", "AlgebraicGeometry.ProEtale.CondensedRing.map_upperShriekUnitTensorMap_comp_upperShriekBaseChange"]
uses = ["definition-relative-dualizing-complex", "definition-exceptional-base-change-map", "theorem-smooth-purity-all-admissible-coefficients"]
+++
The Lean route uses the following two statements with algebraically closed
coefficients. Let $\ell$ be prime, let $k$ be a field of positive
characteristic different from $\ell$, and let the displayed cartesian
square consist of separated schemes of finite type over $k$. Put
$\Lambda=\overline{\mathbf Q}_\ell$ and work in the bounded constructible
pro-étale derived categories $\Dbc(-,\Lambda)$, with the condensed
coefficient ring attached to $\Lambda$.

Write $\omega_f=f^!\Lambda_Y$ and let
$\mu_{f,K}:f^*K\otimes^{\mathbf L}\omega_f\to f^!K$ be the adjoint of
the inverse projection formula followed by the counit at $\Lambda_Y$,
with the tensor factors interchanged as necessary. Let
$b_K:g'^*f^!K\to f'^!g^*K$ be the exceptional base change map of
[definition-exceptional-base-change-map]. With
$c_g:g^*\Lambda_Y\xrightarrow{\sim}\Lambda_{Y'}$ the unit comparison, put

$$
b_\omega=f'^!(c_g)\circ b_{\Lambda_Y}:
g'^*\omega_f\longrightarrow\omega_{f'}.
$$

1. Suppose $f$ and $f'$ are smooth of pure relative dimension $d$.
   Write $T_X=\Lambda_X(d)[2d]$ and let
   $o_f:T_X\xrightarrow{\sim}\omega_f$ and
   $o_{f'}:T_{X'}\xrightarrow{\sim}\omega_{f'}$ be the orientations
   chosen in Lean. There exists an isomorphism
   $\tau:g'^*T_X\xrightarrow{\sim}T_{X'}$ such that
   $$
   b_\omega\circ g'^*o_f=o_{f'}\circ\tau.
   $$
   The isomorphism $\tau$ is not prescribed to be the canonical pullback
   comparison for Tate twists.
2. For any $K\in\Dbc(Y,\Lambda)$, let
   $$
   h_K:g'^*(f^*K\otimes^{\mathbf L}\omega_f)
   \xrightarrow{\sim}f'^*g^*K\otimes^{\mathbf L}g'^*\omega_f
   $$
   be the tensor comparison for $g'^*$ followed by
   $g'^*f^*\simeq f'^*g^*$. Then
   $$
   b_K\circ g'^*\mu_{f,K}
   =\mu_{f',g^*K}\circ(1\otimes b_\omega)\circ h_K.
   $$
   This identity does not require $f$ or $f'$ to be smooth.
