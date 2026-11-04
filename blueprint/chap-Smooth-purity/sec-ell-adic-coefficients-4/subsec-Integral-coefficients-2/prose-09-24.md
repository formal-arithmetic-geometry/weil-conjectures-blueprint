+++
id = "prose-09-24"
kind = "hidden"
title = "Integral coefficients (4)"
order = 775
+++
The orientation passes to towers as well. By the finite case each level of
$\omega_{f,\bullet}[-2d]$ is an invertible sheaf, so it is an invertible
sheaf of towers. The comparisons for vector bundles and for the deformation
family are maps of sheaves of towers in degree zero. Equality of such maps
can be tested level by level, unlike equality of maps in
$D(\operatorname{Tow})$ in general. Hence the uniqueness in
Lemma [lemma-section-normal-bundle] holds for them,
because it holds at each level. Composing the inverse of the orientation with the map
(9.4) on towers, we obtain an isomorphism, natural in the constructible tower $K_\bullet$,

$$
\gamma_{f,\bullet}(K_\bullet):f_\bullet^*K_\bullet(d)[2d]\xrightarrow{\sim}f_\bullet^!K_\bullet,
\tag{9.19}
$$

whose level $n$ is $\gamma_{f,\mathcal O_E/\ell^n}(K_n)$.

Both functors in
(9.18) preserve normalized towers. For
$Rf_{!,\bullet}$ this follows from the comparison $b$, and for
$f_\bullet^!$ from (9.17) and
(9.19).

Since $R\bar f_*$ and $j_!$ commute with $R\varprojlim$ [Stacks, [09BP](https://stacks.math.columbia.edu/tag/09BP)], we have

$$
Rf_{!,\mathcal O_E}M\simeq R\varprojlim_nRf_{!,\mathcal O_E/\ell^n}(M/\ell^n)
$$

for $M\in\Dbc(X,\mathcal O_E)$. For $K\in\Dbc(Y,\mathcal O_E)$ we put

$$
H_{f,\mathcal O_E}(K)=R\varprojlim_n f_{\mathcal O_E/\ell^n}^!(K/\ell^n)\in\Dbc(X,\mathcal O_E),
\tag{9.20}
$$

the derived limit of the normalized tower $f_\bullet^!\operatorname{red}_YK$.

The functor $H_{f,\mathcal O_E}$ is given by an
explicit formula, whereas we only know that $f^!_{\mathcal O_E}$ exists. The
next proposition shows that the formula defines a right adjoint, and so,
by uniqueness, computes $f^!_{\mathcal O_E}$.
