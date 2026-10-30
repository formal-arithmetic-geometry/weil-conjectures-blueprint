+++
id = "prose-13-12"
kind = "hidden"
title = "The trace formula with finite coefficients"
order = 599
+++
This is the main theorem of the section, and the other coefficient
rings follow from it in Section [sec-tf-coefficient-transport]. The only
compactification the proof uses is $\mathbf A^1\subset\mathbf P^1$.
Every affine scheme of finite type over $\mathbf F_q$ is a closed
subscheme of some $\mathbf A^d$, the fibres of a
coordinate projection lie in $\mathbf A^1$, and the only new fixed
point of $\mathbf P^1$, the rational point $\infty$, carries the zero
stalk of $j_!K$. Thus the Lefschetz–Verdier formula and the curve
computation of Proposition [sk-p-frob] are applied
only to $\mathbf P^1$. Since the fibres over points of
$Y_0(\mathbf F_{q^m})$ are schemes over $\mathbf F_{q^m}$, we prove the
theorem for all finite fields at once.

The base of the induction, finite schemes, shows in miniature what the
formula counts. For $X_0=\operatorname{Spec}\mathbf F_{q^2}$ and $K=A$,
the scheme $X$ consists of two points interchanged by $\Phi_X$. Hence
$T_{c_1}$ is the swap of $A\oplus A$, with trace
$0=\#X_0(\mathbf F_q)$, and $T_{c_2}$ is the identity, with trace
$2=\#X_0(\mathbf F_{q^2})$. In general $T_{c_m}$ is a block permutation
matrix, and only the points fixed by $\Phi_X^m$ contribute to its trace.

We first prove the trace formula for a finite coefficient ring and
for an arbitrary Frobenius correspondence $\psi:\Phi_X^*K\to K$.
We do not require $\psi$ to be invertible, because in general an integral model of a rational Weil complex
carries only a multiple of the Weil structure
(Lemma [sk-lem-tf-rational-model]). The iterates $\psi_m$, the
endomorphisms $T_{c_m}(\psi_m)$ and the stalk
maps $\psi_{m,\bar x}$ are those of Definition [sk-d-weil].
