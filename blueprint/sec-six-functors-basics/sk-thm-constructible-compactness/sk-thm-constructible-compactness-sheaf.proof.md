+++
kind = "proof"
of = "det-constructible-compactness-sheaf"
+++
Replacing $K_\lambda$ by $K_\lambda[m]$ we may take $m=0$. Put $T=\tau_{\geq-d_C}\tau_{\leq0}$. Since
cohomology commutes with direct sums ([sk-cor-ambient-ind-derived]), truncations commute with direct
sums: $T(\bigoplus K_\lambda)\cong\bigoplus T(K_\lambda)$, compatibly with the truncation maps. The square

$$
\begin{matrix}
\bigoplus_\lambda\Hom(C,K_\lambda)&\longrightarrow&\Hom(C,\bigoplus_\lambda K_\lambda)\\
\downarrow&&\downarrow\\
\bigoplus_\lambda\Hom(C,TK_\lambda)&\longrightarrow&\Hom(C,\bigoplus_\lambda TK_\lambda)
\end{matrix}
$$

commutes, and its vertical maps are isomorphisms by [sk-lem-finite-window] (applied to each
$K_\lambda$ and to $\bigoplus K_\lambda$, all in $\Dic(X,\Lambda)$). The family $(TK_\lambda)$ has
cohomology in the common interval $[-d_C,0]$, so the bottom map is an isomorphism by
[det-constructible-compactness-bounded]. Hence so is the top map.
