+++
id = "prose-10-16"
kind = "hidden"
title = "Orientation on towers and the integral adjoint"
order = 3314
+++
The orientation passes to towers in the same way: $\omega_{f,\bullet}[-2d]$ is an invertible
sheaf of towers, the comparisons for vector bundles and for the deformation family are maps
of sheaves of towers in degree zero, and the uniqueness of Lemma [sk-thm-dnc]
holds for them level by level. Composing the inverse of the orientation with the canonical map
$f^{*}K\otimes^{\mathbf L}\omega_{f}\to f^{!}K$ on towers, we obtain an isomorphism, natural in the constructible tower $K_\bullet$,

$$
\gamma_{f,\bullet}(K_\bullet):f_\bullet^*K_\bullet(d)[2d]\xrightarrow{\sim}f_\bullet^!K_\bullet,
$$

whose level $n$ is $\gamma_{f,\mathcal O_E/\ell^n}(K_n)$. Both functors in
the adjunction of [sk-prop-sp-tower-geometric] preserve normalized towers, $Rf_{!,\bullet}$ by the
comparison $b$ and $f_\bullet^!$ by the compatibility $c_{A,B}(K)\circ(\gamma_{f,A}(K))_B=\gamma_{f,B}(K_B)$
of the maps $\gamma_{f,A}$ with change of coefficients and the isomorphism $\gamma_{f,\bullet}$ above.
Since $R\bar f_*$ and $j_!$ commute with $R\varprojlim$ ([Stacks, Tag 09BP](https://stacks.math.columbia.edu/tag/09BP)), we have
$Rf_{!,\mathcal O_E}M\simeq R\varprojlim_nRf_{!,\mathcal O_E/\ell^n}(M/\ell^n)$ for
$M\in\Dbc(X,\mathcal O_E)$. For $K\in\Dbc(Y,\mathcal O_E)$ we put

$$
H_{f,\mathcal O_E}(K)=R\varprojlim_n f_{\mathcal O_E/\ell^n}^!(K/\ell^n)\in\Dbc(X,\mathcal O_E),
$$

the derived limit of the normalized tower $f_\bullet^!\operatorname{red}_YK$.
