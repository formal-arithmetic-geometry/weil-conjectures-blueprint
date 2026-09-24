+++
id = "lem-fd-double-transform-trace"
kind = "lemma"
title = "The double transform has the trace function of the Tate twist"
order = 4162
uses = ["def-fd-additive-character", "def-fd-trace-function", "def-fd-transform", "def-wf-tate-twist", "lem-fd-additive-orthogonality", "lem-wf-tate-twist-frobenius", "thm-fd-fourier-trace"]
+++
Let $k_0=\mathbf F_q$ and $V=\mathbf A^1_k$ with $k=\bar k_0$, and let
$K$ be a constructible Weil complex on $V$ in the conventions of
[def-fd-trace-function]. Then for every $n\geq1$ and every
$y\in\mathbf F_{q^n}$ the trace functions of [def-fd-trace-function]
satisfy

$$
t_{\operatorname{FT}_{\psi^{-1}}\operatorname{FT}_\psi(K)}(y)
=q^n\,t_K(y)=t_{K(-1)}(y),
$$

the second equality being the trace of the Tate twist
[def-wf-tate-twist] at the point $y$ of degree $n$. This is the
trace-level half of the inversion formula of [lem-fd-inversion]; it
does not by itself identify the two complexes, equal trace functions not
forcing an isomorphism.

## Proof

Use the trace function and additive character of
[def-fd-trace-function], [def-fd-additive-character].
By the Fourier trace formula [thm-fd-fourier-trace], applied to the
complex $\operatorname{FT}_\psi(K)$ and to the character $\psi^{-1}$,

$$
t_{\operatorname{FT}_{\psi^{-1}}\operatorname{FT}_\psi(K)}(y)
=-\sum_{x\in\mathbf F_{q^n}}t_{\operatorname{FT}_\psi(K)}(x)\,
\psi\Bigl(-\operatorname{Tr}_{\mathbf F_{q^n}/\mathbf F_p}(xy)\Bigr),
$$

while the same formula applied to $K$ gives
$t_{\operatorname{FT}_\psi(K)}(x) =-\sum_{z\in\mathbf F_{q^n}}t_K(z)\psi(\operatorname{Tr}(xz))$.
Substituting and exchanging the two finite sums,

$$
t_{\operatorname{FT}_{\psi^{-1}}\operatorname{FT}_\psi(K)}(y)
=\sum_{z\in\mathbf F_{q^n}}t_K(z)
\sum_{x\in\mathbf F_{q^n}}
\psi\bigl(\operatorname{Tr}_{\mathbf F_{q^n}/\mathbf F_p}(x(z-y))\bigr),
$$

the two signs cancelling. The inner sum is evaluated by the additive
orthogonality [lem-fd-additive-orthogonality]: it equals $q^n$ when
$z=y$ and vanishes otherwise, so the double sum collapses to
$q^n\,t_K(y)$. Finally the trace of the Tate twist is
$t_{K(-1)}(y)=q^nt_K(y)$: the twist multiplies the local Frobenius
eigenvalues by $q$ by the Frobenius normalization of
[lem-wf-tate-twist-frobenius], hence their $n$-th power sums – the
traces at the points of $\mathbf F_{q^n}$ – by $q^n$.
