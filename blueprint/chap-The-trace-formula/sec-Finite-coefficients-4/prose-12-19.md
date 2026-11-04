+++
id = "prose-12-19"
kind = "hidden"
title = "Finite coefficients"
order = 999
+++
The only compactification the proof uses is $\mathbf A^1\subset\mathbf P^1$.
Every affine scheme of finite type over $\mathbf F_q$ is a closed
subscheme of some $\mathbf A^d$, and the fibres of a
coordinate projection lie in $\mathbf A^1$. On $\mathbf P^1$ the only new fixed
point is the rational point $\infty$, where $j_!K$ has
zero stalk. Thus we apply the Lefschetz–Verdier formula and the curve
computation of Proposition [proposition-frobenius-local-term-curve]
only to $\mathbf P^1$. The fibres over points of
$Y_0(\mathbf F_{q^m})$ are schemes over $\mathbf F_{q^m}$, so we prove the
theorem for all finite fields at once. We treat the other coefficient
rings in Section [sec-ell-adic-coefficients-5].

The base of the induction is the case of finite schemes. There we
can see directly what the formula counts. Take $X_0=\operatorname{Spec}\mathbf F_{q^2}$ and $K=A$.
The scheme $X$ consists of two points interchanged by $\Phi_X$. Hence
$T_{c_1}$ is the swap of $A\oplus A$, with trace
$0=\#X_0(\mathbf F_q)$, and $T_{c_2}$ is the identity, with trace
$2=\#X_0(\mathbf F_{q^2})$. In general $T_{c_m}$ is a block permutation
matrix, and only the points fixed by $\Phi_X^m$ contribute to its trace.

The iterates $\psi_m$, the
endomorphisms $T_{c_m}(\psi_m)$ and the stalk
maps $\psi_{m,\bar x}$ are those of Definition [definition-frobenius-correspondences-their-operators].
