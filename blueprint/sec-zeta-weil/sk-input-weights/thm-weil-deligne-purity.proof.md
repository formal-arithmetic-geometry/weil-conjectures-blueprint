+++
kind  = "proof"
of    = "thm-weil-deligne-purity"
+++
*Step 1: the main-route purity input.* The constant
$\Qlb$-Weil sheaf $(\Qlb)_X$ is the constant $\Qlb$-sheaf of
[cor-zl-purity-smooth-proper] of the zeta chapter on the smooth and
proper $X_0$ of pure dimension $d$: the
smoothness, properness, coefficient, embedding $\iota$, and
Frobenius data of that corollary are exactly those fixed in the
statement, and the cohomological family is extended to $\Qlb$ with
the Frobenius operator $F_{\Qlb}$ as in the constant-sheaf setting
there. Hence, for every $0\leq i\leq2d$,
$(H^i(X,\Qlb),F_{\Qlb})$ is $\iota$-pure of weight $i$ in the sense of
[def-weil-frobenius-module-weights] – this is assertion (4).

For assertion (2), apply the general $Rf_!$ weight theorem
[thm-zl-wme-deligne-estimate] to the structure morphism
$a_{X_0}:X_0\to\Spec k_0$ and to $K=(\Qlb)_{X_0}$, viewed as a
complex concentrated in degree $0$. Its only cohomology sheaf is the
constant sheaf, punctually $\iota$-pure of weight $0$ by
[lem-zl-constant-sheaf-weight-zero], so $K\in D_{\le0}(X_0)$ in the
sense of [def-weil-complex-weights]. Hence
$Ra_{X_0!}K\in D_{\le0}(\Spec k_0)$: its degree-$i$ cohomology sheaf,
whose stalk at the unique closed point (with $q_y=q$) is
$H_c^i(X,\Qlb)$ with its geometric Frobenius, is $\iota$-mixed of
weights at most $i$. This is assertion (2); it is the absolute case of
the relative estimate, which bounds $Rf_!$ on every bounded
constructible Weil complex.

In addition, the proper coincidence
$H_c^i(X,\Qlb)\xrightarrow{\sim}H^i(X,\Qlb)$ in the form of
[prop-weil-proper-compact-coincidence] is Frobenius-equivariant,
which is assertion (3), and it transfers the mixed bound of assertion
(2) from $H_c^i$ to $H^i$.

*Step 2: the eigenvalue bound – assertion (5).* By
[def-weil-frobenius-module-weights], $\iota$-purity of weight
$i$ of the Frobenius module $(H^i(X,\Qlb),F_{\Qlb})$ means
precisely that every eigenvalue $\alpha$ of $F_{\Qlb}$ on
$H^i(X,\Qlb)$ satisfies $|\iota(\alpha)|=q^{i/2}$, which is
assertion (5).

*Step 3: the constant Weil sheaf is pure of weight $0$ –
assertion (1).* Let $K=(\Qlb)_X$, with the canonical Weil
structure, and use the two predicates of [def-weil-complex-weights].
The cohomology sheaves of
$\operatorname{For}K$ are $(\Qlb)_X$ in degree $0$ and $0$
elsewhere. The constant sheaf is punctually $\iota$-pure of weight
$0$: its local Frobenius operators are the identities on the
one-dimensional stalks ([def-trf-frobenius-operators]), so every
local eigenvalue is $1$, with $|\iota(1)|=1=q_y^{0/2}$ for the
residue-field base $q_y$, which is the definition of
[def-weil-punctual-weights] (this is [lem-zl-constant-sheaf-weight-zero]). Hence
$\Wt_{\iota,\leq0}(K)$ holds. For the lower predicate, the dual
complex $D_XK$ of [def-weil-complex-weights] is

$$
D_XK=R\mathcal Hom_{\Qlb}\bigl(K,\omega_X\bigr),
\qquad \operatorname{For}(\omega_X)=Ra_X^!\Qlb,
$$

by the dualizing Weil complex fixed in [def-weil-complex-weights]
(the constructible exceptional inverse image of the structure morphism,
with its canonical Weil lift) and
[def-weil-derived-pullback-tensor-hom]; the smooth-dualizing
identification [thm-sf-dual-perfect] gives

$$
D_XK\cong(\Qlb)_X^{\vee}(d)[2d]\cong(\Qlb(d))_X[2d],
$$

the coefficient dual $(\Qlb)_X^{\vee}$ of the constant rank-one sheaf
being the constant rank-one sheaf
([def-weil-derived-pullback-tensor-hom]), and the twist
$(\Qlb(d))_X$ carrying the canonical Weil structure. Its only
cohomology sheaf, in degree $-2d$, is $((\Qlb(d))_X)$, punctually
$\iota$-pure of weight $-2d$: the local geometric Frobenius acts on
$\Qlb(d)$ by the scalar $q^{-d}$
([def-weil-frobenius-coefficient-twists]), so every local
eigenvalue is $q^{-d}$ with
$|\iota(q^{-d})|=q^{-d}=q^{(-2d)/2}$, by
[def-weil-punctual-weights]. The weight $0+j$ required at
$j=-2d$ by [def-weil-complex-weights] is therefore available:
$-2d=0+(-2d)$. Thus $\Wt_{\iota,\leq0}(D_XK)$ holds, i.e.
$\Wt_{\iota,\geq0}(K)$, and with $\Wt_{\iota,\leq0}(K)$ the
constant Weil sheaf $(\Qlb)_X$ is $\iota$-pure of weight $0$.
This is assertion (1), and all five assertions of the statement are
established.
