+++
id = "sk-cor-plancherel"
kind = "corollary"
title = "Plancherel"
lean = ["FiniteField.sum_norm_sq_fourierTransform", "AlgebraicGeometry.WeilComplex.traceFunction_fourierTransform", "AlgebraicGeometry.WeilComplex.traceEnergy_fourierTransform"]
order = 4178
uses = ["sk-lem-as-properties", "sk-thm-inversion", "sk-def-sf-weil-complexes", "sk-thm-tf-uniform-formula", "sk-cor-tf-point-counting", "sk-def-wrp-l2-definition"]
tags = ["sketch"]
+++
*Setting* (§17.3 of the tex). Take $S=\operatorname{Spec}k_0$ and
$V=\mathbf A^1_{k_0}$, identified with its dual by the multiplication
pairing $\mu(x,y)=xy$, so that $\mathcal K_\psi=\mu^*\mathcal L_\psi$ and
$\operatorname{FT}_\psi K=Rp_{2!}(p_1^*K\otimes\mathcal K_\psi)[1]$ is a
transform of Weil complexes on $\mathbf A^1_{k_0}$. For a Weil complex $K$ on $\mathbf A^1_{k_0}$, write
$t_{K,n}(x)$ for the alternating sum of the Frobenius traces at
$x\in\mathbf A^1(\mathbf F_{q^n})=\mathbf F_{q^n}$. Applying to $p_2$ the
formula for the trace function of a direct image with compact support
([sk-thm-tf-uniform-formula]), we get, for every $n\ge1$ and
$y\in\mathbf F_{q^n}$,

$$
 t_{\operatorname{FT}_\psi K,n}(y)
   =-\sum_{x\in\mathbf F_{q^n}}
       t_{K,n}(x)\,
       \psi\bigl(\operatorname{Tr}_{\mathbf F_{q^n}/k_0}(xy)\bigr).
 \tag{17.3}
$$

The sign $-1$ comes from the shift $[1]$ in the definition of
$\operatorname{FT}_\psi$.

For $\psi$ nontrivial, every field embedding
$\iota:\overline{\mathbf Q}_\ell\hookrightarrow\mathbf C$ and every $n\ge1$,

$$
 \sum_{y\in\mathbf F_{q^n}}|\iota t_{\operatorname{FT}_\psi K,n}(y)|^2
       =q^{n}\sum_{x\in\mathbf F_{q^n}}|\iota t_{K,n}(x)|^2.
$$

Consequently, the $L^2$ growth parameter $\nu$ of
[sk-def-wrp-l2-definition] and [sk-thm-wrp-l2-dictionary]
satisfies $\nu(\operatorname{FT}_\psi K)=\nu(K)+1$ whenever these
parameters are finite.

*Complement.* For $\psi$ nontrivial, applying (17.3) twice with $\psi$ and $\psi^{-1}$
gives the trace-level inversion
$t_{\operatorname{FT}_{\psi^{-1}}\operatorname{FT}_\psi K,n}=q^n\,t_{K,n}$,
the trace function of $K(-1)$.
