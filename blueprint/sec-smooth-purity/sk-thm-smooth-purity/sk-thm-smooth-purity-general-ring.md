+++
id = "det-sp-finite-general-ring"
kind = "lemma"
title = "Smooth purity over an arbitrary finite coefficient ring"
order = 3350
uses = ["thm-pur-diagonal-dualizing-object", "thm-pur-cohomological-smoothness", "det-sp-reduction-exceptional", "det-sp-scalar-extension-functor"]
+++
Let $A$ be a finite commutative ring with $\ell^nA=0$, and let $f:X\to Y$ be
smooth of pure relative dimension $d$. Then:

1. the relative dualizing complex $\omega_{f,A}=f_A^!A_Y$ has an orientation
   $\omega_{f,A}\xrightarrow{\sim}A_X(d)[2d]$, namely the composite
   $$
   \omega_{f,A}=f_A^!\bigl((\mathbf Z/\ell^n)_Y\bigr)_A
   \xleftarrow[\ \sim\ ]{\ c_{\mathbf Z/\ell^n,A}\ }(\omega_{f,\mathbf Z/\ell^n})_A
   \xrightarrow{\ \sim\ }\bigl((\mathbf Z/\ell^n)_X(d)[2d]\bigr)_A=A_X(d)[2d],
   $$
   where the last map is the extension of scalars of the orientation of
   [thm-pur-diagonal-dualizing-object] and $c_{\mathbf Z/\ell^n,A}$ is the
   coefficient comparison of [det-sp-reduction-exceptional];
2. it agrees with the orientation obtained by running the diagonal and
   deformation construction directly with $A$-coefficients;
3. for every $K\in\Dctf(Y_{\mathrm{proét}},A)$ the composite
   $$
   \gamma_{f,A}(K):\ f_A^*K(d)[2d]\simeq f_A^*K\otimes^{\mathbf L}_{A_X}A_X(d)[2d]
   \xrightarrow{\ \sim\ }f_A^*K\otimes^{\mathbf L}_{A_X}\omega_{f,A}
   \xrightarrow{\ \sim\ }f_A^!K
   $$
   of the inverse orientation and the tensor map is an isomorphism, natural
   in $K$, and it does not depend on the choice of $n$.
