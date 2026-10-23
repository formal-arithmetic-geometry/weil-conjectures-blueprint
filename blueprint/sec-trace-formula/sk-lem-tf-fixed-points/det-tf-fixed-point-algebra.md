+++
id = "det-tf-fixed-point-algebra"
kind = "lemma"
title = "The coordinate ring of the Frobenius fixed scheme"
order = 3509
uses = ["det-tf-fixed-point-equations"]
+++
Let $\mathfrak a\subset k_0[t_1,\ldots,t_r]$ be an ideal, $X_0=\operatorname{Spec}k_0[t]/\mathfrak a$,
and $m\geq1$. Evaluation at the points $\lambda\in\mathbf F_{q^m}^r$ gives an isomorphism of
$k$-algebras

$$
 k[t_1,\ldots,t_r]/(t_i^{q^m}-t_i)_i\xrightarrow{\ \sim\ }\prod_{\lambda\in\mathbf F_{q^m}^r}k,
$$

and it induces an isomorphism

$$
 k[t_1,\ldots,t_r]/\bigl(\mathfrak a\,k[t]+(t_i^{q^m}-t_i)_i\bigr)\xrightarrow{\ \sim\ }
 \prod_{x\in X_0(\mathbf F_{q^m})}k .
$$

Consequently, by [det-tf-fixed-point-equations],
$\operatorname{Fix}(\Phi_X^m)\simeq\coprod_{x\in X_0(\mathbf F_{q^m})}\operatorname{Spec}k$ for
affine $X_0$, compatibly with restriction to affine opens; in particular it is finite and
reduced over $k$.
