+++
kind  = "proof"
of    = "sk-cor-plancherel"
+++
Apply $\iota$ to the finite Fourier sum of P8, multiply by its complex
conjugate and sum over $y$; since $\iota\psi_n(z)$ is a complex root of
unity, $\overline{\iota\psi_n(x'y)}=\iota\psi_n(-x'y)$, so

$$
\sum_y\Bigl|\sum_x\iota t_K(x)\,\iota\psi_n(xy)\Bigr|^2
=\sum_y\sum_{x,x'}\iota t_K(x)\,\overline{\iota t_K(x')}\,
\iota\psi_n\bigl((x-x')y\bigr);
$$

the orthogonality of [sk-lem-orthogonality] (an identity in $\Qlb$,
transported by $\iota$) makes the inner $y$-sum $q^n$
on the diagonal and $0$ off it, which is the identity. This is the classical
Plancherel theorem for the finite group $(\mathbf F_{q^n},+)$, transported to
trace functions; no weight enters.
