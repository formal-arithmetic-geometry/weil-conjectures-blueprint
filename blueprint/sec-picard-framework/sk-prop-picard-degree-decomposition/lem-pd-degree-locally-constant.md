+++
id = "lem-pd-degree-locally-constant"
kind = "lemma"
title = "The fibrewise degree is a locally constant function, and is a base-change invariant"
order = 848
uses = ["def-pc-base-change", "def-pc-degree-line-bundle", "def-pc-euler-characteristic", "def-pd-fibrewise-degree", "def-sc-invertible-module", "def-pc-perfect-complex", "lem-pc-degree-base-change", "lem-pc-euler-additive", "lem-pc-flat-complex-derived-pullback", "lem-pc-rf-perfect-base-change", "thm-pc-semicontinuity-base-change"]
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
