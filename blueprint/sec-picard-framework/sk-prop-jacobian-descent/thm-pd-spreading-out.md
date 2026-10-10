+++
id = "thm-pd-spreading-out"
kind = "theorem"
title = "Descent of finitely presented data at a filtered limit"
order = 862
uses = ["def-pc-base-change", "def-pc-morphism-conventions"]
+++
Let $I$ be a directed set, let $(S_i,f_{ii'})$ be an inverse system of schemes
over $I$ with affine transition morphisms and $S_i$ quasi-compact and
quasi-separated, and put $S=\varprojlim_iS_i$. Then:

1. for every morphism of finite presentation $V\to S$ there are $i\in I$ and
a morphism of finite presentation $V_i\to S_i$ with
$V\cong V_i\times_{S_i}S$;
1. given $i$, schemes $V_i,W_i$ of finite presentation over $S_i$ and a
morphism $\psi:V_i\times_{S_i}S\to W_i\times_{S_i}S$, there are $i'\geq i$
and a morphism $\psi_{i'}:V_i\times_{S_i}S_{i'}\to W_i\times_{S_i}S_{i'}$
whose base change to $S$ is $\psi$;
1. given $i$, schemes $V_i,W_i$ of finite presentation over $S_i$ and two
morphisms $\psi_i,\chi_i:V_i\to W_i$ whose base changes to $S$ agree,
there is $i'\geq i$ with
$\psi_i\times_{S_i}S_{i'}=\chi_i\times_{S_i}S_{i'}$.
