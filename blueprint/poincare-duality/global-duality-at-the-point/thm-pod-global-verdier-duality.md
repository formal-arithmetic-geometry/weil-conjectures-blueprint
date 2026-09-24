+++
id = "thm-pod-global-verdier-duality"
kind = "theorem"
title = "Global Verdier duality at the point"
order = 3805
uses = ["def-pod-conventions", "def-weil-finite-coefficient-point", "def-weil-ordinary-compact-cohomology", "def-weil-site-perfect-complex", "fix-cor-verdier-exchange", "lem-fix-operation-reduction", "lem-pod-point-dualizing-complex", "thm-pur-finite-reduction-of-purity"]
+++
Use the Poincare duality conventions,
and let $K\in D^b_{ctf}(X,\Lambda)$. For the admissible structure
morphism $a_X:X\to s$ there is a canonical isomorphism

$$
R\Gamma_c(X,K)^\vee\xrightarrow{\sim}R\Gamma(X,\mathbb D_XK),
$$

with the cohomology functors
of the fixed coefficient stage. It is natural in $K$ and compatible
with shifts. For a site-perfect
$K$, it is also compatible with finite coefficient reduction and
scalar extension under the smooth orientation and its coefficient
comparisons. At $K=\Lambda_X$ it identifies
$R\Gamma_c(X,\Lambda_X)^\vee$ with $R\Gamma(X,\omega_{X,\Lambda})$.

## Proof

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
