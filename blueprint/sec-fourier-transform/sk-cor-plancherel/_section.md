+++
id = "sk-cor-plancherel"
kind = "corollary"
title = "Plancherel"
lean = ["FiniteField.sum_norm_sq_fourierTransform"]
order = 3957
uses = ["sk-lem-as-properties", "sk-thm-inversion", "sk-def-sf-weil-complexes", "sk-thm-tf-uniform-formula", "sk-cor-tf-point-counting", "sk-def-wrp-l2-definition"]
tags = ["sketch"]
+++
*Setting* (§17.3 of the tex). Take $S=\operatorname{Spec}k_0$ and
$V=\mathbf A^r_{k_0}$. For a Weil complex $K$, write $t_{K,n}(x)$ for the
alternating sum of the Frobenius traces at $x\in X_0(\mathbf F_{q^n})$.
Applying to $p_2$ the formula for the trace function of a direct image with
compact support ([sk-thm-tf-uniform-formula]), we get

$$
 t_{\operatorname{FT}_\psi K,n}(y)
   =(-1)^r\sum_{x\in\mathbf F_{q^n}^r}
       t_{K,n}(x)\,
       \psi\bigl(\operatorname{Tr}_{\mathbf F_{q^n}/k_0}
                                      \langle x,y\rangle\bigr).
 \tag{17.3}
$$

The sign $(-1)^r$ comes from the shift in the definition of
$\operatorname{FT}_\psi$.

For every $n\ge1$,

$$
 \sum_y|\iota t_{\operatorname{FT}_\psi K,n}(y)|^2
       =q^{nr}\sum_x|\iota t_{K,n}(x)|^2.
$$

Consequently, on a line, the $L^2$ growth parameter $\nu$ of
[sk-def-wrp-l2-definition] and [sk-thm-wrp-l2-dictionary]
satisfies $\nu(\operatorname{FT}_\psi K)=\nu(K)+1$ whenever these
parameters are finite.

*Complement.* On the line, applying (17.3) twice with $\psi$ and $\psi^{-1}$
gives the trace-level inversion
$t_{\operatorname{FT}_{\psi^{-1}}\operatorname{FT}_\psi K,n}=q^n\,t_{K,n}$,
the trace function of $K(-1)$.
