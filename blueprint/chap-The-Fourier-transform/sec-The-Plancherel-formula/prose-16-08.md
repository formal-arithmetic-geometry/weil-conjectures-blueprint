+++
id = "prose-16-08"
kind = "hidden"
title = "The Plancherel formula (1)"
order = 1240
+++
On trace functions, the Fourier transform is, up to the sign $(-1)^r$, the
discrete Fourier transform over $\mathbf F_{q^n}$ for the character
$\psi\circ\operatorname{Tr}_{\mathbf F_{q^n}/k_0}$
(equation (16.3) below). The Plancherel formula
then says how it changes the growth of squared trace sums, and for a pure sheaf
this growth is the weight
(Theorem [theorem-weights-sums-squared-traces]). This is how we find
the weight of the transform in Chapter [chap-The-Deligne-Laumon-theorem-for-curves]: on the
line, Plancherel multiplies the sums of squared traces by $q^n$, and so it
raises the weight read off from their growth by one.

In this section $S=\operatorname{Spec}k_0$ and
$V=\mathbf A^r_{k_0}$.
For a Weil complex $K$ on a $k_0$-scheme $X_0$, we write $t_{K,n}(x)$
for the alternating sum of the Frobenius traces at
$x\in X_0(\mathbf F_{q^n})$, as in Definition [definition-growth-squared-traces].
With this notation, the dictionary (Proposition [proposition-function-sheaf-dictionary])
computes the trace function of the transform step by step. For
$y\in\mathbf F_{q^n}^r$, the shift contributes $(-1)^r$ (chain formula of
Proposition [proposition-properties-trace]), part (3) sums over
the fibre of $p_2$, and part (2) splits the trace of the tensor product:

$$
t_{\operatorname{FT}_\psi K,n}(y)
=(-1)^r\,t_{Rp_{2!}(p_1^*K\otimes\mathcal K_\psi),n}(y)
=(-1)^r\sum_{x\in\mathbf F_{q^n}^r}t_{p_1^*K,n}(x,y)\,
t_{\mathcal K_\psi,n}(x,y).
$$

By part (1), $t_{p_1^*K,n}(x,y)=t_{K,n}(x)$, and by part (1) and
Lemma [lemma-artin-schreier-character-sheaf],
$t_{\mathcal K_\psi,n}(x,y)=\psi(\operatorname{Tr}_{\mathbf F_{q^n}/k_0}\langle x,y\rangle)$.
Hence

$$
t_{\operatorname{FT}_\psi K,n}(y)
=(-1)^r\sum_{x\in\mathbf F_{q^n}^r}
t_{K,n}(x)\,
\psi\bigl(\operatorname{Tr}_{\mathbf F_{q^n}/k_0}
\langle x,y\rangle\bigr).
\tag{16.3}
$$
