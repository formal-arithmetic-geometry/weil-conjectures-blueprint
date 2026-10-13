+++
id = "pur713-input-point-pullback"
kind = "remark"
title = "Pullback from the point"
order = 1813
tags = ["latex:bpinput"]
+++
For every scheme $X$ there is a specified functor

$$
p_X^*:\mathsf{Sh}(*_{\Proet},\mathsf{Ab})\longrightarrow\mathsf{Sh}(X_{\Proet},\mathsf{Ab}),
$$

the composite of the sheafified left Kan extension $p^*$ along the functor $*_{\Proet}\to(\operatorname{Spec}\mathbf Z)_{\Proet}$, $S\mapsto\operatorname{Spec}LC(S,\mathbf Z)$ ($LC$ denoting locally constant functions), with the inverse image $\pi^{-1}_{X,\mathbf Z}$ of Definition “Inverse image of abelian sheaves” (`pur713-def-abelian-pull`) along the structure morphism $\pi_X:X\to\operatorname{Spec}\mathbf Z$. It is strong symmetric monoidal and braided, so it carries condensed rings to commutative ring objects of $\mathsf{Sh}(X_{\Proet},\mathsf{Ab})$. Source: governing reference, §3.2 (established there).
