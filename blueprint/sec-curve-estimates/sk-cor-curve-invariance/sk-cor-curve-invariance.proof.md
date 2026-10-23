+++
kind = "proof"
of = "sk-cor-curve-invariance"
uses = ["sk-thm-curve-package", "sk-prop-sf-comparison", "sk-lem-curve-dense-open"]
+++
Choose compatible algebraic closures $\bar k\subseteq\bar k'$. The extensions
$\bar k/k$ and $\bar k'/k'$ are purely inseparable, so the base-change
morphisms $C_{\bar k}\to C$ and $C_{\bar k'}\to C_{k'}$ are universal
homeomorphisms and induce equivalences of étale topoi (Stacks, Tag 03SI). By
[sk-prop-sf-comparison], the vertical maps in

$$
\begin{array}{ccc}
H^q(C,F) & \longrightarrow & H^q(C_{k'},F|)\\
\big\downarrow{\scriptstyle\sim} & & \big\downarrow{\scriptstyle\sim}\\
H^q(C_{\bar k},F|) & \longrightarrow & H^q(C_{\bar k'},F|)
\end{array}
$$

are isomorphisms. The bottom map is an isomorphism by $(C_7)$ of
[sk-thm-curve-package]. All maps are pullback maps, so the square commutes and
the top map is an isomorphism (Stacks, Tag 0A5E).

In the main text, the curve input to proper base change and the comparison of
closed fibres under field extension restate [sk-thm-curve-package] and this
corollary, and the cohomology of $\PP^1$ over an algebraically closed field,
with its normalized Kummer class, comes from [sk-thm-curveestimate].
