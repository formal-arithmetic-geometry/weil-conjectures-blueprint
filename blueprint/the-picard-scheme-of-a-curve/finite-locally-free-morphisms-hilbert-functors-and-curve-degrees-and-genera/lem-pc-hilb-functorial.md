+++
id = "lem-pc-hilb-functorial"
kind = "lemma"
title = "The Hilbert functor is a functor"
order = 4282
lean = ["AlgebraicGeometry.hilbFunctor_isFunctor"]
uses = ["def-pc-hilb-functor", "def-pc-finite-locally-free", "def-pc-base-change", "lem-pc-flf-properties", "lem-pc-closed-imm-base-change", "lem-pc-flat-base-change-cohom"]
+++
Let $X\to S$ be a morphism of schemes and $d\ge0$. The assignment
$T\mapsto\operatorname{Hilb}^d_{X/S}(T)$ of [def-pc-hilb-functor] is a
functor $(\mathit{Sch}/S)^{\mathrm{op}}\to\textit{Sets}$: for $g:T'\to T$
and $Z\in\operatorname{Hilb}^d_{X/S}(T)$, the base change
$Z_{T'}:=Z\times_TT'$ is a closed subscheme of $X_{T'}$ finite locally free
of degree $d$ over $T'$.

## Proof

The fibre square $X_{T'}=X_T\times_TT'$ shows $Z_{T'}\subset X_{T'}$ is a
closed subscheme (base change of the closed immersion $Z\subset X_T$:
closed immersions are stable under base change,
[lem-pc-closed-imm-base-change]). Its structure morphism $Z_{T'}\to T'$ is
the base change of $Z\to T$, hence finite, flat and locally of finite
presentation (finite: base change of finite; flat: base change of flat;
locally of finite presentation: base change of the same); and the degree is
$d$ (by base change: for $t'\in T'$ over $t\in T$ the fibre
$Z_{T',t'}=Z_t\otimes_{\kappa(t)}\kappa(t')$, and
$\Gamma(Z_{t'},\mathcal{O})=\Gamma(Z_t,\mathcal{O})\otimes\kappa(t')$ by
[lem-pc-flf-properties] and [lem-pc-flat-base-change-cohom], of dimension
$d$).
