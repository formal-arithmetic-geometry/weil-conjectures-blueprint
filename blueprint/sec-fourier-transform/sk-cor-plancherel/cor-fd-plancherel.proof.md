+++
kind  = "proof"
of    = "cor-fd-plancherel"
+++
Apply $\iota$ to the finite Fourier sum of [thm-fd-fourier-trace], multiply it by its complex conjugate, and sum over $y$; since $\iota\psi_n(z)$ is a complex root of unity, $\overline{\iota\psi_n(x'y)}=\iota\psi_n(-x'y)$, so

$$
\sum_{y}\Bigl|\sum_x \iota t_K(x)\,\iota\psi_n(xy)\Bigr|^2
=\sum_{y}\sum_{x,x'}\iota t_K(x)\,\overline{\iota t_K(x')}\ \iota\psi_n((x-x')y).
$$

The orthogonality relation [lem-fd-additive-orthogonality] (an identity in $\Qlb$, transported by $\iota$) makes the inner $y$-sum equal to $q^n$ when $x=x'$ and zero otherwise. The surviving diagonal sum is exactly the right-hand side written with the absolute values of the trace function of [def-fd-trace-function].
