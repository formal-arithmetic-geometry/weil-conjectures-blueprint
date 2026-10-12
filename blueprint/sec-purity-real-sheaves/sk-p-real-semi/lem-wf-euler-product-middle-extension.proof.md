+++
kind  = "proof"
of    = "lem-wf-euler-product-middle-extension"
+++
This is the curve case of the Euler-product form of the trace formula
[thm-trf-l-function-euler-product], applied with $\Lambda=\Qlb$ in
the coefficient category [def-weil-pbc-qbar-category], to the curve
$X_0$ (separated of finite type, of dimension one) and the
constructible sheaf $K=j_*\mathcal F$ placed in degree zero, under the
hypotheses of [thm-trf-grothendieck-lefschetz-qbar] with which the
trace formula is applied to it. Its $L(X_0,j_*\mathcal F,t)$ is the
left-hand side (the local factor at $x$ being
$\det(1-F_xt^{d(x)}\mid(j_*\mathcal F)_{\bar x})$, with $e_x=d(x)$),
and its items (2) and (3) give

$$
L(X_0,j_*\mathcal F,t)=
\frac{\det(1-Ft,H_c^1(X,j_*\mathcal F))}
{\det(1-Ft,H_c^0(X,j_*\mathcal F))\,\det(1-Ft,H_c^2(X,j_*\mathcal F))}.
$$

It remains to see that the degree-zero factor is $1$, i.e.
$H_c^0(X,j_*\mathcal F)=0$: a compactly supported global section of
$j_*\mathcal F$ vanishes in a neighborhood of every boundary point,
hence restricts to zero on the complement of its finite support in the
connected open curve, and by lissity it is zero.
