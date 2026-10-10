+++
kind  = "proof"
of    = "thm-pod-global-verdier-duality"
+++
Apply the independently proved exchange [fix-cor-verdier-exchange]
to $f=a_X$ and the coefficient object at $s$:

$$
D_sRa_{X!}K\cong Ra_{X*}D_XK.
$$

By [lem-pod-point-dualizing-complex], $D_s$ is the derived
coefficient dual. Apply the point equivalence of
[def-weil-finite-coefficient-point]; the two resulting global
functors are those of [def-weil-ordinary-compact-cohomology].
This proves the asserted isomorphism and its naturality and shift
compatibility. Its construction uses only tensor–Hom adjunction,
the compact-support projection formula, and the adjunction for
$Ra_{X!}$; it does not use global Poincare duality.
For $K$ site-perfect in the sense of
[def-weil-site-perfect-complex], the tensor, internal-Hom,
evaluation, and cohomology comparisons are
[lem-fix-operation-reduction]. The smooth dualizing object and
its counit reduce compatibly by
[thm-pur-finite-reduction-of-purity]. Each constituent of the
adjunction comparison therefore commutes with coefficient change,
so their composite does too. Finally $D_X\Lambda_X=\omega_X$
by tensor–Hom evaluation of the unit object, giving the specialization.
Properness of $X_0$ is used nowhere above: the exchange
[fix-cor-verdier-exchange] needs only that $a_X$ is exceptionally
admissible, $Ra_{X!}$ and $Ra_{X*}$ enter as different functors with no
comparison between them, and the smooth dualizing object and its finite
reduction ([thm-pur-finite-reduction-of-purity]) are stated for smooth
separated morphisms. The same argument applies word for word to a smooth
proper $X$ over $k$ that is not defined over $k_0$, which is the proper
case of [thm-sf-global-duality].
