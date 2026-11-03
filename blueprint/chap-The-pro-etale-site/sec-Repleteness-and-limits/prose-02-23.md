+++
id = "prose-02-23"
kind = "hidden"
title = "Repleteness and limits (3)"
order = 90
+++
Derived limits of countable towers have an explicit model. For a
countable tower of modules, write $t_n:M_{n+1}\to M_n$ and let
$T:\prod_nM_n\to\prod_nM_n$ be $T((m_n)_n)=(t_n(m_{n+1}))_n$. For a
tower $(K_n)$ in $D(X_{\mathrm{pro}\acute{e}t},\mathcal R)$, represented by a tower of
complexes $K_{n+1}\to K_n$, the same formula defines $T$ termwise, and the
derived inverse limit is the homotopy fibre of $1-T$

$$
R\varprojlim_n K_n
=
\fib\Bigl(
\prod_n K_n\xrightarrow{\,1-T\,}\prod_n K_n
\Bigr)=\Cone(1-T)[-1].
\tag{2.1}
$$

The cone is formed on the level of complexes, so that the
construction is functorial in the tower. By Proposition [proposition-exact-products]
the termwise products are the derived products, and so, by [Stacks, [0940](https://stacks.math.columbia.edu/tag/0940)],
this cone agrees with the derived inverse limit.
