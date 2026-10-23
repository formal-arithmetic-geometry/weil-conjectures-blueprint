+++
kind = "proof"
of = "lem-weil-pbc-etale-ring-map-conormal-criterion"
+++
Since $\alpha$ is surjective, $S=P/J$, and $J/J^2$ is an $S$-module. The conormal map $c:J/J^2\to S\otimes_P\Omega_{P/R}$, $g\bmod J^2\mapsto1\otimes\mathrm dg$, is well defined and $S$-linear. The module $\Omega_{P/R}$ is free on $\mathrm dx_1,\dots,\mathrm dx_n$ with $\mathrm dg=\sum_k(\partial g/\partial x_k)\,\mathrm dx_k$, so base change gives an $S$-linear isomorphism $t:S\otimes_P\Omega_{P/R}\xrightarrow{\sim}\bigoplus_{k=1}^nS\,\mathrm dx_k$, and $t\circ c$ sends $g\bmod J^2$ to $\sum_k\alpha(\partial g/\partial x_k)\,\mathrm dx_k$. Hence $\mathrm d=t\circ c$; in particular $\mathrm d$ is well defined and $S$-linear.

The polynomial algebra $P$ is formally smooth over $R$. For a presentation $S=P/J$ by a formally smooth $R$-algebra, the first homology of the naive cotangent complex is the kernel of the conormal map, so $c$ is injective if and only if $H_1(\mathrm{NL}_{S/R})=0$. The conormal sequence $J/J^2\xrightarrow{c}S\otimes_P\Omega_{P/R}\to\Omega_{S/R}\to0$ is exact, so $c$ is surjective if and only if $\Omega_{S/R}=0$: if $c$ is surjective every differential is the image of some $c(a)$, hence zero; conversely if $\Omega_{S/R}=0$, exactness gives every element a preimage under $c$.

Since $J$ is finitely generated, $S$ is a finitely presented $R$-algebra. The morphism $\operatorname{Spec}S\to\operatorname{Spec}R$ is etale if and only if $R\to S$ is etale, and a finitely presented algebra is etale if and only if it is formally etale, i.e. if and only if $H_1(\mathrm{NL}_{S/R})=0$ and $\Omega_{S/R}=0$. By the previous step this holds if and only if $c$ is bijective, and since $t$ is an isomorphism, if and only if $\mathrm d$ is bijective.
