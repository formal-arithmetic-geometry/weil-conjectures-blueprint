+++
kind = "proof"
of = "det-prop-diagonal-tower-coefficients"
+++
(1) $\mathcal O_E$ is finite free over $\Zl$, so extension of scalars along
$\Zl\to\mathcal O_E$ is tensoring with a finite free module; it is exact and
commutes with products and with $R\varprojlim$, and with $Rq_*$, $Rp_{i*}$.
Since $\ell^n\mathcal O_E=\pi_E^{en}\mathcal O_E$ up to a unit, where $e$ is
the ramification index, the systems of reductions modulo $\ell^n$ and modulo
$\pi_E^n$ are cofinal, so the $\mathcal O_E$-objects are derived complete with
the expected reductions. Applying the functor to $\delta_{\Zl}$, to the trace
and to the identities of [det-prop-diagonal-tower-trace](2) gives the
$\mathcal O_E$-statements.

(2) Rationalization $-\otimes\mathbf Q$ is the colimit of
$K\xrightarrow{\ell}K\xrightarrow{\ell}\cdots$, and extension to $\Qlb$ is the
filtered colimit over finite extensions $E'/E$. Both are colimits of systems
with a common lower bound, so the direct images $Rq_*$ and $Rp_{i*}$ commute
with them ([sk-lem-bounded-continuity]). Applying them to the morphisms of (1)
gives $\delta_E$, $\delta_{\Qlb}$ and the traces, and the identities, being
equalities of morphisms, are preserved.

(3) After base change along $g$, the diagonal and the sections remain
effective Cartier divisors, and the Cartier extension and the Kummer
sequences are natural under pullback, so the morphisms of systems of
[det-prop-diagonal-tower-system] and [det-prop-diagonal-tower-trace](1) pull
back to the corresponding morphisms over $Y'$. The adjunction between the
constant-system functor and $R\varprojlim$ gives, for an inverse system
$K_\bullet$ of sheaves on $T_{\mathrm{proét}}$ with $T$ one of $Y$,
$\mathbf P^1_Y$, $\mathbf P^1_Y\times_Y\mathbf P^1_Y$, a natural comparison
$g^{-1}R\varprojlim K_\bullet\to R\varprojlim g^{-1}K_\bullet$ in
$D((T\times_YY')_{\mathrm{proét}},\underline{\mathbf Z_\ell})$. For the
systems used here it is an isomorphism, by
[sk-prop-sfb-cartesian-coefficients] for the coefficient systems, closed base
change for $\Delta_*$, and the compatibility of the Tate twist with pullback.
Naturality of this comparison gives the compatibility of $\delta_\Lambda$
with base change, and the base-changed decomposition of $Rq_*$ gives that of
the trace; the statements for $\mathcal O_E$, $E$, $\Qlb$ follow by applying
the coefficient functors of (1) and (2), which commute with pullback.
