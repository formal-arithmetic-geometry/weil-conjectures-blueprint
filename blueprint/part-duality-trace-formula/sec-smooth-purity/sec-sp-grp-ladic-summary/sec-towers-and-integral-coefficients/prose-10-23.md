+++
id = "prose-10-23"
kind = "hidden"
title = "Towers and integral coefficients (3)"
order = 470
+++
The orientation passes to towers in the same way: $\omega_{f,\bullet}[-2d]$ is an invertible
sheaf of towers, the comparisons for vector bundles and for the deformation family are maps
of sheaves of towers in degree zero, and the uniqueness of Lemma [sk-lem-lem-sp-dnc-naturality]
holds for them level by level. Composing the inverse of the orientation with the map
(10.9) on towers, we obtain an isomorphism, natural in the constructible tower $K_\bullet$,

$$
\gamma_{f,\bullet}(K_\bullet):f_\bullet^*K_\bullet(d)[2d]\xrightarrow{\sim}f_\bullet^!K_\bullet,
\tag{10.18}
$$

whose level $n$ is $\gamma_{f,\mathcal O_E/\ell^n}(K_n)$. Both functors in
(10.17) preserve normalized towers, $Rf_{!,\bullet}$ by the
comparison $b$ and $f_\bullet^!$ by (10.16) and (10.18).
Since $R\bar f_*$ and $j_!$ commute with $R\varprojlim$ [Stacks, Tag 09BP](https://stacks.math.columbia.edu/tag/09BP), we have
$Rf_{!,\mathcal O_E}M\simeq R\varprojlim_nRf_{!,\mathcal O_E/\ell^n}(M/\ell^n)$ for
$M\in\Dbc(X,\mathcal O_E)$. For $K\in\Dbc(Y,\mathcal O_E)$ we put

$$
H_{f,\mathcal O_E}(K)=R\varprojlim_n f_{\mathcal O_E/\ell^n}^!(K/\ell^n)\in\Dbc(X,\mathcal O_E),
\tag{10.19}
$$

the derived limit of the normalized tower $f_\bullet^!\operatorname{red}_YK$.
