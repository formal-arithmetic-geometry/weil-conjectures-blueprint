+++
id = "lem-pd-degree-locally-constant"
kind = "lemma"
title = "The fibrewise degree is locally constant, and is a base-change invariant"
order = 4703
lean = ["AlgebraicGeometry.Curve.isLocallyConstant_fibrewiseDegree"]
uses = ["def-pd-fibrewise-degree"]
+++
In the situation of [def-pd-fibrewise-degree]:

1. the function $t\mapsto\deg_T(\mathcal{L})(t)$ is locally constant on $T$;
2. for every invertible $\mathcal{O}_T$-module $\mathcal{N}$ one has
   $\deg_T(\mathcal{L}\otimes_{\mathcal{O}_{C_T}}f_T^*\mathcal{N})=\deg_T(\mathcal{L})$,
   where $f_T:C_T\to T$ is the structure morphism;
3. for every morphism $g:T'\to T$ of $k$-schemes one has
   $\deg_{T'}(g_C^*\mathcal{L})=\deg_T(\mathcal{L})\circ g$, where
   $g_C:C_{T'}\to C_T$ is the base change of $g$.

## Proof

We work throughout in the situation of [def-pd-fibrewise-degree].

*(1) Local constancy.* The question is local on $T$, so let $T=\Spec(A)$ be
affine and let $t\in T$ with residue field $\kappa(t)$. The sheaf
$\mathcal{L}$ is an invertible $\mathcal{O}_{C_A}$-module, and
$C_A\to\Spec(A)$ is proper and flat with one-dimensional fibres. For each $i$
the $\mathcal{O}_A$-module $H^i(C_A,\mathcal{L})$ is coherent, and formation
of its fibre commutes with base change along $A\to\kappa(t)$, so
$\dim_{\kappa(t)}H^i(C_{\kappa(t)},\mathcal{L}_t)$ is computed from
$H^i(C_A,\mathcal{L})\otimes_A\kappa(t)$. The function
$$
t\mapsto\sum_i(-1)^i\dim_{\kappa(t)}\bigl(H^i(C_A,\mathcal{L})\otimes_A\kappa(t)\bigr)
$$
is therefore the Euler characteristic of a bounded complex of finitely
generated $A$-modules, hence locally constant on $\Spec(A)$; the second term
is the same function for $\mathcal{L}=\mathcal{O}_{C_A}$ and is likewise
locally constant. Subtracting gives (1).

*(2) Twisting by a pullback.* The fibrewise degree is unchanged by extension
of the base field, so it suffices to compute at a point $t$ after base change
to $\kappa(t)$. Over the field $\kappa(t)$ the projection formula gives
$\chi(C_t,\mathcal{L}_t\otimes f_t^*\mathcal{N}_t)=\chi(C_t,\mathcal{L}_t)$,
because $f_t^*\mathcal{N}_t$ is the pullback of an invertible module on
$\Spec\kappa(t)$ and hence trivial. The asserted equality follows, with the
additivity of $\chi$ supplying the computation.

*(3) Base change.* For $t'\in T'$ with image $t\in T$ the residue field
$\kappa(t')$ is an extension of $\kappa(t)$ and
$(g_C^*\mathcal{L})_{t'}=(\mathcal{L}_t)_{\kappa(t')}$; the equality is the
base-change invariance of the degree applied to the field extension
$\kappa(t')/\kappa(t)$.

Unresolved dependencies: def:sc-invertible-module, def:pc-base-change, def:pc-degree-line-bundle, def:pc-euler-characteristic, lem:pc-degree-base-change, lem:pc-euler-additive, lem:pc-flat-base-change-cohom, lem:pc-coherent-hi
