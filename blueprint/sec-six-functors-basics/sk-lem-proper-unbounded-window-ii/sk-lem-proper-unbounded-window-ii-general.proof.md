+++
kind = "proof"
of = "det-proper-unbounded-window-ii-general"
+++
Fix $q$ and put $W=\tau_{\geq q-2d-1}\tau_{\leq q}$. Direct sums of sheaves are exact, so
$\mathcal H^n(\bigoplus K_\alpha)=\bigoplus\mathcal H^n(K_\alpha)$ and $W(\bigoplus K_\alpha)\cong\bigoplus W(K_\alpha)$,
compatibly with the truncation maps. Consider the commutative diagram

$$
\begin{matrix}
\bigoplus_\alpha\mathcal H^q(Rp_*K_\alpha)&\longrightarrow&\mathcal H^q(Rp_*\bigoplus_\alpha K_\alpha)\\
\downarrow&&\downarrow\\
\bigoplus_\alpha\mathcal H^q(Rp_*WK_\alpha)&\longrightarrow&\mathcal H^q(Rp_*\bigoplus_\alpha WK_\alpha)
\end{matrix}
$$

(left: sums commute with $\mathcal H^q$). The vertical maps are isomorphisms by the window isomorphism of
[sk-lem-proper-unbounded-window], applied to each $K_\alpha$ and to $\bigoplus K_\alpha\in\Dic(X,\Lambda)$ (both
vertical maps are zig-zags of truncation maps, and these are compatible with sums). The family $(WK_\alpha)$
has cohomology in $[q-2d-1,q]$, so the bottom map is an isomorphism by
[det-proper-unbounded-window-ii-bounded]. Hence the top map, which is $\mathcal H^q$ of the comparison
map, is an isomorphism. As $q$ is arbitrary, the comparison map is a quasi-isomorphism, i.e. an
isomorphism in $\D(Y_{\mathrm{proét}},\Lambda)$.
