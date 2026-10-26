+++
id = "lem-pd-degree-locally-constant"
kind = "lemma"
title = "The fibrewise degree is locally constant for flat families, and is a base-change invariant"
lean = ["AlgebraicGeometry.picardFibreDegree_eq_picardPresheafDegree", "AlgebraicGeometry.picardPresheafDegree_map", "AlgebraicGeometry.isLocallyConstant_picardPresheafDegree", "AlgebraicGeometry.picardPresheafDegree_mul_map_snd"]
order = 828
uses = ["def-pc-base-change", "def-pc-degree-line-bundle", "def-pc-euler-characteristic", "def-pd-fibrewise-degree", "def-sc-invertible-module", "lem-pc-degree-base-change", "lem-pc-rf-perfect-base-change"]
+++
Let $f:X\to S$ be a proper morphism of schemes which is locally of finite
presentation, let $T$ be an $S$-scheme, let $\mathcal{L}$ be an invertible
$\mathcal{O}_{X_T}$-module and let $\deg_T(\mathcal{L})$ be its fibrewise degree
([def-pd-fibrewise-degree]); $f_T:X_T\to T$ is the projection. Then:

1. if $f$ is moreover flat, the function $t\mapsto\deg_T(\mathcal{L})(t)$ is
locally constant on $T$;
1. for every invertible
$\mathcal{O}_T$-module $\mathcal{N}$ one has
$\deg_T(\mathcal{L}\otimes_{\mathcal{O}_{X_T}}f_T^*\mathcal{N}) =\deg_T(\mathcal{L})$;
1. for every morphism $g:T'\to T$ of $S$-schemes one has
$\deg_{T'}\bigl(g_{X}^*\mathcal{L}\bigr)=\deg_T(\mathcal{L})\circ g$,
where $g_X:X_{T'}\to X_T$ is the
base change of $g$;
1. if $S=\Spec(k)$ for a field $k$, then for every field extension $K/k$ and
every morphism $\tau:\Spec(K)\to T$ of $k$-schemes, with image point $t$ and
base change $\tau_X:X_K\to X_T$, the degree of the invertible module
$\tau_X^*\mathcal{L}$ on the proper $K$-scheme $X_K$
([def-pc-degree-line-bundle]) is $\deg_T(\mathcal{L})(t)$.
