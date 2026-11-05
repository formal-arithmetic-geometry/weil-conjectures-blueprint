+++
id = "prose-12-19"
kind = "hidden"
title = "Finite coefficients"
order = 1005
+++
The proof uses a single compactification, $\mathbf A^1\subset\mathbf P^1$, so the
Lefschetz–Verdier formula and the curve
computation of Proposition [proposition-frobenius-local-term-curve]
are applied only on $\mathbf P^1$. This suffices because every affine scheme of finite type over $\mathbf F_q$ is a closed subscheme of some $\mathbf A^d$, and the fibres of a
coordinate projection lie in $\mathbf A^1$. On $\mathbf P^1$ the only new fixed point is the rational point $\infty$, where $j_!K$ has
zero stalk. The fibres over points of $Y_0(\mathbf F_{q^m})$ are schemes over $\mathbf F_{q^m}$, so we prove the theorem for all finite fields at once. The other coefficient rings are treated in Section [sec-ell-adic-coefficients-5].

The base of the induction is the case of finite schemes. There we
can see directly what the formula counts. For example, take $X_0=\operatorname{Spec}\mathbf F_{q^2}$ and $K=A$. Then the scheme $X$ consists of two points interchanged by $\Phi_X$. Hence
$T_{c_1}$ is the swap of $A\oplus A$, with trace
$0=\#X_0(\mathbf F_q)$, and $T_{c_2}$ is the identity, with trace
$2=\#X_0(\mathbf F_{q^2})$. In general $T_{c_m}$ is a block permutation
matrix, and only the points fixed by $\Phi_X^m$ contribute to its trace.

The iterates $\psi_m$, the
endomorphisms $T_{c_m}(\psi_m)$ and the stalk
maps $\psi_{m,\bar x}$ are those of Definition [definition-frobenius-correspondences-their-operators].
