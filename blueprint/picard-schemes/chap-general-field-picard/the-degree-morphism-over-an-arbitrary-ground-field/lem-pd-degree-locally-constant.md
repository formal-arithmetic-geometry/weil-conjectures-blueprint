+++
id = "lem-pd-degree-locally-constant"
kind = "lemma"
title = "The fibrewise degree is a locally constant function, and is a base-change invariant"
order = 2651
uses = ["def-pc-base-change", "def-pc-degree-line-bundle", "def-pc-euler-characteristic", "def-pd-fibrewise-degree", "def-sc-invertible-module", "lem-pc-coherent-hi", "lem-pc-degree-base-change", "lem-pc-euler-additive", "lem-pc-flat-base-change-cohom"]
+++
In the situation of [def-pd-fibrewise-degree]:

1. the function $t\mapsto\deg_T(\mathcal{L})(t)$ is locally constant on $T$;
1. for every invertible
$\mathcal{O}_T$-module $\mathcal{N}$ one has
$\deg_T(\mathcal{L}\otimes_{\mathcal{O}_{C_T}}f_T^*\mathcal{N}) =\deg_T(\mathcal{L})$, where $f_T:C_T\to T$ is the structure morphism;
1. for every morphism $g:T'\to T$ of $k$-schemes one has
$\deg_{T'}\bigl(g_{C}^*\mathcal{L}\bigr)=\deg_T(\mathcal{L})\circ g$,
where $g_C:C_{T'}\to C_T$ is the
base change of $g$.

## Proof

We work throughout in the situation of [def-pd-fibrewise-degree], so
that the degree is the [def-pc-degree-line-bundle] and $\chi$ is the
[def-pc-euler-characteristic] of the fibre, and fibre products are those
of [def-pc-base-change].

*(1) Local constancy.* The question is local on $T$, so let
$T=\Spec(A)$ be affine and let $t\in T$ with residue field $\kappa(t)$. The
sheaf $\mathcal{L}$ is an invertible $\mathcal{O}_{C_A}$-module, and $C_A\to \Spec(A)$ is proper and flat with one-dimensional fibres. For each $i$ the
$\mathcal{O}_A$-module $H^i(C_A,\mathcal{L})$ is coherent
([lem-pc-coherent-hi]), and formation of its fibre commutes with base
change along $A\to\kappa(t)$ ([lem-pc-flat-base-change-cohom]), so
$\dim_{\kappa(t)}H^i(C_{\kappa(t)},\mathcal{L}_t)$ is computed from
$H^i(C_A,\mathcal{L})\otimes_A\kappa(t)$. The function
$t\mapsto\sum_i(-1)^i\dim_{\kappa(t)}\bigl(H^i(C_A,\mathcal{L})\otimes_A\kappa(t)\bigr)$
is therefore the Euler characteristic of a bounded complex of finitely
generated $A$-modules, hence locally constant on $\Spec(A)$; the second term
is the same function for $\mathcal{L}=\mathcal{O}_{C_A}$ and is likewise
locally constant. Subtracting gives (1).

*(2) Twisting by a pullback.* By [lem-pc-degree-base-change](1)
the fibrewise degree is unchanged by extension of the base field, so it
suffices to compute at a point $t$ after base change to $\kappa(t)$. Over the
field $\kappa(t)$ the projection formula in the form of
[lem-pc-degree-base-change](2) gives
$\chi\bigl(C_t,\mathcal{L}_t\otimes f_t^*\mathcal{N}_t\bigr) =\chi\bigl(C_t,\mathcal{L}_t\bigr)$, because
$f_t^*\mathcal{N}_t$ is the pullback of an invertible module on
$\Spec\kappa(t)$ and hence trivial. The asserted equality follows, and
[lem-pc-euler-additive] supplies the additivity of $\chi$ used here.

*(3) Base change.* For $t'\in T'$ with image $t\in T$ the residue field
$\kappa(t')$ is an extension of $\kappa(t)$ and
$(g_C^*\mathcal{L})_{t'}=(\mathcal{L}_t)_{\kappa(t')}$; the equality is
[lem-pc-degree-base-change](1) applied to the field extension
$\kappa(t')\big/\kappa(t)$.
