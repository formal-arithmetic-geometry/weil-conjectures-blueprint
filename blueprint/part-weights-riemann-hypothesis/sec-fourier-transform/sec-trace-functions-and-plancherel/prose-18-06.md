+++
id = "prose-18-06"
kind = "hidden"
title = "Trace functions and Plancherel"
order = 725
+++
On trace functions, the Fourier transform is the classical discrete
Fourier transform over $\mathbf F_{q^n}$, and the Plancherel formula
tells us how it changes the growth of squared trace sums, and this
growth determines the weight of a pure sheaf
(Theorem [sk-thm-wrp-l2-dictionary]). In
Section [sec-deligne-laumon-a1] we find the weight of the transform
in this way. The heuristic is simple. A lisse sheaf of weight $w$ on a
dense open of the line has about $q^n$ points over $\mathbf F_{q^n}$,
each contributing a squared trace of size $q^{nw}$, so the sum of
squared traces grows like $q^{n(w+1)}$; multiplying by $q^n$, as
Plancherel does, raises the weight read off from this growth by one. For
the Kummer sheaf of a nontrivial character $\chi$, of weight $0$, the
transform has trace $-\overline\chi(y)g$ at $y\ne0$ with $|g|^2=q$, and
the sum of its squared traces is $(q-1)q$, as Plancherel predicts.
The only input is the trace formula for $Rp_{2!}$, which converts the
transform into the discrete Fourier transform of trace functions; the
orthogonality of characters does the rest. Plancherel is an identity
of numbers and gives no information about the transform as a sheaf.
That is the subject of the next two subsections.

In this subsection $S=\operatorname{Spec}k_0$ and
$V=\mathbf A^r_{k_0}$.
For a Weil complex $K$ on a $k_0$-scheme $X_0$, we write $t_{K,n}(x)$
for the alternating sum of the Frobenius traces at
$x\in X_0(\mathbf F_{q^n})$, as in Definition [sk-def-wrp-l2-definition].
Applying to $p_2$ the formula for the trace function of a direct image
with compact support (Corollary [sk-cor-tf-trace-function-pushforward]),
we get

$$
t_{\operatorname{FT}_\psi K,n}(y)
=(-1)^r\sum_{x\in\mathbf F_{q^n}^r}
t_{K,n}(x)\,
\psi\bigl(\operatorname{Tr}_{\mathbf F_{q^n}/k_0}
\langle x,y\rangle\bigr).
\tag{18.3}
$$

The sign $(-1)^r$ comes from the shift in the definition of
$\operatorname{FT}_\psi$.
