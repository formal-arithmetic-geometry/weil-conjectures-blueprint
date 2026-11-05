+++
kind = "proof"
of = "proposition-twisting-weight-zero-adding-dual--1"
order = 1194011
uses = ["definition-weights"]
+++
A nonzero sheaf has a nonzero stalk at some closed point $x$. Choose a
Frobenius eigenvalue $\alpha$ there; it is nonzero since Frobenius is
invertible. If $d=[\kappa(x):k_0]$, then $d>0$ and purity gives
$|\iota(\alpha)|=q^{dw/2}$. Choose a $d$th root $b$ of $\alpha^{-1}$
in $\overline{\mathbf Q}_\ell$. It is nonzero, and

$$
|\iota(b)|^d=|\iota(\alpha)|^{-1}=q^{-dw/2}.
$$

Taking the positive $d$th root gives the required equality. This is the
argument of `AlgebraicGeometry.WeilSheaf.exists_norm_eq_of_isPunctuallyPureOfWeight`;
the nonzero stalk is supplied by
`AlgebraicGeometry.WeilSheaf.exists_nontrivial_stalk_of_not_isZero`.
