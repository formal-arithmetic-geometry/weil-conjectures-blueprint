+++
kind = "proof"
of = "lemma-vanishing-local-term-zero-stalk--1"
order = 989003
uses = ["lemma-flat-models-generators", "lemma-covers-degree-prime-to-ell", "lemma-tangent-cones-on-cover", "lemma-vanishing-restrictions-after-blowing-up", "lemma-descent-vanishing-finite-etale", "proposition-dctf-x-qbar-2-colimit", "proposition-inverting-ell", "proposition-six-operations-change-coefficients", "lemma-perfect-complexes-geometric-point", "theorem-bounded-below-cohomology-comparison", "proposition-comparison-immersions"]
+++
For finite coefficients, the stalk of $P$ at the closed point of $T$
is $L_{\bar y}\otimes^{\mathbf L}K_{\bar y}=0$. Strict locality gives
$R\Gamma(T,P)=0$ and $R\Gamma(\Delta,\delta^*P)=0$.
The localization triangles therefore reduce the assertion to the
vanishing of the restriction from $T-\Gamma$ to $\Delta-y$. Put
$V=\{y\}\times X$ and $H=X\times\{y\}$, pulled back to $T$.
Since $\Delta-y$ lies in $O=T-(\Gamma\cup V)$, it suffices to kill

$$
R\Gamma(O,P)\longrightarrow R\Gamma(\Delta-y,\delta^*P).
$$

Choose bounded flat constructible models of $L$ and $K$ by
Lemma [lemma-flat-models-generators]. Their restrictions to the
punctured strictly local traits have finite locally constant terms.
The cover construction of Lemma [lemma-covers-degree-prime-to-ell]
is applied simultaneously to both models. In Lean it gives a single
cover datum, with a point of ramification index $e$ prime to $\ell$;
using this cover on both factors gives a finite étale cover of the
punctured diagonal of degree $e^2$.

On the resulting strictly local surface $T'$, the reduced inverse
images $D'=(\Gamma'\cup V')_{\mathrm{red}}$, $H'_{\mathrm{red}}$ and
$\Delta'_{\mathrm{red}}$ have the tangent-cone properties of
Lemma [lemma-tangent-cones-on-cover]. Since $K_{\bar y}=0$, localization
expresses $K$ as extension by zero from the punctured trait. Thus on
$T'-D'$ the pullback of $P$ is extension by zero across $H'$ of a bounded
complex with finite $\ell$-group monodromy. This is the data supplied by
`AlgebraicGeometry.Etale.CurveLocalModel.exists_restrictionZeroCover`.
Lemma [lemma-vanishing-restrictions-after-blowing-up] kills the
restriction upstairs. Its compatibility with pullback and the finite
étale trace of Lemma [lemma-descent-vanishing-finite-etale] give the
vanishing downstairs, because $e^2$ is invertible in $A$.

For $\Qbarl$ coefficients, first choose a model over $\mathcal O_E$ for
some finite $E/\mathbf Q_\ell$, using Proposition
[proposition-dctf-x-qbar-2-colimit] and Proposition [proposition-inverting-ell].
If $j:X-\{y\}\hookrightarrow X$, replace this model by $j_!j^*$ of it.
Since $K_{\bar y}=0$, this is still a model of $K$, and its stalk at $y$
is zero. This construction is
`AlgebraicGeometry.ProEtale.CondensedRing.exists_integralModel_isZero_upperStar`.
Write $M$ for the resulting model and $N=\mathbb D_XM$.

Let $f_0$ be the point fibre of the integral supported restriction for
$M\boxtimes N$. Its source and target are perfect $\mathcal O_E$-complexes
by Lemma [lemma-perfect-complexes-geometric-point]. For every $n\geq1$,
the finite-coefficient comparison and the compatibilities of Proposition
[proposition-six-operations-change-coefficients] identify the reduction
of this map with a classical supported restriction; the interchange of
the factors puts the zero-stalk factor second. More precisely,
`AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.exists_reduction_pointIntegralSupportedRestriction`
gives a distinguished triangle whose first map is multiplication by
$\ell^n$ on the target of $f_0$, and a commutative square through a
classical supported restriction. The finite-coefficient result makes
the latter map zero. Exactness then makes $f_0$ divisible by every
$\ell^n$. The Krull intersection theorem for morphisms between perfect
complexes gives $f_0=0$; in Lean this is
`AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.eq_zero_of_forall_reduction`.

Finally extend scalars from $\mathcal O_E$ to $E$ and then to $\Qbarl$.
Compatibility of the supported restriction, external products and
Verdier duality with these maps, together with faithfulness of the point
fibre functor over $\Qbarl$, gives $z^*\rho_{P'}=0$.
